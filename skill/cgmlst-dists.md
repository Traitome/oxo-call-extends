---
name: cgmlst-dists
category: genomics
description: Convert cgMLST allele table to distance matrix for phylogenetic analysis
tags: [cgmlst-dists, cgmlst, distance-matrix, phylogenetics, bacterial-typing]
author: oxo-call-community
source_url: "https://github.com/tseemann/cgmlst-dists"
---

## Concepts

- **Tool Overview**: cgMLST-dists converts cgMLST (core genome Multi-Locus Sequence Typing) allele tables to distance matrices for phylogenetic analysis.
- **Core Function**: Computes pairwise distances between bacterial isolates based on cgMLST alleles.
- **Algorithm**: Uses allele differences to calculate genetic distances between isolates.
- **Input**: cgMLST allele table (tabular format with alleles per isolate).
- **Output**: Distance matrix in PHYLIP or matrix format.
- **Application**: Bacterial population genetics and outbreak investigation.
- **Installation**: Install via bioconda: `conda install -c bioconda cgmlst-dists`

## Pitfalls

- **Input Format**: Requires specific cgMLST table format.
- **Missing Data**: Missing alleles may affect distance calculation.
- **Allele Quality**: Requires high-quality allele calls.
- **Matrix Size**: Large datasets may produce very large matrices.

## Examples

### Generate distance matrix
**Args:** `cgmlst-dists -i alleles.tsv -o distances.matrix`
**Explanation:** Converts cgMLST allele table to distance matrix.

### PHYLIP format output
**Args:** `cgmlst-dists -i alleles.tsv -o distances.phylip -p`
**Explanation:** Outputs distance matrix in PHYLIP format.

### Include headers
**Args:** `cgmlst-dists -i alleles.tsv -o distances.matrix -H`
**Explanation:** Includes headers in the output matrix.

### Display help
**Args:** `cgmlst-dists --help`
**Explanation:** Shows all available options and usage information.