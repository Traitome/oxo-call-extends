---
name: paraviewer
category: qc
description: ParaViewer generates visualizations for Paraphase HiFi analysis results.
tags: [paraviewer, qc, visualization, hifi]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/Paraviewer"
---

## Concepts

- **Tool Overview**: ParaViewer visualizes Paraphase analysis results.
- **Core Function**: Generates automated visualizations from HiFi data.
- **Algorithm**: Processes and visualizes haplotype data.
- **Input Format**: Accepts Paraphase output and gene annotations.
- **Output**: Produces visual reports and plots.
- **Use Case**: HiFi data visualization, haplotype analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Dependency Management**: Requires visualization libraries.
- **Output Quality**: Depends on input data quality.
- **Runtime**: Report generation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paraviewer --help`
**Explanation:** Shows available options and usage instructions.

### Generate report
**Args:** `paraviewer -i paraphase_output/ -o report/`
**Explanation:** Generates visualization report.

### With annotations
**Args:** `paraviewer -i paraphase_output/ -a genes.gff -o report/`
**Explanation:** Includes gene annotations in visualization.

### Verbose mode
**Args:** `paraviewer -v -i paraphase_output/ -o report/`
**Explanation:** Runs with verbose output.

### PDF output
**Args:** `paraviewer -i paraphase_output/ -o report.pdf --pdf`
**Explanation:** Exports report as PDF.

### Custom theme
**Args:** `paraviewer -i paraphase_output/ -o report/ --theme light`
**Explanation:** Uses light theme for visualization.

### Include statistics
**Args:** `paraviewer -i paraphase_output/ -o report/ --stats`
**Explanation:** Includes statistical analysis.