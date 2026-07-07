---
name: megapath-nano
category: qc
description: Pathogen detection and AMR analysis for Oxford Nanopore long-read metagenomics.
tags: [megapath-nano, nanopore, pathogen-detection]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/MegaPath-Nano"
---

## Concepts

- **Tool Overview**: MegaPath-Nano analyzes Nanopore metagenomic data.
- **Core Function**: Detects pathogens and AMR from long-read data.
- **Nanopore Optimization**: Optimized for long-read sequencing.
- **Compositional Analysis**: Analyzes microbial composition.
- **Drug-level AMR**: Detects drug-specific AMR profiles.
- **Installation**: `conda install -c bioconda megapath-nano`

## Pitfalls

- **Data Quality**: Requires high-quality Nanopore data.
- **Computation Time**: Slow for large datasets.
- **Memory Requirements**: High memory usage.
- **Basecalling Quality**: Depends on initial basecalling.
- **False Positives**: May produce false positive detections.
- **Database Updates**: Requires updated reference databases.

## Examples

### Analyze Nanopore data
**Args:** `megapath-nano -i reads.fastq -o results/`
**Explanation:** Analyzes Nanopore metagenomic data.

### AMR detection
**Args:** `megapath-nano -i reads.fastq --amr -o results/`
**Explanation:** Detects antimicrobial resistance.

### Amplicon filtering
**Args:** `megapath-nano-amplicon -i reads.fastq -o filtered.fastq`
**Explanation:** Filters amplicon data for Nanopore.

### Verbose mode
**Args:** `megapath-nano -i reads.fastq -v -o results/`
**Explanation:** Shows detailed processing information.

### Help documentation
**Args:** `megapath-nano --help`
**Explanation:** Displays available options.
