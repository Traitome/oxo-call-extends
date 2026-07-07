---
name: hifihla
category: bioinformatics
description: hifihla performs HLA star-calling for PacBio HiFi sequencing data.
tags: [hifihla, HLA-typing, PacBio, HiFi, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/hifihla"
---

## Concepts

- **HLA Typing**: hifihla performs HLA allele typing.

- **PacBio HiFi**: Optimized for PacBio HiFi sequencing data.

- **High Resolution**: Provides high-resolution HLA typing.

- **Allele Identification**: Identifies HLA alleles.

- **Immunogenetics**: Analyzes immune system genetics.

- **Genetic Variation**: Studies HLA genetic variation.

## Pitfalls

- **Data Quality**: Results depend on sequencing data quality.

- **Reference Database**: Requires up-to-date HLA reference database.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Ambiguity Resolution**: May have ambiguous allele calls.

## Examples

### Type HLA
**Args:** `hifihla --input reads.fastq --output hla_results.txt`
**Explanation:** Performs HLA typing from HiFi reads.

### With BAM input
**Args:** `hifihla --input aligned.bam --output hla_results.txt`
**Explanation:** Uses aligned BAM file.

### Batch processing
**Args:** `for f in *.fastq; do hifihla --input $f --output ${f%.fastq}_hla.txt; done`
**Explanation:** Processes multiple HiFi datasets.

### Generate report
**Args:** `hifihla --input reads.fastq --output hla_results.txt --report`
**Explanation:** Generates comprehensive HLA typing report.

### Help command
**Args:** `hifihla --help`
**Explanation:** Shows available options and usage information.