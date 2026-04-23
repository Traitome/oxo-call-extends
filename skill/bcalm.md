---
name: bcalm
category: assembly
description: BCALM 2 - Construct compacted de Bruijn graph from sequencing data
tags: [de-bruijn-graph, assembly-graph, k-mer, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/GATB/bcalm"
---

## Concepts

- **Tool Overview**: BCALM 2 constructs the compacted de Bruijn graph from sequencing data, used as a foundation for genome assembly.

- **Compacted Graph**: Produces compacted de Bruijn graph where non-branching paths are merged into unitigs.

- **Memory Efficient**: Uses disk-based algorithms for memory-efficient processing of large datasets.

- **K-mer Based**: Builds graph from k-mer counts, suitable for various k-mer sizes.

- **Assembly Foundation**: Output used by many assemblers for scaffold construction.

## Pitfalls

- **K-mer Size**: K-mer size affects graph structure. Choose appropriate size for genome complexity.

- **Disk Space**: Requires substantial disk space for temporary files. Ensure adequate storage.

- **Coverage**: Low coverage regions may have fragmented graphs. Adjust parameters.

- **Memory vs Speed**: Trade-off between memory usage and speed. Adjust based on resources.

## Examples

### Basic graph construction
**Args:** `bcalm -in reads.fasta -kmer-size 31 -out graph`
**Explanation:** Constructs compacted de Bruijn graph with k=31 from reads.

### Specify k-mer size
**Args:** `bcalm -in reads.fasta -kmer-size 51 -abundance-min 2 -out graph`
**Explanation:** Uses k=51 and minimum abundance 2 for error correction.

### Memory-efficient mode
**Args:** `bcalm -in reads.fasta -kmer-size 31 -max-memory 16 -out graph`
**Explanation:** Limits memory usage to 16GB, using disk for overflow.

### Parallel processing
**Args:** `bcalm -in reads.fasta -kmer-size 31 -nb-cores 8 -out graph`
**Explanation:** Uses 8 CPU cores for parallel graph construction.

### Output GFA format
**Args:** `bcalm -in reads.fasta -kmer-size 31 -out graph -gfa`
**Explanation:** Outputs graph in GFA format for compatibility with other tools.
