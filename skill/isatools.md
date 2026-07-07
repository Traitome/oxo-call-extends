---
name: isatools
category: metadata
description: Metadata tracking tools for life science experimental metadata management
tags: [isatools, metadata, ISA-Tab, ISA-JSON, bioinformatics]
author: oxo-call-community
source_url: "https://isa-tools.org/"
---

## Concepts

- **Tool Overview**: isatools (v0.14.3) - Open-source metadata tracking tools for managing life science, environmental, and biomedical experiments
- **ISA Format**: Built around Investigation-Study-Assay (ISA) tabular format for standardized experimental metadata description
- **Core Components**: ISA-Tab (tabular format), ISA-JSON (JSON format), validation tools, and conversion utilities
- **Metadata Standards**: Enforces community-driven standards for reproducibility and data reuse across scientific disciplines
- **Interoperability**: Supports conversion between ISA formats and integration with other bioinformatics tools and databases
- **Validation Framework**: Provides reference implementations for validating ISA documents against official specifications

## Pitfalls

- **Format Strictness**: Requires strict adherence to ISA specifications; minor formatting errors cause validation failures
- **Configuration Dependencies**: ISA-Tab validation requires XML configuration files for assay types
- **Version Compatibility**: Different ISA format versions have different validation rules and schemas
- **Large Files**: Performance may degrade with very large ISA documents or batch processing scenarios
- **Error Interpretation**: JSON validation reports can be complex and require careful interpretation
- **Python Version**: Requires Python 3.9+; older Python versions not supported

## Examples

### Create ISA-Tab investigation
**Args:** `isatools create -i investigation.txt -s study.txt -a assay.txt`
**Explanation:** Creates a basic ISA-Tab structure with investigation, study, and assay files.

### Validate ISA-Tab directory
**Args:** `isatools validate-tab ./isa_study/ --config ./isaconfig/`
**Explanation:** Validates ISA-Tab files in specified directory against provided configuration.

### Convert ISA-Tab to JSON
**Args:** `isatools convert --input ./tab_study/ --output experiment.json --format json`
**Explanation:** Converts ISA-Tab format to ISA-JSON format for web-based applications.

### Validate ISA-JSON file
**Args:** `isatools validate-json experiment.json`
**Explanation:** Validates a single ISA-JSON file against the ISA JSON version 1.0 specification.

### Batch validation
**Args:** `isatools batch-validate --input-list studies.txt --output report.json`
**Explanation:** Validates multiple ISA documents listed in studies.txt and generates combined validation report.

### Generate sample assay plan
**Args:** `isatools generate-sap --template template.yaml --output sap.json`
**Explanation:** Generates a Sample and Assay Plan (SAP) from a template configuration.