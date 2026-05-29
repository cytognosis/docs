# Evaluation

## A. Current Automated Test Status

- Backend: `84 passed`.
- Mobile: `flutter test` passed for the API client.
- Mobile analyzer: `flutter analyze` reported no issues.
- Demo schema registration: `python scripts/register_demo_schema.py` completed successfully.

## B. Evaluation Dimensions

- Valid JSON routing.
- Schema-aware validation.
- CAP-Lite refusal behavior.
- Annotation transformation correctness.
- Local graph editing.
- Anytype write confirmation.
- Voice turn routing.
- Product status reporting without secret leakage.
- Ollama failure fallback reporting.
- No external dependency in tests.

## C. Suggested Manual Checklist

- Run `pytest`.
- Run `python scripts/register_demo_schema.py`.
- Run capture demo.
- Run annotation demo.
- Run search demo.
- Run local edit/link demo.
- Run Anytype write-plan demo.
- Run mobile voice API demo.
- Run refusal demo.

## D. Known Limitations

- Real central Ollama model `gemma4:e4b` was smoke-tested through `/voice/turn` and returned structured JSON with `used_fallback=false`.
- No real Anytype write tested.
- No browser extension.
- No full LinkML validation.
- Native Flutter app exists; physical-device E2B inference still needs manual validation.

## Reproducibility Notes

The core demo uses FastAPI `TestClient`, SQLite, and the deterministic stub provider. It should run without network access or private credentials.
