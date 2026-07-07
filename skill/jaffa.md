---
name: jaffa
category: expression
description: JAFFA is a multi-step pipeline that takes either raw RNA-Seq reads, or pre-assembled transcripts then searches for gene fusions.
tags: [jaffa, expression, gene-fusion, RNA-seq, cancer]
author: oxo-call-community
source_url: "https://github.com/Oshlack/JAFFA"
---

## Concepts

- **Tool Overview**: jaffa (v2.5) - A comprehensive pipeline for detecting gene fusions from RNA-Seq data using multiple complementary approaches.
- **Detection Methods**: Implements three detection strategies: direct alignment, assembly-based, and hybrid approaches.
- **jaffa-direct**: Aligns reads directly to a reference transcriptome to identify fusion candidates.
- **jaffa-assembly**: Assembles reads into transcripts and then searches for fusion events.
- **jaffa-hybrid**: Combines direct alignment and assembly approaches for improved sensitivity.
- **Fusion Validation**: Integrates multiple lines of evidence to validate fusion calls.

## Pitfalls

- **False Positives**: High levels of false positives require careful filtering and validation.
- **Transcriptome Bias**: Performance depends on the completeness of the reference transcriptome.
- **Low Expression**: Fusions with low expression levels may be missed.
- **Complex Rearrangements**: Complex genomic rearrangements can confound detection.
- **Computational Resources**: Assembly-based approach requires significant memory and processing time.
- **Chimeric Reads**: Technical artifacts can produce false fusion signals.

## Examples

### Run jaffa-direct
**Args:** `jaffa-direct --reads R1.fastq R2.fastq --output results/`
**Explanation:** Uses direct alignment approach for rapid fusion detection.

### Run jaffa-assembly
**Args:** `jaffa-assembly --reads R1.fastq R2.fastq --output results/`
**Explanation:** Uses de novo assembly approach for higher sensitivity.

### Run jaffa-hybrid
**Args:** `jaffa-hybrid --reads R1.fastq R2.fastq --output results/`
**Explanation:** Combines direct and assembly approaches for optimal performance.

### Specify reference
**Args:** `jaffa-direct --reads R1.fastq R2.fastq --ref ref.fa --output results/`
**Explanation:** Uses custom reference genome for alignment.

### Filter by quality
**Args:** `jaffa-direct --reads R1.fastq R2.fastq --output results/ --min-quality 20`
**Explanation:** Filters calls based on minimum quality score.

### Set minimum coverage
**Args:** `jaffa-assembly --reads R1.fastq R2.fastq --output results/ --min-cov 10`
**Explanation:** Requires minimum coverage of 10x for fusion calls.