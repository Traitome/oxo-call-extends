---
name: mhg
category: annotation
description: MHG is an annotation-free graph-based tool to merge and partition homologous groups.
tags: [mhg, annotation, homology]
author: oxo-call-community
source_url: "https://github.com/NakhlehLab/Maximal-Homologous-Groups"
---

## Concepts

- **Tool Overview**: MHG v1.1.0 is an annotation-free graph-based tool for merging and partitioning homologous groups.
- **Core Function**: Identifies and partitions homologous sequence groups.
- **Graph-based Approach**: Uses graph algorithms for homology detection.
- **Annotation-free**: Operates without requiring prior gene annotation.
- **Input/Output**: Accepts sequence data; outputs homologous groups.
- **Evolutionary Analysis**: Supports evolutionary studies through homology detection.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal grouping.
- **Data Quality**: Homology detection accuracy depends on sequence quality.
- **Runtime**: Analysis of large sequence sets can be time-consuming.
- **Sequence Similarity**: Results depend on sequence similarity thresholds.

## Examples

### Identify homologous groups
**Args:** `mhg -i sequences.fasta -o groups.txt`
**Explanation:** Identifies and partitions homologous groups.

### With custom similarity threshold
**Args:** `mhg -i sequences.fasta -o groups.txt -s 0.8`
**Explanation:** Uses similarity threshold of 0.8.

### Batch processing
**Args:** `mhg -i fasta/ -o groups/`
**Explanation:** Processes multiple sequence files in batch mode.

### Detailed output
**Args:** `mhg -i sequences.fasta -o groups.txt -v`
**Explanation:** Generates detailed homology report.

### Graph visualization
**Args:** `mhg -i sequences.fasta -o groups.txt -g graph.dot`
**Explanation:** Generates graph visualization of homology relationships.