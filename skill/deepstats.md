---
name: deepstats
category: utility
description: deepStats - statistical and dataviz toolbox for deepTools and genomic signals.
tags: [deepstats, utility, statistics, visualization, deeptools]
author: oxo-call-community
source_url: "https://github.com/gtrichard/deepStats"
---

## Concepts

- **Tool Overview**: deepstats (v0.4+) is a statistical analysis and visualization toolbox for deepTools output and genomic signal data. It provides comprehensive statistical tests and visualizations.
- **Core Function**: Performs statistical tests and generates visualizations for genomic signal data from deepTools and similar tools, enabling comprehensive genomic data analysis.
- **Input/Output**: Input: deepTools output files (coverage, matrices), genomic signal files. Output: Statistical reports, visualizations (heatmaps, profiles, scatter plots).
- **Algorithm**: Implements various statistical methods including correlation analysis, differential testing, and clustering for genomic signals.
- **Key Features**: Integrates with deepTools, comprehensive visualization, statistical testing, supports multiple genomic signal types, batch processing.
- **Installation**: `conda install -c bioconda deepstats`

## Pitfalls

- **Input Compatibility**: Requires deepTools-compatible input files.
- **Data Quality**: Requires high-quality genomic signal data.
- **Computational Resources**: May require significant computational resources for large datasets.
- **Visualization Complexity**: Complex visualizations may require tuning.
- **Statistical Assumptions**: Requires understanding of statistical assumptions.

## Examples

### Generate visualization from matrix
**Args:** `deepstats plot --input matrix.gz --output plot.pdf`
**Explanation:** Generates visualization from deepTools matrix output.

### Perform statistical analysis
**Args:** `deepstats stats --input signal.bw --output statistics.txt`
**Explanation:** Perform statistical analysis on genomic signal data.

### Compare multiple signals
**Args:** `deepstats compare --input signal1.bw signal2.bw --output comparison.pdf`
**Explanation:** Compare multiple genomic signals with visualization.