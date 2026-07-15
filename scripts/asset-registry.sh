#!/usr/bin/env bash
# Regenerate the Master Asset Registry. cytomem is the live index; this is the human map.
# Usage: bash scripts/asset-registry.sh > 06-Operations/inventory/MASTER-ASSET-REGISTRY_$(date +%F).md
set -uo pipefail
D=~/repos/cytognosis/docs
echo "# Master Asset Registry — where everything lives"
echo; echo "> Generated $(date +%F). cytomem = queryable system of record; this = human map."
echo; echo "## Claude projects + _context slices"
for d in ~/Claude/Projects/*/; do n=$(basename "$d"); ctx=""
  [ -d "$d/_context" ] && for l in "$d/_context"/*; do [ -L "$l" ] && ctx="$ctx $(basename "$l")"; done
  echo "- $n:${ctx:- (none)}"; done
echo; echo "## Repos (branch | dirty | last commit)"
for r in ~/repos/cytognosis/*/; do [ -d "$r/.git" ] || continue
  echo "- $(basename "$r"): $(git -C "$r" branch --show-current 2>/dev/null) | dirty $(git -C "$r" status --porcelain 2>/dev/null|wc -l) | $(git -C "$r" log -1 --format='%h %s' 2>/dev/null|cut -c1-48)"; done
echo; echo "## Datasets"; du -sh ~/datasets/cytognosis/*/ 2>/dev/null
echo; echo "## Drive top-level"; ls -d "/home/mohammadi/.mnt/cytognosis-gdrive/Cytognosis Foundation"/*/ 2>/dev/null | xargs -n1 basename 2>/dev/null
