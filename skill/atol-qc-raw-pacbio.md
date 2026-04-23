---
name: atol-qc-raw-pacbio
category: qc
description: AToL QC Raw PacBio - Run QC and produce summary stats on PacBio HiFi reads
tags: [pacbio, hifi, long-reads, quality-control]
author: oxo-call-community
source_url: "https://github.com/amytims/atol-qc-raw-pacbio"
---

## Concepts

- **Tool Overview**: Quality control and statistics generation for PacBio HiFi (High Fidelity) long reads in AToL Genome Engine pipeline.

- **HiFi-Specific Metrics**: Calculates metrics specific to PacBio HiFi technology including circular consensus sequencing (CCS) quality.

- **Read Statistics**: Provides comprehensive read length, quality, and yield statistics.

- **Filtering Support**: Filters reads based on quality and length criteria suitable for downstream assembly.

## Pitfalls

- **CCS Mode**: Results depend on CCS mode used during sequencing. Document CCS parameters.

- **Movie Time**: Longer movie times generate more data but may have declining quality over time.

- **Polymerase Reads vs Subreads**: Ensure correct interpretation of polymerase reads vs subreads in statistics.

## Examples

### Basic QC statistics
**Args:** `atol-qc-raw-pacbio --input reads.bam --output stats.tsv`
**Explanation:** Generates summary statistics from PacBio HiFi BAM file.

### Filter HiFi reads
**Args:** `atol-qc-raw-pacbio --input reads.bam --min-quality 20 --min-length 10000 --output filtered.bam`
**Explanation:** Filters HiFi reads for quality ≥Q20 and length ≥10kb.

### Generate visual report
**Args:** `atol-qc-raw-pacbio --input reads.bam --report report.html --output results/`
**Explanation:** Creates HTML report with read length and quality visualizations.

### Extract subreads
**Args:** `atol-qc-raw-pacbio --input reads.bam --extract-subreads --output subreads.fastq`
**Explanation:** Extracts subreads from polymerase reads for analysis.
