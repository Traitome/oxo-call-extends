---
name: squigualiser
category: visualization
description: Squigualiser - Visualize Oxford Nanopore raw signals
tags: [squigualiser, visualization, ont, nanopore, raw-signals]
author: oxo-call-community
source_url: "https://github.com/hiruna72/squigualiser"
---

## Concepts

- **Tool Overview**: squigualiser (v0.6.4) - A signal visualization tool
- **Core Function**: Visualizes Oxford Nanopore raw signals
- **Input/Output**: Accepts ONT signal files; outputs visualizations
- **Algorithm**: Signal processing and visualization algorithms
- **Installation**: `conda install -c bioconda squigualiser`
- **Key Features**: Signal visualization, ONT data, raw signal analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted ONT signal files
- **Signal Quality**: Signal quality affects visualization accuracy
- **Visualization Settings**: Settings affect visualization clarity
- **Memory Usage**: Large signal files require significant memory
- **Output Format**: Output format depends on configuration
- **Visualization Performance**: Performance depends on signal size and settings

## Examples

### Display help
**Args:** `squigualiser --help`
**Explanation:** Shows available options and usage information.

### Basic signal visualization
**Args:** `squigualiser -i signals.fast5 -o visualization.html`
**Explanation:** Visualize ONT raw signals.

### With basecalling
**Args:** `squigualiser -i signals.fast5 -b basecalls.fasta -o visualization.html`
**Explanation:** Include basecalling in visualization.

### With quality scores
**Args:** `squigualiser -i signals.fast5 -q quality.txt -o visualization.html`
**Explanation:** Include quality scores in visualization.

### Multiple files
**Args:** `squigualiser -i signal1.fast5 signal2.fast5 -o visualization.html`
**Explanation:** Visualize multiple signal files.

### Output detailed results
**Args:** `squigualiser -i signals.fast5 -o visualization.html --detailed`
**Explanation:** Output detailed signal information.

### Output statistics
**Args:** `squigualiser -i signals.fast5 -o visualization.html --stats`
**Explanation:** Output signal statistics.

### Generate report
**Args:** `squigualiser -i signals.fast5 -o visualization.html --report`
**Explanation:** Generate signal visualization report.

### With custom settings
**Args:** `squigualiser -i signals.fast5 -o visualization.html --settings custom.json`
**Explanation:** Use custom visualization settings.