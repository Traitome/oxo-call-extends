---
name: clinker-py
category: hpc
description: Gene cluster comparison figure generator
tags: [clinker-py, gene-cluster, visualization, bioinformatics, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/gamcil/clinker/blob/master/README.md"
---

## Concepts

- **Tool Overview**: clinker-py is a Python-based tool for generating gene cluster comparison figures, enabling visualization of gene synteny and comparisons across multiple genomes.
- **Core Function**: Visualizes gene clusters from different organisms to compare their structure and identify homologous genes.
- **Algorithm**: Parses gene annotations and generates visual comparisons of gene clusters.
- **Input**: GenBank files or gene annotation files from multiple organisms.
- **Output**: Interactive or static visualization of gene cluster comparisons.
- **Application**: Comparative genomics, gene cluster analysis, and evolutionary studies.
- **Installation**: Install via bioconda: `conda install -c bioconda clinker-py`

## Pitfalls

- **Annotation Format**: Requires properly formatted gene annotation files.
- **Gene Naming**: Consistent gene naming across clusters is important.
- **Visualization Complexity**: May become cluttered with many clusters.
- **Computational Resources**: May require significant resources for large datasets.
- **Memory Usage**: May require significant memory for large gene clusters.

## Examples

### Compare gene clusters
**Args:** `clinker genome1.gbk genome2.gbk genome3.gbk -o comparison.png`
**Explanation:** Generates comparison figure for gene clusters from multiple genomes.

### Interactive visualization
**Args:** `clinker genome1.gbk genome2.gbk --interactive`
**Explanation:** Opens interactive visualization in web browser.

### With output directory
**Args:** `clinker -i genomes/*.gbk -o results/`
**Explanation:** Processes all GenBank files in directory.

### Display help
**Args:** `clinker --help`
**Explanation:** Shows all available options and usage information.