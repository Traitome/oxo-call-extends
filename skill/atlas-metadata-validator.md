---
name: atlas-metadata-validator
category: utility
description: Atlas Metadata Validator - MAGE-TAB validator for Expression Atlas and Single Cell Expression Atlas
tags: [metadata-validation, mage-tab, expression-atlas, single-cell]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/atlas-metadata-validator"
---

## Concepts

- **Tool Overview**: Validates MAGE-TAB format metadata files for compatibility with Expression Atlas and Single Cell Expression Atlas analysis pipelines.

- **MAGE-TAB Standard**: Validates against MAGE-TAB (MicroArray Gene Expression Tabular) format specifications used by ArrayExpress and Expression Atlas.

- **Experiment Type Detection**: Automatically detects experiment type (bulk or single-cell) and applies appropriate validation rules.

- **Pipeline Compatibility**: Ensures metadata meets requirements for downstream analysis pipelines, preventing processing failures.

## Pitfalls

- **Format Strictness**: MAGE-TAB format has strict requirements. Minor formatting errors can cause validation failures.

- **Ontology Terms**: Requires proper ontology term identifiers for experimental factors and sample attributes.

- **File References**: All referenced files must exist and be accessible at specified paths.

- **Protocol Descriptions**: Incomplete or missing protocol descriptions will trigger validation errors.

## Examples

### Basic validation
**Args:** `atlas-metadata-validator experiment.txt`
**Explanation:** Validates MAGE-TAB experiment file and reports any errors or warnings.

### Validate with detailed output
**Args:** `atlas-metadata-validator --verbose experiment.txt`
**Explanation:** Provides detailed validation output including all checks performed and their results.

### Single-cell experiment validation
**Args:** `atlas-metadata-validator --experiment-type single-cell experiment.txt`
**Explanation:** Validates metadata specifically for single-cell experiment requirements.

### Output validation report
**Args:** `atlas-metadata-validator --output report.json experiment.txt`
**Explanation:** Saves validation results in JSON format for programmatic processing.

### Check specific sections
**Args:** `atlas-metadata-validator --sections IDF,SDRF experiment.txt`
**Explanation:** Validates only specified MAGE-TAB sections (Investigation Description Format, Sample and Data Relationship Format).
