---
name: fastme
category: utility
description: "a comprehensive, accurate and fast distance-based phylogeny inference program."
tags: [fastme, utility, phylogeny, distance-based, bioinformatics]
author: oxo-call-community
source_url: "http://www.atgc-montpellier.fr/fastme/binaries.php"
---

## Concepts

- **Tool Overview**: FastME is a comprehensive, accurate, and fast distance-based phylogeny inference program for constructing phylogenetic trees.
- **Core Function**: Infers phylogenetic trees from distance matrices using efficient algorithms.
- **Input/Output**: Input: Distance matrix, aligned sequences. Output: Phylogenetic tree (Newick format).
- **Algorithm**: Uses balanced minimum evolution algorithm for tree inference.
- **Key Features**: Fast tree inference, accurate results, multiple input formats, support for large datasets, bootstrap support.
- **Installation**: `conda install -c bioconda fastme`

## Pitfalls

- **Distance Matrix**: Requires pre-computed distance matrix or aligned sequences.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Tree Quality**: Results depend on input data quality.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic tree inference
**Args:** `fastme -i alignment.fasta -o tree.newick`
**Explanation:** Infers phylogenetic tree from alignment.

### With distance matrix
**Args:** `fastme -i distance_matrix.txt -o tree.newick -d`
**Explanation:** Uses distance matrix for tree inference.

### Bootstrap support
**Args:** `fastme -i alignment.fasta -o tree.newick -b 100`
**Explanation:** Performs 100 bootstrap replicates.

### Output formats
**Args:** `fastme -i alignment.fasta -o tree.nexus -f nexus`
**Explanation:** Outputs tree in Nexus format.

### Advanced options
**Args:** `fastme -i alignment.fasta -o tree.newick -s SPR -t`
**Explanation:** Uses SPR moves and outputs tree statistics.