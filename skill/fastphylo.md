---
name: fastphylo
category: qc
description: "Fastphylo is software project containing the implementations of the algorithms 'Fast Computation of Distance Estimators' and 'Fast Neighbor Joining'."
tags: [fastphylo, qc, phylogeny, distance-estimation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/arvestad/FastPhylo"
---

## Concepts

- **Tool Overview**: FastPhylo is a software package implementing fast algorithms for distance estimation and neighbor joining in phylogenetic analysis.
- **Core Function**: Computes distance estimators and constructs phylogenetic trees using Fast Neighbor Joining.
- **Input/Output**: Input: Aligned sequences. Output: Distance matrix, phylogenetic tree.
- **Algorithm**: Implements Fast Computation of Distance Estimators and Fast Neighbor Joining algorithms.
- **Key Features**: Fast distance estimation, neighbor joining, large dataset support, efficient computation, multiple sequence types.
- **Installation**: `conda install -c bioconda fastphylo`

## Pitfalls

- **Alignment Quality**: Requires high-quality sequence alignment.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Tree Quality**: Results depend on input data quality.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Compute distance matrix
**Args:** `fastphylo distance -i alignment.fasta -o distance_matrix.txt`
**Explanation:** Computes distance matrix from alignment.

### Build tree with neighbor joining
**Args:** `fastphylo nj -i alignment.fasta -o tree.newick`
**Explanation:** Constructs phylogenetic tree using neighbor joining.

### Distance estimation only
**Args:** `fastphylo estimate -i alignment.fasta -o distances.txt`
**Explanation:** Performs distance estimation only.

### Bootstrapping
**Args:** `fastphylo nj -i alignment.fasta -o tree.newick -b 100`
**Explanation:** Performs 100 bootstrap replicates.

### Output formats
**Args:** `fastphylo nj -i alignment.fasta -o tree.nexus -f nexus`
**Explanation:** Outputs tree in Nexus format.