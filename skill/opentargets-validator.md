---
name: opentargets-validator
category: utility
description: OpenTargets Validator validates evidence data for the Open Targets platform.
tags: [opentargets-validator, utility, data-validation, drug-discovery]
author: oxo-call-community
source_url: "https://github.com/opentargets/validator"
---

## Concepts

- **Tool Overview**: Validator checks evidence data for Open Targets.
- **Core Function**: Validates data format and content.
- **Algorithm**: Uses JSON schema validation and custom checks.
- **Input Format**: Accepts JSON/YAML evidence files.
- **Output**: Produces validation reports and errors.
- **Use Case**: Data quality control, evidence submission, and pipeline validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Schema Changes**: Validation rules may change.
- **Data Quality**: Poor data may fail validation.
- **Memory Usage**: Large files require memory.
- **Error Messages**: May be cryptic.
- **Validation**: Results should be validated manually.

## Examples

### Display help
**Args:** `validator --help`
**Explanation:** Shows available options and usage instructions.

### Validate file
**Args:** `validator validate -i evidence.json -o report.json`
**Explanation:** Validates evidence JSON file.

### With schema
**Args:** `validator validate -i evidence.json -s schema.json -o report.json`
**Explanation:** Uses custom schema for validation.

### Check format
**Args:** `validator format -i evidence.json`
**Explanation:** Checks file format.

### Batch validation
**Args:** `validator batch -d evidences/ -o reports/`
**Explanation:** Validates multiple files.

### Verbose mode
**Args:** `validator validate -i evidence.json -v -o report.json`
**Explanation:** Runs with verbose output.

### Generate schema
**Args:** `validator schema -o schema.json`
**Explanation:** Generates validation schema.