---
name: strainest
category: metagenomics
description: Abundance estimation of strains from metagenomic sequencing data.
tags: [strainest, metagenomics, strain-profiling, abundance-estimation]
author: oxo-call-community
source_url: "https://github.com/compmetagen/strainest"
---

## Concepts

- **Tool Overview**: strainest (v1.2.4) is a tool for estimating strain-level abundances from metagenomic sequencing data.
- **Core Function**: Quantifies the relative abundance of different strains within microbial communities.
- **Algorithm**: Uses reference genomes and read mapping to estimate strain abundances.
- **Input/Output**: Input: Metagenomic reads (FASTQ), reference genomes; Output: Strain abundance estimates.
- **Applications**: Tracking strain dynamics, monitoring microbial populations, outbreak investigation.
- **Installation**: `conda install -c bioconda strainest` or download from GitHub.

## Pitfalls

- **Reference Quality**: Incomplete or incorrect reference genomes affect estimation.
- **Strain Similarity**: Very similar strains are hard to distinguish.
- **Read Coverage**: Low coverage affects abundance estimation accuracy.
- **Mapping Quality**: Poor mapping produces incorrect estimates.
- **Reference Bias**: Reference genome selection affects results.
- **Memory Requirements**: Large reference databases require significant memory.

## Examples

### Display help
**Args:** `strainest --help`
**Explanation:** Shows available options and usage information.

### Basic abundance estimation
**Args:** `strainest -i reads.fastq -r references/ -o results.txt`
**Explanation:** Estimate strain abundances from metagenomic reads.

### With pre-computed mapping
**Args:** `strainest -i aligned.bam -r references/ -o results.txt`
**Explanation:** Use pre-aligned BAM file for abundance estimation.

### Verbose mode
**Args:** `strainest -i reads.fastq -r references/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strainest -i reads.fastq -r references/ -o results.txt --plot`
**Explanation:** Generate visualization of strain abundances.

### Custom thresholds
**Args:** `strainest -i reads.fastq -r references/ -o results.txt -c 0.01`
**Explanation:** Minimum abundance threshold of 0.01.

### Batch processing
**Args:** `strainest -i batch/ -r references/ -o results/`
**Explanation:** Process multiple metagenomic samples together.

### Filter by coverage
**Args:** `strainest -i reads.fastq -r references/ -o results.txt -m 10`
**Explanation:** Minimum coverage threshold of 10x.

### Generate report
**Args:** `strainest -i reads.fastq -r references/ -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
