# Multimodal Health Data Schema

## Overview

Standardized schema for integrating genomics, proteomics, imaging, clinical, and behavioral health data for AI-driven preventive healthcare research.

## Core Data Types

### 1. Genomic Data

```json
{
  "genomic_profile": {
    "sample_id": "string",
    "sequencing_platform": "illumina|pacbio|nanopore",
    "variants": [
      {
        "chromosome": "string",
        "position": "integer",
        "ref_allele": "string",
        "alt_allele": "string",
        "variant_type": "snv|indel|cnv|sv",
        "clinical_significance": "pathogenic|benign|uncertain",
        "gene_symbol": "string",
        "transcript_id": "string"
      }
    ],
    "polygenic_scores": {
      "cardiovascular_risk": "float",
      "diabetes_risk": "float",
      "cancer_risk": "float"
    }
  }
}
```

### 2. Proteomic Data

```json
{
  "proteomic_profile": {
    "sample_id": "string",
    "assay_type": "mass_spec|immunoassay|proximity_extension",
    "biomarkers": [
      {
        "protein_id": "string",
        "uniprot_id": "string",
        "concentration": "float",
        "units": "ng/ml|pg/ml|relative_units",
        "detection_method": "string",
        "quality_score": "float"
      }
    ],
    "pathway_analysis": {
      "enriched_pathways": ["string"],
      "pathway_scores": {"pathway_name": "float"}
    }
  }
}
```

### 3. Clinical Data (FHIR R4 Compatible)

```json
{
  "clinical_profile": {
    "patient_id": "string",
    "demographics": {
      "age": "integer",
      "sex": "male|female|other",
      "ethnicity": "string",
      "race": "string"
    },
    "vital_signs": [
      {
        "timestamp": "datetime",
        "blood_pressure_systolic": "integer",
        "blood_pressure_diastolic": "integer",
        "heart_rate": "integer",
        "temperature": "float",
        "weight": "float",
        "height": "float"
      }
    ],
    "lab_results": [
      {
        "test_code": "string",
        "test_name": "string",
        "value": "float",
        "units": "string",
        "reference_range": "string",
        "timestamp": "datetime"
      }
    ],
    "medications": [
      {
        "medication_code": "string",
        "medication_name": "string",
        "dosage": "string",
        "frequency": "string",
        "start_date": "date",
        "end_date": "date"
      }
    ]
  }
}
```

### 4. Imaging Data

```json
{
  "imaging_profile": {
    "study_id": "string",
    "modality": "ct|mri|xray|ultrasound|pet|oct",
    "body_part": "string",
    "acquisition_parameters": {
      "resolution": "string",
      "contrast_agent": "boolean",
      "acquisition_date": "datetime"
    },
    "image_features": {
      "radiomics_features": {"feature_name": "float"},
      "ai_annotations": [
        {
          "finding": "string",
          "confidence": "float",
          "bounding_box": [{"x": "float", "y": "float"}]
        }
      ]
    }
  }
}
```

### 5. Behavioral/Lifestyle Data

```json
{
  "behavioral_profile": {
    "patient_id": "string",
    "lifestyle_factors": {
      "smoking_status": "never|former|current",
      "alcohol_consumption": "none|light|moderate|heavy",
      "exercise_frequency": "sedentary|light|moderate|vigorous",
      "diet_pattern": "mediterranean|western|vegetarian|other"
    },
    "social_determinants": {
      "education_level": "string",
      "income_bracket": "string",
      "insurance_status": "string",
      "geographic_region": "string"
    },
    "wearable_data": [
      {
        "device_type": "fitbit|apple_watch|garmin|other",
        "metric": "steps|heart_rate|sleep|activity",
        "value": "float",
        "timestamp": "datetime"
      }
    ]
  }
}
```

## Data Integration Schema

### Unified Patient Record

```json
{
  "patient_record": {
    "patient_id": "string",
    "study_id": "string",
    "fair_metadata": {
      "persistent_identifier": "string (F1)",
      "metadata_registry_url": "string (F4, A1)",
      "ontologies_used": ["string (I2)"],
      "data_usage_license": "string (R1.1)",
      "data_provenance": "string (R1.2)"
    },
    "consent_status": "active|withdrawn|expired",
    "data_collection_date": "datetime",
    "genomic_profile": "object",
    "proteomic_profile": "object",
    "clinical_profile": "object",
    "imaging_profile": "object",
    "behavioral_profile": "object",
    "longitudinal_data": [
      {
        "timepoint": "baseline|6month|1year|2year",
        "data_snapshot": "object"
      }
    ],
    "outcomes": {
      "primary_endpoints": ["string"],
      "secondary_endpoints": ["string"],
      "adverse_events": ["string"]
    }
  }
}
```

## Privacy and Security Schema

### De-identification Metadata

```json
{
  "deidentification_metadata": {
    "method": "safe_harbor|expert_determination|synthetic",
    "k_anonymity": "integer",
    "l_diversity": "integer",
    "privacy_budget": "float",
    "suppressed_fields": ["string"],
    "generalized_fields": {"field_name": "generalization_level"}
  }
}
```

## Quality Control Schema

### Data Quality Metrics

```json
{
  "quality_metrics": {
    "completeness": "float",
    "accuracy": "float",
    "consistency": "float",
    "timeliness": "float",
    "validity": "float",
    "uniqueness": "float",
    "quality_flags": ["missing_data|outlier|inconsistent|duplicate"]
  }
}
```

---

**Schema Version**: 1.1
**Last Updated**: March 2026
**Owner**: Data Architecture Team, Cytognosis Foundation
