# SOP: Confidential Compute Rollout Plan
**Control**: NIH GDS 2025 §4 — Hardware-level isolation for Tier 4 ML workloads
**Effective**: 2026-05-19 (planned) | **Status**: DEFERRED — see deferred-controls.md
**Owner**: Engineering | **Trigger**: First PHI ML training workload

## What Confidential Computing Provides

AMD SEV-SNP (Secure Encrypted Virtualization — Secure Nested Paging) encrypts VM
memory in hardware. Even a GCP hypervisor operator cannot read the memory of a
Confidential VM. This provides the strongest isolation for Tier 4 data processing.

**Use cases requiring this**:
- Fine-tuning a model on raw WGS or clinical phenotypes from a DUC cohort
- Running inference pipelines where raw ePHI is loaded into GPU memory
- Any Vertex AI custom training job on Tier 4 data

## GCP Confidential VM Options

| Option | Use case | Attestation | Cost premium |
|---|---|---|---|
| Confidential VM (AMD SEV) | Standard training jobs | Basic | +10% |
| Confidential VM (AMD SEV-SNP) | Sensitive PHI workloads | Full attestation | +10-15% |
| Confidential Space | Multi-party compute | Workload attestation | Custom |

## Rollout Phases

### Phase 1: Pilot (trigger: first DUC data arrives)
1. Create one Confidential VM instance for batch analysis
2. Verify application runs correctly under SEV-SNP
3. Test attestation report generation

```bash
# Create a Confidential VM instance
gcloud compute instances create phi-analysis-pilot \
  --zone=us-central1-b \
  --machine-type=n2d-standard-4 \   # AMD processor required for SEV
  --image-family=debian-12 \
  --image-project=debian-cloud \
  --confidential-compute \
  --on-host-maintenance=TERMINATE \  # Required for Confidential VMs
  --maintenance-policy=TERMINATE \
  --shielded-secure-boot \
  --shielded-vtpm \
  --shielded-integrity-monitoring \
  --no-address \                     # No external IP — IAP access only
  --project=cytognosis-infrastructure
```

### Phase 2: Vertex AI Integration (trigger: ML pipeline on PHI)

```python
# Use Confidential computing in Vertex AI custom training
from google.cloud import aiplatform

job = aiplatform.CustomJob(
    display_name="phi-training-confidential",
    worker_pool_specs=[{
        "machine_spec": {
            "machine_type": "n2d-standard-8",
            "confidential_compute_type": "SEV_SNP",
        },
        "replica_count": 1,
        "container_spec": {
            "image_uri": "us-central1-docker.pkg.dev/cytognosis-phi-prod/phi-services/training:latest",
        },
    }],
)
job.run()
```

### Phase 3: Full PHI Pipeline (trigger: production DUC analysis)
- All Tier 4 analysis jobs run on Confidential VMs
- Attestation reports stored alongside analysis results
- VPC-SC perimeter enforced around all Confidential VM instances

## Attestation

AMD SEV-SNP provides cryptographic attestation that the workload is running
on genuine AMD hardware with correct firmware. Store attestation reports:

```bash
# Get attestation report from within a Confidential VM
gcloud compute instances get-shielded-identity phi-analysis-pilot \
  --zone=us-central1-b --project=cytognosis-infrastructure
```

## References
- Google Cloud Confidential VM documentation
- NIH GDS Policy 2025 §4.3 — Trusted Execution Environments
- AMD SEV-SNP white paper
