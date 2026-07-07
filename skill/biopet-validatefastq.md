---
name: biopet-validatefastq
category: qc
description: Validate FASTQ files for format correctness and paired-end consistency
tags: [fastq, validation, quality-control, paired-end]
author: oxo-call-community
source_url: "https://github.com/biopet/validatefastq"
---

## Concepts

- **Tool Overview**: ValidateFastq validates FASTQ files for format correctness, checking for proper formatting, duplicate read names, and valid quality scores.
- **Validation Checks**: Verifies FASTQ format structure, quality score encoding, read name consistency, and paired-end read pair matching.
- **Paired-End Support**: Can validate paired FASTQ files to ensure read pairs match correctly.
- **Error Detection**: Identifies duplicate read names, invalid characters, and format violations.
- **Applications**: FASTQ quality control, pre-processing validation, pipeline input verification.

## Pitfalls

- **Encoding Detection**: Must correctly identify quality encoding (Sanger/Illumina 1.8+ vs older formats).
- **Paired Files**: For paired-end data, both files must be properly synchronized.

## Examples

### Validate single FASTQ
**Args:** `java -jar ValidateFastq.jar -i reads.fq -o validation_report.txt`
**Explanation:** Validates a single FASTQ file.

### Validate paired-end FASTQ
**Args:** `java -jar ValidateFastq.jar -i R1.fq -i2 R2.fq -o validation_report.txt`
**Explanation:** Validates paired-end FASTQ files, checking read pair consistency.

### Check for duplicates
**Args:** `java -jar ValidateFastq.jar -i reads.fq --check-duplicates -o report.txt`
**Explanation:** Validates FASTQ and specifically checks for duplicate read names.