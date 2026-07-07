---
name: disty
category: population-genomics
description: Disty McMatrixface - Compute distance matrix from core genome alignment.
tags: [disty, population-genomics, distance-matrix, core-genome, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/c2-d2/disty"
---

## Concepts

- **Tool Overview**: disty (v0.1.0+) is a fast distance matrix computation tool from core genome alignments.
- **Core Function**: Calculates pairwise distances from core genome alignment files efficiently.
- **Input/Output**: Input: Core genome multiple sequence alignment (FASTA). Output: Distance matrix (TSV).
- **Algorithm**: Uses efficient algorithms for computing genetic distances from alignments.
- **Key Features**: Fast distance calculation, core genome alignment support, multiple distance models, parallel processing, large dataset support.
- **Installation**: `conda install -c bioconda disty`

## Pitfalls

- **Input Requirements**: Requires core genome multiple sequence alignment.
- **Alignment Quality**: Poor alignments affect distance calculation.
- **Missing Data**: Handle gaps and missing data appropriately.
- **Memory Usage**: Large alignments may require significant memory.
- **Model Selection**: Choosing appropriate substitution model is critical.

## Examples

### Compute distance matrix
**Args:** `disty --alignment core_aln.fa --output distances.tsv`
**Explanation:** Computes distance matrix from core genome alignment.

### With specific model
**Args:** `disty --alignment core_aln.fa --output distances.tsv --model JC69`
**Explanation:** Use Jukes-Cantor substitution model.

### Ignore gaps
**Args:** `disty --alignment core_aln.fa --output distances.tsv --ignore-gaps`
**Explanation:** Ignore gap positions when calculating distances.

### Parallel processing
**Args:** `disty --alignment core_aln.fa --output distances.tsv --threads 8`
**Explanation:** Use multiple threads for parallel computation.

### Generate tree
**Args:** `disty --alignment core_aln.fa --output distances.tsv --tree tree.nwk`
**Explanation:** Generate phylogenetic tree from distance matrix.