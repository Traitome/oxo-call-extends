---
name: gepard
category: visualization
description: Gepard - Genome Pair Rapid Dotter for visualizing sequence similarities.
tags: [gepard, visualization, genome-comparison, dot-plot]
author: oxo-call-community
source_url: "https://cube.univie.ac.at/gepard"
---

## Concepts
- **Dot Plot Visualization**: Creates dot plots of sequence comparisons.
- **Genome Comparison**: Compares two genome sequences.
- **Sequence Alignment**: Visualizes sequence similarities.
- **Synteny Detection**: Detects syntenic regions.
- **Interactive Visualization**: Provides interactive dot plots.

## Pitfalls
- **Sequence Length**: Large sequences may affect performance.
- **Memory Usage**: Requires significant memory for large genomes.
- **Display Resolution**: May require adjustment for clarity.
- **Computational Time**: May take time for large comparisons.
- **Output Format**: Requires appropriate output format.

## Examples
### Create dot plot
**Args:** `gepard -f genome1.fasta genome2.fasta -o dotplot.png`
**Explanation:** Creates dot plot comparing two genomes.

### With options
**Args:** `gepard -f genome1.fasta genome2.fasta -k 10 -o dotplot.png`
**Explanation:** Uses k-mer size of 10 for comparison.

### Batch comparison
**Args:** `gepard -l genomes.txt -o ./plots/`
**Explanation:** Compares multiple genome pairs.

### Highlight regions
**Args:** `gepard -f genome1.fasta genome2.fasta -h regions.bed -o dotplot.png`
**Explanation:** Highlights specific regions in dot plot.

### Generate report
**Args:** `gepard -f genome1.fasta genome2.fasta -r -o report.html`
**Explanation:** Generates comparison report.