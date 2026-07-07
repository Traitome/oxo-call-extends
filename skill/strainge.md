---
name: strainge
category: metagenomics
description: "Strain Genome Explorer: a tool suite for tracking and characterizing low-abundance strains."
tags: [strainge, metagenomics, strain-tracking, low-abundance]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/strainge"
---
## Concepts

- **Tool Overview**: strainge (v1.3.9) is a tool suite for tracking and characterizing low-abundance microbial strains in metagenomic data.
- **Core Function**: Identifies and tracks rare strains using allele-specific analysis and coverage-based detection.
- **Algorithm**: Uses reference-guided variant calling and relative abundance estimation for strain tracking.
- **Input/Output**: Input: Metagenomic reads (FASTQ), reference genomes; Output: Strain profiles and abundance estimates.
- **Applications**: Tracking low-abundance pathogens, monitoring microbial population dynamics, outbreak investigation.
- **Installation**: `conda install -c bioconda strainge` or download from GitHub.

## Pitfalls

- **Reference Quality**: Incomplete reference genomes affect strain detection.
- **Abundance Threshold**: Very low-abundance strains may be missed.
- **Read Coverage**: Insufficient coverage affects variant calling accuracy.
- **Strain Similarity**: Very similar strains are hard to distinguish.
- **Memory Requirements**: Large reference databases require significant memory.
- **Computational Time**: Processing large datasets can be computationally intensive.

## Examples

### Display help
**Args:** `strainge --help`
**Explanation:** Shows available options and usage information.

### Basic strain tracking
**Args:** `strainge track -i reads.fastq -r reference.fasta -o results/`
**Explanation:** Track strains from metagenomic reads.

### With database
**Args:** `strainge track -i reads.fastq -d database/ -o results/`
**Explanation:** Use pre-built reference database for strain tracking.

### Verbose mode
**Args:** `strainge track -i reads.fastq -r reference.fasta -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strainge track -i reads.fastq -r reference.fasta -o results/ --plot`
**Explanation:** Generate visualization of strain abundances.

### Custom thresholds
**Args:** `strainge track -i reads.fastq -r reference.fasta -o results/ -c 0.001`
**Explanation:** Minimum abundance threshold of 0.001.

### Batch processing
**Args:** `strainge track -i batch/ -r reference.fasta -o results/`
**Explanation:** Process multiple metagenomic samples together.

### Build database
**Args:** `strainge build -i references/ -o database/`
**Explanation:** Build reference database from multiple genomes.

### Generate report
**Args:** `strainge track -i reads.fastq -r reference.fasta -o results/ --report`
**Explanation:** Generate comprehensive HTML report.
