# OIDC / Workload Identity Federation

## What It Is

Workload Identity Federation lets GitHub Actions authenticate to GCP **without
long-lived service account keys**. Instead of storing a JSON key file in GitHub
Secrets, Actions exchanges a short-lived GitHub JWT (valid ~10 min) for a
short-lived GCP access token.

```
GitHub → OIDC JWT (signed by GitHub) → GCP verifies → short-lived GCP token
```

## Configuration (as deployed)

| Resource | Value |
|---|---|
| Pool name | `github-pool` |
| Pool resource | `projects/517562623935/locations/global/workloadIdentityPools/github-pool` |
| Provider name | `github-provider` |
| Provider OIDC issuer | `https://token.actions.githubusercontent.com` |
| Project | `cytognosis-infrastructure` |

**Attribute mapping**:
```
google.subject              = assertion.sub
attribute.repository        = assertion.repository
attribute.repository_owner  = assertion.repository_owner
attribute.actor             = assertion.actor
attribute.aud               = assertion.aud
```

**Attribute condition** (access gate):
```
attribute.repository_owner == "cytognosis"
```
This means **only repos under `github.com/cytognosis/`** can use this pool.
Private forks or external orgs cannot, even if they know the pool resource name.

## SA Binding

`website-deployer` is bound to the pool via `attribute.repository_owner`:

```bash
# Current binding (already applied)
gcloud iam service-accounts get-iam-policy \
  website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com \
  --project=cytognosis-infrastructure

# Output: members includes
# principalSet://.../attribute.repository_owner/cytognosis
```

This org-wide binding means **no per-repo setup is needed**. Any new repo
under `github.com/cytognosis/` immediately has access to `website-deployer`.

## Adding a Repo-Specific SA (Advanced)

If a repo needs a different SA with different permissions (e.g., a tighter scope):

```bash
gcloud iam service-accounts add-iam-policy-binding \
  <new-sa>@cytognosis-infrastructure.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/517562623935/locations/global/workloadIdentityPools/github-pool/attribute.repository/cytognosis/<repo-name>"
```

Note the use of `attribute.repository` (single repo) vs `attribute.repository_owner`
(all repos in org). Prefer per-repo bindings for SAs with elevated permissions.

## Troubleshooting

**"Error: google-github-actions/auth failed"**
1. Check `id-token: write` is in workflow `permissions:`
2. Verify `attribute.repository_owner` matches exactly `cytognosis`
3. Run: `gcloud iam workload-identity-pools providers describe github-provider --workload-identity-pool=github-pool --location=global --project=cytognosis-infrastructure`

**"Permission denied" after auth**
The SA's roles are the constraint, not the OIDC binding. Check what the SA
needs vs what it has: `gcloud projects get-iam-policy cytognosis-phi-prod --filter="bindings.members:website-deployer"`
