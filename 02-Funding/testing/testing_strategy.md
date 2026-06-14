# Grant Pipeline — Testing Strategy

**Status:** Proposed
**Last updated:** 2026-05-24

---

## Overview

The grant pipeline currently has **zero test coverage**. This document defines a comprehensive testing strategy across 4 levels: unit, integration, pressure, and validation.

All tests should live under `tests/scholarly/grants/` and use `pytest` with `-v --tb=short`.

---

## 1. Unit Tests

### 1.1 Registry (`test_registry.py`)

```python
# Fixture: load registry from real schemas dir
@pytest.fixture
def registry():
    return GrantTemplateRegistry()

class TestManifestLoading:
    def test_manifest_loads(self, registry):
        """Manifest should load without errors."""
        assert registry._manifest is not None
        assert registry._manifest.get("version") == "1.2"

    def test_manifest_has_expected_funders(self, registry):
        """Manifest should contain all 16+ registered funders."""
        funders = registry.list_funders()
        assert len(funders) >= 16
        funder_ids = {f.id for f in funders}
        assert "nsf_xlabs" in funder_ids
        assert "arpah_solution_summary" in funder_ids

class TestFunderProfiles:
    @pytest.mark.parametrize("funder_id", [
        "nsf_xlabs", "arpah_solution_summary", "nih_r01", "doe_genesis"
    ])
    def test_get_funder_profile(self, registry, funder_id):
        """Each funder profile should load with non-empty required fields."""
        profile = registry.get_funder(funder_id)
        assert profile.name
        assert profile.kind
        assert len(profile.required_slots) > 0

    def test_unknown_funder_raises(self, registry):
        with pytest.raises(KeyError):
            registry.get_funder("nonexistent_funder_xyz")

class TestValidation:
    def test_empty_submission_fails(self, registry):
        errors = registry.validate_submission("nsf_xlabs", {})
        assert len(errors) > 0
        assert all(e.severity == "error" for e in errors if e.rule == "required_slot")

    def test_complete_submission_passes(self, registry):
        profile = registry.get_funder("nsf_xlabs")
        content = {slot: "Content for " + slot for slot in profile.required_slots}
        errors = registry.validate_submission("nsf_xlabs", content)
        # Should only have warnings (useful_slots), not errors
        assert all(e.severity == "warning" for e in errors)
```

### 1.2 Extractor Schema (`test_extractor_schema.py`)

```python
class TestGrantInfoSchema:
    def test_valid_grant_info(self):
        """GrantInfo should validate correct JSON."""
        data = {
            "title": "Test Grant",
            "funder_name": "NSF",
            "deadlines": [{"date": "2026-07-13", "label": "Proposal", "type": "hard"}],
            "eligibility": {"entity_types": ["University"], "exclusions": [], "restrictions": []},
            "funding": {"phases": ["Phase 1"], "cost_share": False},
            "timeline": [],
            "contacts": [],
            "requirements": [],
        }
        info = GrantInfo(**data)
        assert info.title == "Test Grant"

    def test_missing_required_fields(self):
        """GrantInfo should reject missing required fields."""
        with pytest.raises(ValidationError):
            GrantInfo(title="Test")  # Missing funder_name, eligibility, funding

    def test_empty_arrays_accepted(self):
        """GrantInfo should accept empty arrays for optional list fields."""
        data = {
            "title": "Test",
            "funder_name": "NSF",
            "eligibility": {"entity_types": [], "exclusions": [], "restrictions": []},
            "funding": {"phases": []},
        }
        info = GrantInfo(**data)
        assert info.deadlines == []

class TestLLMConfig:
    def test_default_config(self):
        config = LLMConfig()
        assert config.model == "llama3.1"
        assert config.timeout == 600.0
        assert config.provider == "ollama"
```

### 1.3 Parser (`test_parser.py`)

```python
class TestParserOutputFormat:
    def test_parse_produces_markdown(self, tmp_path, sample_pdf):
        parser = GrantDocumentParser(output_dir=tmp_path)
        result = parser.parse(sample_pdf)
        assert result.endswith(".md")
        content = Path(result).read_text()
        assert len(content) > 0

    def test_tables_file_generated(self, tmp_path, sample_pdf_with_tables):
        parser = GrantDocumentParser(output_dir=tmp_path)
        parser.parse(sample_pdf_with_tables)
        tables_file = tmp_path / (sample_pdf_with_tables.stem + "_tables.md")
        assert tables_file.exists()

    def test_metadata_json_generated(self, tmp_path, sample_pdf):
        parser = GrantDocumentParser(output_dir=tmp_path)
        parser.parse(sample_pdf)
        meta_file = tmp_path / (sample_pdf.stem + "_metadata.json")
        assert meta_file.exists()
        meta = json.loads(meta_file.read_text())
        assert "num_pages" in meta

    def test_criticmarkup_annotations(self, tmp_path, sample_pdf_with_highlights):
        parser = GrantDocumentParser(output_dir=tmp_path)
        parser.parse(sample_pdf_with_highlights)
        cm_file = tmp_path / (sample_pdf_with_highlights.stem + "_criticmarkup.md")
        assert cm_file.exists()
        content = cm_file.read_text()
        assert "{==" in content  # CriticMarkup highlight syntax
```

### 1.4 Harmonizer (`test_harmonizer.py`)

```python
class TestHarmonizer:
    def test_harmonize_produces_sections(self, registry):
        harmonizer = GrantDocumentHarmonizer(registry)
        parsed = {"text": "Test grant about biosensors...", "source_file": "test.md"}
        result = harmonizer.harmonize(parsed, "nsf_xlabs")
        assert isinstance(result, HarmonizedGrant)
        assert len(result.sections) > 0

    def test_slot_coverage_tracked(self, registry):
        harmonizer = GrantDocumentHarmonizer(registry)
        parsed = {"text": "Test", "source_file": "test.md"}
        result = harmonizer.harmonize(parsed, "nsf_xlabs")
        assert isinstance(result.slot_coverage, dict)
        assert len(result.slot_coverage) > 0
```

---

## 2. Integration Tests

### 2.1 End-to-End Pipeline (`test_pipeline_e2e.py`)

```python
@pytest.mark.integration
@pytest.mark.slow
class TestEndToEndPipeline:
    def test_pdf_to_json(self, small_test_pdf):
        """Parse a PDF and extract structured JSON."""
        # Stage 1: Parse
        parser = GrantDocumentParser()
        md_path = parser.parse(small_test_pdf)

        # Stage 2: Extract
        extractor = GrantInfoExtractor()
        text = Path(md_path).read_text()
        info = extractor.extract(text)
        assert info.title
        assert info.funder_name

    def test_cross_funder_consistency(self):
        """Same content harmonized for two funders should produce different section orderings."""
        registry = GrantTemplateRegistry()
        harmonizer = GrantDocumentHarmonizer(registry)
        parsed = {"text": "Sample biosensor grant...", "source_file": "test.md"}

        nsf_result = harmonizer.harmonize(parsed, "nsf_xlabs")
        arpah_result = harmonizer.harmonize(parsed, "arpah_solution_summary")

        # Different funders should have different section counts
        assert len(nsf_result.sections) != len(arpah_result.sections)
```

### 2.2 Extraction Regression (`test_extraction_regression.py`)

```python
@pytest.mark.integration
class TestExtractionRegression:
    """Validate known-good extractions against golden files."""

    GOLDEN_DIR = Path("tests/scholarly/grants/golden")

    @pytest.mark.parametrize("filename", [
        "nsf-topic2-fy26-xlabssensingandimaging.json",
    ])
    def test_extraction_matches_golden(self, filename):
        golden = json.loads((self.GOLDEN_DIR / filename).read_text())
        # Re-run extraction and compare key fields
        assert golden["funder_name"]
        assert len(golden.get("deadlines", [])) > 0
```

---

## 3. Pressure Tests

### 3.1 Volume Tests

| Test | Input | Expected |
|---|---|---|
| Parse 100 PDFs sequentially | 100 test PDFs | All complete in <10 minutes |
| Extract 50 documents | 50 staged markdowns | All produce valid JSON |
| Concurrent extraction | 5 parallel extraction threads | No race conditions |

### 3.2 Adversarial Tests

| Test | Input | Expected |
|---|---|---|
| Corrupted PDF | Truncated binary file | Graceful error, no crash |
| Scanned PDF (image-only) | PDF with no text layer | Empty/minimal output, warning logged |
| Huge table | PDF with 200-row table | Table extracted, no OOM |
| Non-English document | French grant announcement | Extraction attempts, may produce partial results |
| Empty file | 0-byte PDF | FileNotFoundError or graceful skip |

### 3.3 LLM Reliability Tests

| Test | Scenario | Expected |
|---|---|---|
| Timeout handling | Set timeout to 1s, extract large doc | TimeoutError caught, logged |
| Retry exhaustion | Mock LLM to always return invalid JSON | RuntimeError after max_retries |
| Model unavailable | Set base_url to unreachable host | ConnectionError caught |
| Schema evolution | Add new field to GrantInfo, re-extract | Old JSONs still loadable |

---

## 4. Schema Validation Tests

### 4.1 Manifest Consistency

```python
class TestSchemaConsistency:
    def test_every_funder_has_yaml(self, schemas_dir):
        manifest = yaml.safe_load((schemas_dir / "manifest.yaml").read_text())
        for funder_id, entry in manifest["funders"].items():
            funder_file = schemas_dir / entry["file"]
            assert funder_file.exists(), f"Missing YAML for {funder_id}: {funder_file}"

    def test_every_slot_has_file(self, schemas_dir):
        manifest = yaml.safe_load((schemas_dir / "manifest.yaml").read_text())
        for family in manifest.get("slot_families", {}).values():
            for slot in family.get("slots", []):
                slot_file = schemas_dir / "slots" / f"{slot['id']}_{slot['name'].lower().replace(' ', '_')}.md"
                # Note: filename format may vary; check by ID prefix
                matching = list((schemas_dir / "slots").glob(f"{slot['id']}_*.md"))
                assert len(matching) == 1, f"Expected 1 file for {slot['id']}, found {len(matching)}"

    def test_funder_required_slots_exist(self, schemas_dir):
        manifest = yaml.safe_load((schemas_dir / "manifest.yaml").read_text())
        all_slot_ids = set()
        for family in manifest.get("slot_families", {}).values():
            for slot in family.get("slots", []):
                all_slot_ids.add(slot["id"])

        for funder_id, entry in manifest["funders"].items():
            funder_file = schemas_dir / entry["file"]
            if funder_file.exists():
                funder_data = yaml.safe_load(funder_file.read_text())
                for slot_id in funder_data.get("required_slots", []):
                    assert slot_id in all_slot_ids, f"{funder_id} requires unknown slot {slot_id}"
```

---

## 5. Test Data & Fixtures

### Required Test Fixtures

| Fixture | Description | Location |
|---|---|---|
| `sample_pdf` | Small 2-page PDF with text and metadata | `tests/scholarly/grants/fixtures/sample.pdf` |
| `sample_pdf_with_tables` | PDF containing markdown-extractable tables | `tests/scholarly/grants/fixtures/sample_tables.pdf` |
| `sample_pdf_with_highlights` | PDF with highlight annotations | `tests/scholarly/grants/fixtures/sample_highlights.pdf` |
| `golden_extraction` | Known-good JSON extraction output | `tests/scholarly/grants/golden/*.json` |
| `schemas_dir` | Points to real `src/.../schemas/` directory | `conftest.py` fixture |
| `registry` | Loaded `GrantTemplateRegistry` instance | `conftest.py` fixture |

### Nox Session

```python
@nox.session(name="test_grants", python=PYTHON)
def test_grants(session: nox.Session) -> None:
    """Run all grant pipeline tests."""
    session.run(
        "uv", "run", "pytest",
        "tests/scholarly/grants/",
        "-v", "--tb=short",
        "-m", "not slow",
        external=True,
    )

@nox.session(name="test_grants_full", python=PYTHON)
def test_grants_full(session: nox.Session) -> None:
    """Run all grant pipeline tests including slow integration tests."""
    session.run(
        "uv", "run", "pytest",
        "tests/scholarly/grants/",
        "-v", "--tb=short",
        external=True,
    )
```

---

## 6. CI/CD Integration

- Run `nox -s test_grants` on every PR touching `src/cytos/scholarly/grants/`
- Run `nox -s test_grants_full` nightly
- Run `nox -s validate_schemas` on every PR touching `schemas/`
- Fail CI if any schema consistency check fails
