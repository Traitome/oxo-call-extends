---
name: jacusa2
category: variant-calling
description: JACUSA2 is a framework for accurate variant assessment, detecting SNVs and arrest events in NGS data.
tags: [jacusa2, variant-calling, SNV, RNA-seq, arrest-events]
author: oxo-call-community
source_url: "https://github.com/dieterich-lab/JACUSA2"
---

## Concepts

- **Tool Overview**: JACUSA2 (v2.1.16) - A powerful variant calling framework that detects SNVs and arrest events (transcriptional pausing sites) from NGS data with high accuracy.
- **Multi-sample Analysis**: Supports simultaneous analysis of multiple sequencing samples.
- **Arrest Event Detection**: Identifies positions where RNA polymerase pauses during transcription.
- **Strand-specific Calling**: Distinguishes variants on forward and reverse strands.
- **Quality-based Filtering**: Filters calls based on base quality, mapping quality, and strand bias.
- **Statistical Significance**: Uses statistical models to assess confidence in variant calls.

## Pitfalls

- **Alignment Artifacts**: Poorly aligned reads can produce false-positive calls.
- **PCR Bias**: Uneven amplification can skew allele frequencies.
- **Strand Bias**: Significant strand imbalance may indicate technical artifacts.
- **Low Coverage**: Insufficient coverage reduces calling confidence.
- **Indel Handling**: Complex indels may be miscalled or require additional filtering.
- **Reference Genome Quality**: Errors in reference sequences propagate to variant calls.

## Examples

### Basic variant calling
**Args:** `JACUSA2 call -b input.bam -o variants.txt`
**Explanation:** Calls variants from aligned BAM file and outputs to text file.

### Detect arrest events
**Args:** `JACUSA2 detect -b input.bam -o arrest_events.txt`
**Explanation:** Identifies transcription arrest events from RNA-seq data.

### Multi-sample comparison
**Args:** `JACUSA2 call -b sample1.bam sample2.bam -o comparison.txt`
**Explanation:** Calls variants from multiple samples and compares them.

### Strand-specific analysis
**Args:** `JACUSA2 call -b input.bam -o variants.txt --strand-specific`
**Explanation:** Performs strand-specific variant calling.

### Set quality thresholds
**Args:** `JACUSA2 call -b input.bam -o variants.txt -q 30 -Q 30`
**Explanation:** Sets minimum base quality (30) and mapping quality (30) thresholds.

### Filter by coverage
**Args:** `JACUSA2 call -b input.bam -o variants.txt --min-cov 10 --max-cov 1000`
**Explanation:** Filters positions with coverage between 10x and 1000x.