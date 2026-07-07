---
name: schicexplorer
category: visualization
description: scHiCExplorer - Tools to process, analyze and visualize single-cell Hi-C data
tags: ["schicexplorer", "visualization", "Hi-C", "single-cell"]
author: oxo-call-community
source_url: "https://github.com/joachimwolff/scHiCExplorer"
---

## Concepts

- **Tool Overview**: scHiCExplorer (v7) is a set of programs to process, analyze and visualize single-cell Hi-C data.
- **Core Function**: Provides comprehensive tools for single-cell Hi-C data analysis.
- **Algorithm**: Implements various Hi-C analysis and visualization algorithms.
- **Input/Output**: Accepts Hi-C data and produces processed data and visualizations.
- **Single-Cell Focus**: Specifically designed for single-cell Hi-C data analysis.
- **Applications**: 3D genome organization, chromatin interactions, and spatial genomics.

## Pitfalls

- **Data Quality**: Results depend on input Hi-C data quality.
- **Complexity**: Hi-C data analysis can be computationally complex.
- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Normalization**: Proper normalization is critical for Hi-C analysis.
- **Visualization**: Generating meaningful visualizations requires careful parameter selection.

## Examples

### Basic Hi-C processing
**Args:** `scHiCExplorer -i hic_data.cool -o processed.h5`
**Explanation:** `-i` input Hi-C data; `-o` processed output.

### Contact matrix visualization
**Args:** `scHiCExplorer plot -i hic_data.cool -o heatmap.png`
**Explanation:** Generates contact matrix heatmap.

### Quality control
**Args:** `scHiCExplorer qc -i hic_data.cool -o qc_report.html`
**Explanation:** Generates QC report for Hi-C data.

### Normalization
**Args:** `scHiCExplorer normalize -i hic_data.cool -m ICE -o normalized.cool`
**Explanation:** `-m ICE` applies ICE normalization.

### Compartment analysis
**Args:** `scHiCExplorer compartments -i hic_data.cool -o compartments.bed`
**Explanation:** Identifies A/B compartments.

### Loop calling
**Args:** `scHiCExplorer call-loops -i hic_data.cool -o loops.bedpe`
**Explanation:** Calls chromatin loops from Hi-C data.

### Multi-resolution analysis
**Args:** `scHiCExplorer -i hic_data.cool --resolution 10000 -o processed.h5`
**Explanation:** `--resolution` sets analysis resolution.