---
name: eukdetect
category: expression
description: "Detect eukaryotes from shotgun metagenomic sequencing data"
tags: [eukdetect, expression, metagenomics, eukaryotes, marker-genes]
author: oxo-call-community
source_url: "https://github.com/allind/EukDetect"
---

## Concepts

- **Tool Overview**: EukDetect is a tool for detecting and quantifying eukaryotic microbes in shotgun metagenomic sequencing data using conserved marker genes.
- **Core Function**: Identifies eukaryotic organisms by mapping reads to a curated database of conserved marker genes and estimating relative abundances.
- **Input/Output**: Input: Shotgun metagenomic reads (FASTQ), marker database. Output: Eukaryotic taxon profiles, abundance estimates, marker gene coverage.
- **Algorithm**: Uses read mapping to conserved marker genes combined with taxonomic classification to identify eukaryotic taxa.
- **Key Features**: Eukaryotic detection, abundance estimation, marker gene-based identification, support for complex metagenomes, visualization tools.
- **Installation**: `conda install -c bioconda eukdetect`

## Pitfalls

- **Marker Database**: Detection depends on comprehensive marker database.
- **Host Contamination**: Host DNA may interfere with eukaryotic detection.
- **Abundance Bias**: Relative abundance estimates may not reflect actual biomass.
- **Computation Resources**: Large datasets require significant computational resources.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic eukaryote detection
**Args:** `eukdetect -i reads.fastq -o results/`
**Explanation:** Detects eukaryotes from metagenomic sequencing data.

### With custom database
**Args:** `eukdetect -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses custom marker database for detection.

### Paired-end reads
**Args:** `eukdetect -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** Processes paired-end metagenomic reads.

### Abundance estimation
**Args:** `eukdetect -i reads.fastq -o results/ --quantify`
**Explanation:** Estimates relative abundances of detected eukaryotes.

### Batch processing
**Args:** `eukdetect -i samples/ -o results/ --batch`
**Explanation:** Processes multiple metagenomic samples in batch mode.