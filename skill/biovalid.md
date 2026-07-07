---
name: biovalid
category: qc
description: Quick validation of common bioinformatics files in pure Python
tags: [validation, quality-control, file-formats, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/biovalid"
---

## Concepts

- **Tool Overview**: BioValid is a fast validation tool for common bioinformatics file formats, implemented in pure Python for portability.
- **Format Support**: Validates FASTA, FASTQ, VCF, BED, SAM, BAM, and other common formats.
- **Validation Rules**: Checks file structure, field formats, and data consistency.
- **Batch Processing**: Can validate multiple files in a single run.
- **Error Reporting**: Clear error messages indicating validation failures.

## Pitfalls

- **Format Strictness**: Some validators may be stricter than others; check error messages.
- **Large Files**: Very large files may take time to validate completely.

## Examples

### Validate FASTQ file
**Args:** `biovalid validate -i reads.fastq -f fastq`
**Explanation:** Validates FASTQ file format.

### Validate VCF file
**Args:** `biovalid validate -i variants.vcf -f vcf`
**Explanation:** Validates VCF file format.

### Batch validate
**Args:** `biovalid validate -i *.fastq -f fastq`
**Explanation:** Validates all FASTQ files in directory.