# Workspace AI Features Setup

This document covers the required steps to enable Gemini Enterprise or Business AI features (such as "Take notes for me" in Google Meet, or live translated captions) for the Cytognosis Foundation Google Workspace.

**Status**: 🔵 Active · **Owner**: `mohammadi@cytognosis.org`

## 1. Verify Licensing

Google One AI Premium (which includes Gemini Advanced) applies *only* to personal `@gmail.com` accounts.

For Google Workspace accounts (`@cytognosis.org`), the organization must have the **Gemini for Google Workspace** add-on (either Gemini Business or Gemini Enterprise). 

To assign the license:
1. Go to the [Google Workspace Admin Console](https://admin.google.com).
2. Navigate to **Directory > Users**.
3. Select `mohammadi@cytognosis.org`.
4. Scroll down to **Licenses**.
5. Assign the **Gemini Enterprise** (or Business) license.

## 2. Enable Generative AI Features

The features must be explicitly enabled for the Organizational Unit (OU):
1. In the Admin Console, go to **Generative AI > Settings**.
2. Select the top-level OU or the specific OU for `mohammadi@cytognosis.org`.
3. Check the box to **Allow users to access Gemini features**.
4. Specifically for Google Meet, ensure that **Meet generative AI features** ("Take notes for me", "Translate for me") are set to **ON**.

## 3. Usage in Google Meet

Once enabled:
1. Start or join a Google Meet.
2. At the top right, click the **✨ (Gemini icon)**.
3. Select **Take notes for me**.
4. The notes will be automatically saved to your Google Drive and attached to the calendar event.

*Note: Changes in the Admin Console can take up to 24 hours to propagate across all services.*
