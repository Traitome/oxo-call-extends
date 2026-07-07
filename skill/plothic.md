---
name: plothic
category: epigenomics
description: plothic plots Hi-C contact matrix heatmaps.
tags: [plothic, epigenomics, Hi-C, visualization]
author: oxo-call-community
source_url: "https://github.com/Jwindler/PlotHiC"
---

## Concepts

- **Tool Overview**: plothic visualizes Hi-C data.
- **Core Function**: Hi-C contact matrix plotting.
- **Algorithm**: Uses heatmap visualization methods.
- **Input Format**: Accepts Hi-C matrix files.
- **Output**: Produces heatmap images.
- **Use Case**: 3D genome analysis, chromatin interaction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large matrices require memory.
- **Data Quality**: Results depend on Hi-C quality.
- **Visualization Accuracy**: May have rendering issues.
- **Runtime**: Plotting may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plothic --help`
**Explanation:** Shows available options and usage instructions.

### Plot Hi-C matrix
**Args:** `plothic -i hic_matrix.txt -o heatmap.png`
**Explanation:** Plots Hi-C contact matrix heatmap.

### With parameters
**Args:** `plothic -i hic_matrix.txt -p params.yaml -o heatmap.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plothic -v -i hic_matrix.txt -o heatmap.png`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plothic -t 4 -i hic_matrix.txt -o heatmap.png`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plothic -i hic_matrix.txt -o heatmap.pdf --pdf`
**Explanation:** Outputs in PDF format.

### Generate report
**Args:** `plothic -i hic_matrix.txt -o heatmap.png --report report.html`
**Explanation:** Generates HTML report.