---
name: metapointfinder
category: variant-calling
description: MetaPointFinder is a tool for detecting and scoring resistance-associated point mutations directly from long-read and short-read metagenomics sequencing data
tags: [metapointfinder, variant-calling, AMR, metagenomics]
author: oxo-call-community
source_url: "https://github.com/aldertzomer/metapointfinder"
---

## Concepts

- **Tool Overview**: MetaPointFinder v1.01 is a tool for detecting and scoring resistance-associated point mutations directly from metagenomic sequencing data.
- **Core Function**: Identifies and scores antibiotic resistance-associated point mutations in metagenomic samples.
- **AMR Detection**: Uses the AMRFinder database as reference for resistance gene detection.
- **Multi-read Support**: Supports both long-read (PacBio/ONT) and short-read (Illumina) sequencing data.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs detected mutations with resistance scores.
- **Direct Detection**: Detects mutations directly from metagenomic data without prior assembly.

## Pitfalls

- **Database Completeness**: Detection accuracy depends on AMRFinder database completeness.
- **Sequence Quality**: Poor quality sequences may affect mutation detection accuracy.
- **Low Abundance Detection**: May miss mutations present at very low abundance.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **False Positives**: May produce false positive mutation calls.
- **Memory Requirements**: Memory usage can be high for large input datasets.

## Examples

### Detect resistance mutations
**Args:** `metapointfinder -i reads.fastq -o mutations.txt`
**Explanation:** Detects resistance-associated point mutations from metagenomic reads.

### With custom database
**Args:** `metapointfinder -i reads.fastq -d custom_db/ -o mutations.txt`
**Explanation:** Uses a custom AMR database for mutation detection.

### Long-read analysis
**Args:** `metapointfinder -i long_reads.fastq -o mutations.txt -l`
**Explanation:** Optimizes analysis for long-read sequencing data.

### Generate report
**Args:** `metapointfinder -i reads.fastq -o mutations.txt -r report.html`
**Explanation:** Generates an HTML report of detected mutations.

### Batch processing
**Args:** `metapointfinder -i fastq/ -o results/`
**Explanation:** Processes multiple FASTQ files in batch mode.