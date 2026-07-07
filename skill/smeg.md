---
name: smeg
category: metagenomics
description: SMEG - Strain-level Metagenomic Estimation of Growth rate measures growth rates of microbial strains from complex metagenomic datasets
tags: [smeg, metagenomics, growth-rate, strain-level, microbiome]
author: oxo-call-community
source_url: "https://github.com/ohlab/SMEG"
---

## Concepts

- **Tool Overview**: smeg (v1.1.5) - A tool for estimating microbial strain growth rates from metagenomic data
- **Core Function**: Measures growth rates of individual strains within complex microbial communities
- **Input/Output**: Accepts FASTQ reads and reference database; outputs growth rate estimates
- **Algorithm**: Uses coverage patterns and nucleotide composition to infer growth rates
- **Installation**: `conda install -c bioconda smeg`
- **Key Features**: Strain-level resolution, handles complex communities, provides statistical confidence

## Pitfalls

- **Reference Database**: Requires comprehensive reference genome database
- **Sequence Quality**: Low-quality reads affect accuracy
- **Strain Diversity**: May struggle with highly diverse communities
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for large databases
- **Coverage Depth**: Requires sufficient coverage for reliable estimation

## Examples

### Display help
**Args:** `smeg --help`
**Explanation:** Shows available options and usage information.

### Basic growth rate estimation
**Args:** `smeg -i reads.fastq -d reference_db/ -o results.txt`
**Explanation:** Estimate growth rates from metagenomic reads.

### With paired-end reads
**Args:** `smeg -i reads_1.fastq reads_2.fastq -d reference_db/ -o results.txt`
**Explanation:** Process paired-end sequencing data.

### Specify k-mer size
**Args:** `smeg -i reads.fastq -d reference_db/ -o results.txt -k 31`
**Explanation:** Set k-mer size for analysis.

### Filter by coverage
**Args:** `smeg -i reads.fastq -d reference_db/ -o results.txt -c 10`
**Explanation:** Filter strains with coverage < 10x.

### Generate plot
**Args:** `smeg -i reads.fastq -d reference_db/ -o results.txt -p growth_plot.pdf`
**Explanation:** Generate growth rate visualization.

### Batch processing
**Args:** `smeg -b sample_list.txt -d reference_db/ -o results_dir/`
**Explanation:** Process multiple samples in batch.

### With confidence intervals
**Args:** `smeg -i reads.fastq -d reference_db/ -o results.txt --confidence`
**Explanation:** Calculate confidence intervals for growth rate estimates.