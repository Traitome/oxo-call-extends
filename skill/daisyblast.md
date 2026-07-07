---
name: daisyblast
category: programming
description: Python tool to find, plot, and export synteny blocks from all-vs-all BLAST
tags: [daisyblast, programming, synteny, BLAST, visualization]
author: oxo-call-community
source_url: "https://github.com/erinyoung/daisyblast"
---

## Concepts

- **Tool Overview**: daisyblast (v0.2.0+) is a Python tool for finding, plotting, and exporting synteny blocks from all-vs-all BLAST comparisons.
- **Core Function**: Identifies syntenic regions by analyzing BLAST results and visualizing conserved gene order.
- **Input/Output**: Input: Multiple FASTA sequences, BLAST output. Output: Synteny plots, block annotations.
- **Algorithm**: Uses BLAST alignment results to identify orthologous gene pairs and reconstruct syntenic blocks.
- **Key Features**: Automated synteny detection, publication-quality plots, multiple output formats.
- **Installation**: `conda install -c bioconda daisyblast`

## Pitfalls

- **BLAST Format**: Requires BLAST output in specific tabular format.
- **Parameter Selection**: E-value and coverage thresholds affect synteny detection.
- **Memory Usage**: Large genomes may require significant memory.
- **Visualization**: Very large syntenic regions may produce cluttered plots.
- **Dependencies**: Requires matplotlib and other Python packages.

## Examples

### Run synteny analysis
**Args:** `daisyblast -i genomes/ -o synteny_output/`
**Explanation:** Analyze synteny between genomes in the input directory.

### Generate visualization
**Args:** `daisyblast -i genomes/ -o output/ --plot`
**Explanation:** Create synteny plots for visualization.

### Export blocks
**Args:** `daisyblast -i genomes/ -o output/ --format csv`
**Explanation:** Export synteny blocks in CSV format.
