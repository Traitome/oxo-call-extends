---
name: cloci
category: hpc
description: Co-occurrence Locus and Orthologous Cluster Identifier
tags: [cloci, orthologs, gene-clusters, bioinformatics, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/xonq/cloci"
---

## Concepts

- **Tool Overview**: cloci is a tool for identifying co-occurrence loci and orthologous gene clusters across multiple genomes.
- **Core Function**: Detects orthologous gene clusters and their co-occurrence patterns across different species.
- **Algorithm**: Uses sequence similarity and phylogenetic analysis to identify orthologous clusters.
- **Input**: Multiple genome sequences or gene annotations from different organisms.
- **Output**: Orthologous cluster assignments and co-occurrence relationships.
- **Application**: Comparative genomics, gene family evolution, and functional annotation.
- **Installation**: Install via bioconda: `conda install -c bioconda cloci`

## Pitfalls

- **Genome Quality**: Requires well-annotated genomes for accurate clustering.
- **Computational Resources**: May require significant resources for large datasets.
- **Orthology Prediction**: Depends on accurate orthology inference.
- **Memory Usage**: May require significant memory for large number of genomes.
- **Parameter Tuning**: May require adjustment of clustering parameters.

## Examples

### Identify orthologous clusters
**Args:** `cloci -i genomes/ -o clusters.txt`
**Explanation:** Identifies orthologous gene clusters across multiple genomes.

### With annotation file
**Args:** `cloci -i genomes/ -a annotations.gff -o clusters.txt`
**Explanation:** Uses gene annotations for more accurate clustering.

### With output format
**Args:** `cloci -i genomes/ -o clusters.txt --format tsv`
**Explanation:** Outputs results in TSV format.

### Display help
**Args:** `cloci --help`
**Explanation:** Shows all available options and usage information.