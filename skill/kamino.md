---
name: kamino
category: utility
description: Tool for building phylogenomic datasets quickly and reproducibly.
tags: [kamino, utility, phylogenomics, datasets, reproducible]
author: oxo-call-community
source_url: "https://github.com/rderelle/kamino/blob/1.0.0/README.md"
---

## Concepts

- **Tool Overview**: kamino (v1.0.0) - Builds phylogenomic datasets from sequence data.
- **Ortholog Identification**: Identifies orthologous genes across species.
- **Multiple Alignment**: Performs multiple sequence alignment.
- **Dataset Construction**: Creates concatenated alignments for phylogenomics.
- **Reproducibility**: Ensures reproducible dataset construction.
- **Automation**: Automates the entire phylogenomic dataset pipeline.

## Pitfalls

- **Input Quality**: Requires high-quality input sequences.
- **Ortholog Detection**: May miss distant orthologs.
- **Alignment Quality**: Poor alignments affect downstream analysis.
- **Memory Usage**: Large datasets require significant memory.
- **Runtime**: Processing many taxa can be time-consuming.
- **Dependency Management**: Requires proper installation of dependencies.

## Examples

### Build dataset
**Args:** `kamino build -i genomes/ -o dataset/`
**Explanation:** Builds phylogenomic dataset from genome sequences.

### Specify ortholog threshold
**Args:** `kamino build -i genomes/ -o dataset/ -t 0.8`
**Explanation:** Sets ortholog identification threshold to 0.8.

### Include specific genes
**Args:** `kamino build -i genomes/ -o dataset/ -g gene_list.txt`
**Explanation:** Includes only specified genes in dataset.

### Parallel processing
**Args:** `kamino build -i genomes/ -o dataset/ -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output statistics
**Args:** `kamino stats -i dataset/ -o stats.txt`
**Explanation:** Generates dataset statistics.

### Validate dataset
**Args:** `kamino validate -i dataset/`
**Explanation:** Validates dataset integrity.