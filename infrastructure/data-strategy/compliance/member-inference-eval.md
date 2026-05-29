# SOP: Member-Inference Evaluation Methodology
**Control**: NIH GDS Policy 2025 — Privacy-preserving model release
**Effective**: 2026-05-19 | **Owner**: ML Engineering + Privacy Officer | **Review**: Per model release

## Purpose

Before releasing any model trained on controlled-access data (Tier 3 or 4),
evaluate its susceptibility to **membership inference attacks** — techniques
that let an adversary determine whether a specific individual's data was in
the training set.

Required for: any model released publicly or to collaborators that was trained
on data under a DUC, NIH NDA agreement, or containing de-identified PHI.

## Evaluation Protocol

### Step 1: Shadow-Model Attack (Standard Benchmark)

```python
#!/usr/bin/env python3
"""
Membership inference evaluation using shadow models.
Adapted from Shokri et al. (2017) and Salem et al. (2019).
"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

def evaluate_membership_inference(
    target_model,          # The model to evaluate
    train_data,            # Data the model WAS trained on (sample)
    holdout_data,          # Data the model was NOT trained on
    n_shadow_models=10,
    shadow_train_size=500,
):
    """
    Returns:
      auc: AUC of the attack classifier. AUC ~0.5 = random = good.
           AUC > 0.6 = concerning. AUC > 0.7 = likely memorization.
    """
    # Get loss values for member vs non-member
    member_losses = [target_model.loss(x) for x in train_data]
    nonmember_losses = [target_model.loss(x) for x in holdout_data]

    X = np.array(member_losses + nonmember_losses).reshape(-1, 1)
    y = np.array([1]*len(member_losses) + [0]*len(nonmember_losses))

    # Train attack classifier
    attack_clf = RandomForestClassifier(n_estimators=100, random_state=42)
    # Use cross-validation for AUC estimate
    from sklearn.model_selection import cross_val_score
    aucs = cross_val_score(attack_clf, X, y, cv=5, scoring='roc_auc')

    return {
        "attack_auc_mean": aucs.mean(),
        "attack_auc_std": aucs.std(),
        "acceptable": aucs.mean() < 0.60,
        "n_members_tested": len(member_losses),
        "n_nonmembers_tested": len(nonmember_losses),
    }
```

### Step 2: Likelihood Ratio Test (for generative models)

For generative models (VAEs, diffusion models), use the likelihood ratio:

```python
def likelihood_ratio_attack(model, x, n_samples=100):
    """Per Carlini et al. (2022) — 'Membership Inference Attacks From First Principles'"""
    # Score under target model
    log_p_target = model.log_prob(x)
    # Score under reference model (same architecture, different data)
    log_p_ref = reference_model.log_prob(x)
    return log_p_target - log_p_ref
```

### Step 3: Differential Privacy Check

If the model was trained with differential privacy (ε, δ):
- ε ≤ 1.0: strong protection — member-inference evaluation still recommended
- ε = 3-10: moderate protection — evaluation required
- ε > 10 or no DP: full evaluation required

### Reporting Template

```markdown
## Member-Inference Evaluation Report

**Model**: [name/version]
**Training data**: [DUC name / cohort]
**Evaluation date**: [date]
**Evaluator**: [name]

### Results
| Test | Attack AUC | Threshold | Pass/Fail |
|---|---|---|---|
| Shadow-model (loss) | 0.52 | <0.60 | ✅ Pass |
| Likelihood ratio | 0.55 | <0.60 | ✅ Pass |

### Conclusion
[Pass: safe to release / Fail: requires additional mitigation]

### Mitigations if Failed
- Apply output perturbation (add Gaussian noise to model outputs)
- Fine-tune with differential privacy (ε ≤ 3, δ = 1e-5)
- Restrict API access (no raw logits — only top-k predictions)
- Do not release this model — release only aggregate statistics

### Sign-off
Privacy Officer: [signature]
```

## References
- Shokri et al. (2017). Membership Inference Attacks Against Machine Learning Models. IEEE S&P.
- Carlini et al. (2022). Membership Inference Attacks From First Principles. IEEE S&P.
- Dwork & Roth (2014). The Algorithmic Foundations of Differential Privacy.
- NIH GDS Policy 2025 §6.4 — Privacy-preserving model requirements.
