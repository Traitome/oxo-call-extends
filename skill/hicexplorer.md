---
name: hicexplorer
category: bioinformatics
description: HiCExplorer provides tools for processing, analyzing and visualizing Hi-C and capture Hi-C data.
tags: [hicexplorer, Hi-C, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://hicexplorer.readthedocs.org/"
---

## Concepts

- **Hi-C Processing**: HiCExplorer processes Hi-C data.

- **Data Analysis**: Analyzes Hi-C contact maps.

- **Visualization**: Visualizes Hi-C data.

- **Capture Hi-C**: Supports capture Hi-C data.

- **Contact Maps**: Generates and analyzes contact maps.

- **Chromatin Architecture**: Studies chromatin architecture.

## Pitfalls

- **Data Quality**: Results depend on input data quality.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Normalization**: Proper normalization is critical.

## Examples

### Process Hi-C data
**Args:** `hicBuildMatrix --input reads.bam --output matrix.cool`
**Explanation:** Builds Hi-C matrix from aligned reads.

### Visualize matrix
**Args:** `hicPlotMatrix --matrix matrix.cool --output heatmap.png`
**Explanation:** Generates heatmap from Hi-C matrix.

### Call TADs
**Args:** `hicFindTADs --matrix matrix.cool --output tads.bed`
**Explanation:** Identifies topologically associating domains.

### Batch processing
**Args:** `for f in *.bam; do hicBuildMatrix --input $f --output ${f%.bam}.cool; done`
**Explanation:** Processes multiple Hi-C datasets.

### Generate report
**Args:** `hicQC --matrix matrix.cool --output qc_report.html`
**Explanation:** Generates quality control report.

### Help command
**Args:** `hicBuildMatrix --help`
**Explanation:** Shows available options and usage information.