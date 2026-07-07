---
name: fastcov
category: formatting
description: "This package installs fastcov and all it's dependencies. fastcov is used to plot coverage plots based on BAM files."
tags: [fastcov, formatting, coverage, BAM, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RaverJay/fastcov"
---

## Concepts

- **Tool Overview**: fastcov is a tool for generating coverage plots from BAM alignment files, providing visualization of sequencing coverage across genomes.
- **Core Function**: Generates coverage plots and statistics from BAM files.
- **Input/Output**: Input: BAM file, genome reference. Output: Coverage plots (PNG/PDF), coverage statistics.
- **Algorithm**: Parses BAM files and calculates coverage depth across genomic regions.
- **Key Features**: Coverage visualization, BAM processing, multiple output formats, customizable plots, batch processing.
- **Installation**: `conda install -c bioconda fastcov`

## Pitfalls

- **BAM Index**: Requires indexed BAM file.
- **Memory Usage**: Large BAM files may require significant memory.
- **Genome Reference**: Requires matching reference genome.
- **Format Compatibility**: Requires standard BAM format.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic coverage plot
**Args:** `fastcov -i alignment.bam -o coverage_plot.png`
**Explanation:** Generates coverage plot from BAM file.

### With reference genome
**Args:** `fastcov -i alignment.bam -g genome.fasta -o coverage_plot.png`
**Explanation:** Uses reference genome for coordinate information.

### Coverage statistics
**Args:** `fastcov -i alignment.bam -o stats.txt --stats`
**Explanation:** Generates coverage statistics.

### Multiple regions
**Args:** `fastcov -i alignment.bam -o coverage_plot.png -r regions.bed`
**Explanation:** Generates coverage plot for specific regions.

### PDF output
**Args:** `fastcov -i alignment.bam -o coverage_plot.pdf --format pdf`
**Explanation:** Outputs coverage plot in PDF format.