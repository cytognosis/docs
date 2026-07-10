#!/bin/bash
# Antigravity product.json patch - adds missing proposed APIs for GitHub PR extension
# Run after Antigravity updates: sudo bash /usr/local/bin/antigravity-patch-product.sh

set -euo pipefail

PRODUCT_JSON="/usr/share/antigravity/resources/app/product.json"

if [ ! -f "$PRODUCT_JSON" ]; then
    echo "ERROR: product.json not found at $PRODUCT_JSON"
    exit 1
fi

python3 -c "
import json, sys

with open('$PRODUCT_JSON') as f:
    d = json.load(f)

proposals = d.setdefault('extensionEnabledApiProposals', {})

required = [
    'activeComment', 'chatContextProvider', 'chatParticipantAdditions',
    'chatParticipantPrivate', 'chatSessionsProvider', 'codeActionRanges',
    'codiconDecoration', 'commentReactor', 'commentReveal',
    'commentThreadApplicability', 'commentingRangeHint', 'commentsDraftState',
    'contribAccessibilityHelpContent', 'contribCommentEditorActionsMenu',
    'contribCommentPeekContext', 'contribCommentThreadAdditionalMenu',
    'contribCommentsViewThreadMenus', 'contribEditorContentMenu',
    'contribMultiDiffEditorMenus', 'contribShareMenu', 'diffCommand',
    'fileComments', 'languageModelToolResultAudience', 'markdownAlertSyntax',
    'quickDiffProvider', 'remoteCodingAgents', 'shareProvider',
    'tabInputMultiDiff', 'tabInputTextMerge', 'tokenInformation',
    'treeItemMarkdownLabel', 'treeViewMarkdownMessage'
]

current = set(proposals.get('GitHub.vscode-pull-request-github', []))
needed = set(required) - current

if not needed:
    print('Already patched, no changes needed.')
    sys.exit(0)

proposals['GitHub.vscode-pull-request-github'] = required

with open('$PRODUCT_JSON', 'w') as f:
    json.dump(d, f, indent=2)

print(f'Patched: added {len(needed)} missing proposals.')
"
