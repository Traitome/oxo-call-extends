---
name: matchtigs
category: utility
description: Algorithms for computing small and minimum plain text representations of k-mer sets.
tags: [matchtigs, k-mer, sequence-representation]
author: oxo-call-community
source_url: "https://github.com/algbio/matchtigs"
---

## Concepts

- **Tool Overview**: matchtigs computes compact representations of k-mer sets for sequence analysis.
- **Core Function**: Finds minimal text representations of k-mer sets efficiently.
- **k-mer Compression**: Compresses k-mer sets into smaller text representations.
- **Sequence Representation**: Enables efficient storage and comparison of k-mer sets.
- **Input/Output**: Accepts k-mer sets or FASTA files, produces compact text representations.
- **Installation**: `conda install -c bioconda matchtigs`

## Pitfalls

- **k-mer Size Selection**: k-mer size affects compression efficiency.
- **Memory Requirements**: Large k-mer sets require significant memory.
- **Computation Time**: Complex algorithms can be computationally intensive.
- **Output Size**: Compression ratio varies depending on input data.
- **Algorithm Selection**: Different algorithms have different trade-offs.
- **Data Quality**: Poor quality sequences affect representation quality.

## Examples

### Compute minimal representation
**Args:** `matchtigs -i kmers.txt -o minimal.txt`
**Explanation:** Computes minimal text representation of k-mer set.

### From FASTA file
**Args:** `matchtigs -f genome.fasta -o representation.txt`
**Explanation:** Extracts k-mers from FASTA and computes representation.

### Custom k-mer size
**Args:** `matchtigs -i kmers.txt -k 21 -o representation.txt`
**Explanation:** Uses k-mer size of 21 for representation.

### With compression
**Args:** `matchtigs -i kmers.txt -c -o compressed.txt`
**Explanation:** Enables additional compression of output.

### Statistics
**Args:** `matchtigs -i kmers.txt -s -o stats.txt`
**Explanation:** Computes statistics about k-mer representation.

### Help documentation
**Args:** `matchtigs --help`
**Explanation:** Displays available commands and options.
