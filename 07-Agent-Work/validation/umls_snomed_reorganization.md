# UMLS/SNOMED Data Reorganization & Coverage Audit

> **Date**: 2026-05-12 | **Final KG**: 5,813,739 nodes × 48,653,892 edges

## 1. Source Coverage Audit

### UMLS Metathesaurus: 100% Parsed

All 52 META RRF files → Parquet. The only "missing" file `MRHIST` has 0 bytes (empty).

| Table | Purpose | Parsed? | Used in KG? |
|-------|---------|:-------:|:-----------:|
| MRCONSO | Concepts + atoms | ✅ | ✅ nodes + CUI links |
| MRREL | Relationships | ✅ | ✅ broader/narrower |
| MRSTY | CUI→TUI assignments | ✅ | ✅ semantic type edges |
| MRDEF | Definitions | ✅ | ✅ node descriptions |
| MRSAT | Attributes (105M rows) | ✅ | ⚡ future |
| MRRANK | Term ranking | ✅ | ✅ preferred labels |
| MRSAB | Vocabulary metadata | ✅ | ✅ source versions |
| MRDOC | Property docs | ✅ | ⚡ reference |
| MRHIER | Hierarchical paths | ✅ | ⚡ future traversal |
| **MRMAP** | **Cross-vocab mappings** | ✅ | ✅ **761K edges (NEW)** |
| MRSMAP | Simple mappings | ✅ | ⚡ via MRMAP |
| MRCUI | CUI history | ✅ | ⚡ deprecation tracking |
| MRAUI | AUI history | ✅ | ⚡ reference |
| SRDEF | Semantic type defs | ✅ | ✅ SN nodes |
| SRSTRE1 | SN hierarchy | ✅ | ✅ SN edges |
| SRSTR | SN relations (readable) | ✅ | ⚡ reference |
| SRSTRE2 | SN relations (expanded) | ✅ | ⚡ reference |
| SU | SN abbreviations | ✅ | ⚡ reference |
| MRXx_* | Word indexes (30 langs) | ✅ | ⚡ search index |
| MRHIST | Concept history | ✅ | empty |

### MRMAP Cross-Vocabulary Mappings (NEW)

| Mapping Set | Count |
|------------|------:|
| SNOMEDCT_US → ICD/SDUI | 314,179 |
| CCSR → ICD-10-CM | 237,140 |
| CCSR → ICD-10-PCS | 79,115 |
| MEDCIN → MEDCIN | 77,727 |
| CCS → CCS | 23,440 |
| LCH_NW → NLM | 13,416 |
| ICPC2 → ICD-10 | 8,486 |
| MTH → Boolean | 8,307 |
| **Total** | **761,810** |

### SNOMED CT: 100% Parsed (both editions)

| Edition | Snapshot Parquets | Full Parquets | SSSOM | Total |
|---------|:-------:|:-------:|:-------:|:-------:|
| International 20260501 | 23 | 23 | 4 | 50 |
| US 20260301 | 23 | 23 | 4 | 50 |

### UMLS Full Release (2026AA-full)

The `2026aa-otherks.nlm` archive contains the Semantic Network (NET/) and Lexicon (LEX/) — we already have the SN from the standalone 2023AA release. The META files are identical to the metathesaurus-full download. No additional unpacking needed.

## 2. Data Reorganization

### Before (scattered)
```
neuro-pheno/data/UMLS/           ← 52 parquets (no version structure)
neuro-pheno/data/SnomedCT/International/ ← 46 parquets (flat)
neuro-pheno/data/SnomedCT/US/    ← 46 parquets + 4 SSSOM
```

### After (organized)
```
datasets/latest/
├── UMLS/
│   ├── umls-2026AA-full/                          (compressed archives)
│   ├── umls-2026AA-metathesaurus-full/2026AA/META/ (raw RRF files)
│   └── parquet/2026AA/                            (56 parquets + sidecars)
│       ├── *.parquet + *.provenance.yaml           (56 + 56 files)
│       ├── sssom/                                  (UMLS cross-mappings)
│       ├── owl/                                    (OWL exports)
│       ├── SemanticNetwork/                        (derived SN)
│       └── CHANGE/                                 (CUI change logs)
└── SnomedCT/
    ├── SnomedCT_InternationalRF2_PRODUCTION_20260501T120000Z/ (raw RF2)
    ├── SnomedCT_ManagedServiceUS_PRODUCTION_US1000124_20260301T120000Z/ (raw RF2)
    └── parquet/
        ├── International_20260501/  (46 parquets + 4 SSSOM)
        └── US_20260301/             (46 parquets + 4 SSSOM)
```

**Version adaptation**: For 2027AA, create `parquet/2027AA/`, run the RRF→Parquet conversion, update `manifest.yaml` version field.

## 3. Edge Growth Summary

| Edge Source | Before | After | Delta |
|-------------|------:|------:|------:|
| Ontology hierarchy | 2,198,193 | 2,198,193 | — |
| UMLS CUI links | 4,331,289 | 4,331,289 | — |
| UMLS broader/narrower | 37,479,456 | 37,479,456 | — |
| Semantic Network | 6,217 | 6,217 | — |
| CUI→TUI | 3,876,927 | 3,876,927 | — |
| **MRMAP cross-vocab** | — | **761,810** | **+761K** |
| SNOMED | 0 | 0 | — |
| **Total** | 47,892,082 | **48,653,892** | **+761,810** |
