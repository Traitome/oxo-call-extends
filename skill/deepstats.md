---
name: deepstats
category: utility
description: A statistical and dataviz toolbox for deeptools, genomic signals, and more.
tags: [deepstats, utility, statistics, visualization, deeptools]
author: oxo-call-community
source_url: "https://github.com/gtrichard/deepStats"
---

## Concepts

- **Tool Overview**: deepStats v0.4 - Statistical analysis and visualization toolbox for deepTools output and genomic signal data.
- **Core Function**: Performs statistical tests and generates visualizations for genomic signal data from deepTools and similar tools.
- **Input/Output**: Expects deepTools output files (coverage, matrices); outputs statistical reports and plots.
- **Installation**: `conda install -c bioconda deepstats`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure input files are compatible with deepTools output formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepstats plot --input matrix.gz --output plot.pdf`
**Explanation:** Generates visualization from deepTools matrix output.
