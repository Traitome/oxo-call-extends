---
name: grz-check
category: bioinformatics
description: grz-check validates incoming files for Modellvorhaben §64e submissions to German Genomrechenzentren (GRZ).
tags: [grz-check, validation, german, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BfArM-MVH/grz-tools"
---

## Concepts

- **File Validation**: grz-check validates files according to GRZ submission requirements.

- **Format Checking**: Checks file formats and naming conventions.

- **Metadata Validation**: Validates metadata and submission information.

- **Compliance Checking**: Ensures compliance with §64e regulations.

- **Error Reporting**: Provides detailed error reports for invalid submissions.

- **Pre-Submission Testing**: Helps prepare submissions before official submission.

## Pitfalls

- **Regulation Changes**: Stay updated with changes to §64e regulations.

- **File Size**: Large files may require special handling.

- **Format Specificity**: Strict format requirements must be followed.

- **Metadata Completeness**: Ensure all required metadata is provided.

- **Network Issues**: Submission may fail due to network problems.

## Examples

### Validate single file
**Args:** `grz-check -i submission_file.fastq -o report.txt`
**Explanation:** Validates a single submission file.

### Validate directory
**Args:** `grz-check -d submission_dir/ -o report.txt`
**Explanation:** Validates all files in a submission directory.

### Check format compliance
**Args:** `grz-check -i file.fastq -f -o format_report.txt`
**Explanation:** Performs format-specific validation.

### Validate metadata
**Args:** `grz-check -i metadata.xml -m -o metadata_report.txt`
**Explanation:** Validates metadata file according to requirements.

### Generate detailed report
**Args:** `grz-check -i submission_file.fastq -v -o detailed_report.txt`
**Explanation:** Generates verbose validation report.

### Batch validation
**Args:** `grz-check batch -d submissions/ -o reports/`
**Explanation:** Validates multiple submissions in batch mode.

### Check compliance
**Args:** `grz-check -i file.fastq -c -o compliance_report.txt`
**Explanation:** Checks compliance with §64e regulations.