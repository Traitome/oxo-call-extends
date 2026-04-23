---
name: artic
category: variant-calling
description: ARTIC pipeline - Bioinformatics pipeline for viral nanopore sequencing data analysis
tags: [nanopore, virus, amplicon, sars-cov-2, real-time, outbreak]
author: oxo-call-community
source_url: "https://github.com/artic-network/fieldbioinformatics"
---

## Concepts

- **Tool Overview**: ARTIC pipeline is a bioinformatics pipeline for working with virus sequencing data produced using Oxford Nanopore Technologies. Designed for real-time outbreak surveillance. Version 1.10.0.
- **Amplicon-Based**: Optimized for tiled amplicon sequencing schemes (e.g., ARTIC SARS-CoV-2 primers). Handles overlapping amplicons for complete genome coverage.
- **Real-Time Analysis**: Designed for rapid turnaround during outbreaks. Processes data as it arrives from MinION/GridION sequencers.
- **Basecalling Integration**: Works with Guppy basecaller output. Supports both fast and high-accuracy basecalling modes.
- **Consensus Generation**: Produces consensus sequences from amplicon data with proper handling of primer regions and overlaps.
- **Variant Calling**: Identifies variants relative to reference genome. Important for tracking viral evolution during outbreaks.
- **Primer Schemes**: Supports custom primer schemes for different pathogens. ARTIC network provides validated primer sets for emerging pathogens.

## Pitfalls

- **Primer Scheme Matching**: Must use correct primer scheme matching your amplicon design. Mismatched schemes cause failed analysis.
- **Coverage Requirements**: Low coverage (<100x) reduces consensus quality. Ensure adequate sequencing depth for complete genome.
- **Basecaller Version**: Different Guppy versions produce slightly different basecalls. Use consistent version across runs.
- **Amplicon Dropout**: Some amplicons may fail due to primer issues or mutations in primer binding sites. Check coverage per amplicon.
- **Contamination**: Cross-contamination between samples can produce chimeric consensus sequences. Strict lab protocols needed.
- **Reference Genome**: Must use appropriate reference genome for pathogen. Wrong reference produces incorrect variants.

## Examples

### Basic ARTIC pipeline run
**Args:** `artic minion --read-file reads.fastq --scheme-directory /path/to/schemes --scheme-name nCoV-2019/V3 sample_name`
**Explanation:** Standard ARTIC pipeline run for SARS-CoV-2 using V3 primer scheme. Processes reads, trims primers, calls variants, and generates consensus.

### Process basecalled reads
**Args:** `artic guppyplex --min-length 400 --max-length 700 --directory fastq_pass/ --output sample.fastq`
**Explanation:** Aggregates and filters basecalled reads from Guppy output directory. Length filters (400-700bp) appropriate for SARS-CoV-2 amplicons.

### Run with custom primer scheme
**Args:** `artic minion --read-file reads.fastq --scheme-directory /path/to/schemes --scheme-name custom/v1 sample_name`
**Explanation:** Uses custom primer scheme for non-SARS-CoV-2 pathogen. Scheme must be in ARTIC format with primers.bed and scheme.bed files.

### Generate consensus only
**Args:** `artic minion --read-file reads.fastq --scheme-directory /path/to/schemes --scheme-name nCoV-2019/V3 --consensus sample_name`
**Explanation:** Generates consensus sequence without detailed variant calling. Faster for surveillance when detailed variant info not needed.

### Check primer scheme
**Args:** `artic gather --scheme-directory /path/to/schemes --scheme-name nCoV-2019/V3`
**Explanation:** Downloads and validates primer scheme from ARTIC network. Ensures scheme files are available and properly formatted.

### Multi-sample batch processing
**Args:** `for s in samples/*.fastq; do artic minion --read-file "$s" --scheme-directory /path/to/schemes --scheme-name nCoV-2019/V3 "${s%.fastq}"; done`
**Explanation:** Processes multiple samples in batch. Each sample processed independently with separate output directory. Useful for surveillance studies.

### Adjust quality thresholds
**Args:** `artic minion --read-file reads.fastq --scheme-directory /path/to/schemes --scheme-name nCoV-2019/V3 --min-mapq 20 --min-coverage 20 sample_name`
**Explanation:** Sets minimum mapping quality (20) and coverage (20x) for variant calling. Higher thresholds increase confidence but may miss low-frequency variants.