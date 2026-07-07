---
name: debwt
category: hpc
description: Parallel BWT index construction for large and highly similar genome sequences.
tags: [debwt, hpc, BWT-index, genome-indexing, parallel-computing]
author: oxo-call-community
source_url: "https://github.com/DixianZhu/deBWT"
---

## Concepts

- **Tool Overview**: debwt (v1.0.1+) is an efficient parallel method for constructing Burrows-Wheeler Transform (BWT) indexes of DNA sequences. It is specifically designed for large and highly similar genomes with good scalability on multi-core servers and clusters.
- **Core Function**: Constructs BWT indexes for genomic sequences efficiently using parallel computing, enabling fast sequence alignment and search operations.
- **Input/Output**: Input: FASTA genome sequences. Output: BWT index files, FM-index components.
- **Algorithm**: Uses a parallelized approach to BWT construction, leveraging multi-core processing and optimized data structures for large collections of genomes.
- **Key Features**: High scalability, parallel computing support, handles highly similar genomes efficiently, memory-efficient, suitable for clusters.
- **Installation**: `conda install -c bioconda debwt`

## Pitfalls

- **Memory Requirements**: Large genomes require significant memory resources.
- **Parallel Overhead**: May have overhead for small datasets.
- **Input Format**: Requires properly formatted FASTA files.
- **Cluster Configuration**: Requires proper MPI configuration for distributed computing.
- **Similarity Assumption**: Optimized for highly similar genomes; may not perform optimally on diverse sequences.

## Examples

### Build BWT index
**Args:** `debwt -i genome.fasta -o bwt_index/`
**Explanation:** Construct BWT index for a single genome.

### Parallel construction
**Args:** `mpirun -np 16 debwt -i genomes/ -o bwt_index/`
**Explanation:** Build BWT index using 16 MPI processes.

### Index multiple genomes
**Args:** `debwt -i genome1.fasta genome2.fasta -o combined_index/`
**Explanation:** Build combined BWT index for multiple genomes.