---
name: submission-tool-validator
category: utility
description: This tool helps users validate submissions in the client side before submitting to PRIDE.
tags: [submission-tool-validator, pride, validation, proteomics]
author: oxo-call-community
source_url: "https://github.com/bigbio/submission-tool-validator"
---

## Concepts

- **Tool Overview**: submission-tool-validator (v1.0.7) is a tool for validating PRIDE submissions before upload.
- **Core Function**: Validates submission files for compliance with PRIDE database requirements.
- **Algorithm**: Checks file formats, metadata completeness, and compliance with PRIDE standards.
- **Input/Output**: Input: Submission files; Output: Validation report with errors and warnings.
- **Applications**: Proteomics data submission, PRIDE database compliance, data validation.
- **Installation**: `conda install -c bioconda submission-tool-validator` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific PRIDE submission format.
- **Metadata Completeness**: Missing metadata causes validation errors.
- **File Size**: Large files may cause memory issues.
- **Network Dependencies**: May require network access for validation rules.
- **Version Compatibility**: Validation rules may change between versions.
- **Interpretation**: Requires understanding of PRIDE submission guidelines.

## Examples

### Display help
**Args:** `submission-tool-validator --help`
**Explanation:** Shows available options and usage information.

### Basic validation
**Args:** `submission-tool-validator -i submission/ -o report.txt`
**Explanation:** Validate submission files in directory.

### With strict mode
**Args:** `submission-tool-validator -i submission/ -o report.txt --strict`
**Explanation:** Run validation in strict mode.

### Verbose mode
**Args:** `submission-tool-validator -i submission/ -o report.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output JSON
**Args:** `submission-tool-validator -i submission/ -o report.json --json`
**Explanation:** Output validation report in JSON format.

### Batch processing
**Args:** `submission-tool-validator -i submissions/ -o reports/`
**Explanation:** Validate multiple submission directories together.

### Check only
**Args:** `submission-tool-validator -i submission/ --check`
**Explanation:** Check submission without generating report.

### Include warnings
**Args:** `submission-tool-validator -i submission/ -o report.txt --warnings`
**Explanation:** Include warnings in validation report.

### Generate report
**Args:** `submission-tool-validator -i submission/ -o report.txt --html-report`
**Explanation:** Generate comprehensive HTML report.
