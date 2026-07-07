---
name: hifiadapterfilt
category: bioinformatics
description: hifiadapterfilt removes remnant PacBio HiFi adapter sequences from sequencing reads.
tags: [hifiadapterfilt, PacBio, HiFi, adapter-trimming, bioinformatics]
author: oxo-call-community
source_url: "https://bio.tools/hifiadapterfilt"
---

## Concepts

- **Adapter Trimming**: hifiadapterfilt removes adapter sequences.

- **PacBio HiFi**: Specifically designed for PacBio HiFi data.

- **BAM to FASTQ**: Converts BAM to FASTQ format.

- **Quality Control**: Improves data quality by removing adapters.

- **Read Filtering**: Filters reads with adapter remnants.

- **Long Reads**: Optimized for long read sequencing data.

## Pitfalls

- **Data Quality**: Results depend on input data quality.

- **Adapter Sequences**: Requires known adapter sequences.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Memory Usage**: Large datasets may require significant memory.

- **False Positives**: May incorrectly remove valid sequences.

## Examples

### Filter adapters from BAM
**Args:** `hifiadapterfilt --input input.bam --output filtered.fastq`
**Explanation:** Removes adapters and converts BAM to FASTQ.

### With custom adapters
**Args:** `hifiadapterfilt --input input.bam --adapters adapters.fa --output filtered.fastq`
**Explanation:** Uses custom adapter sequences.

### Batch processing
**Args:** `for f in *.bam; do hifiadapterfilt --input $f --output ${f%.bam}_filtered.fastq; done`
**Explanation:** Processes multiple BAM files.

### Quality filtering
**Args:** `hifiadapterfilt --input input.bam --quality 20 --output filtered.fastq`
**Explanation:** Filters by quality score.

### Help command
**Args:** `hifiadapterfilt --help`
**Explanation:** Shows available options and usage information.