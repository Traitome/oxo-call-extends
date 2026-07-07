---
name: cuttlefish
category: annotation
description: Construction of the compacted de Bruijn graph efficiently.
tags: [cuttlefish, annotation, de-bruijn-graph, sequence-analysis, k-mer]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/cuttlefish/blob/v2.2.0/README.md"
---

## Concepts

- **Tool Overview**: cuttlefish (v2.2.0+) is a tool for efficient construction of compacted de Bruijn graphs from sequencing data.
- **Core Function**: Builds compressed de Bruijn graphs for sequence analysis, assembly, and indexing.
- **Input/Output**: Input: FASTA/FASTQ sequence files. Output: Compacted de Bruijn graph, k-mer counts.
- **Algorithm**: Uses minimizer-based indexing and graph compaction for efficient storage.
- **Key Features**: Memory-efficient, supports large datasets, integrates with sequence assembly tools.
- **Installation**: `conda install -c bioconda cuttlefish`

## Pitfalls

- **k-mer Size**: k-mer size selection affects graph complexity and memory usage.
- **Memory Requirements**: Large datasets may require significant memory for graph construction.
- **Input Quality**: Low-quality sequences may increase graph complexity.
- **Output Format**: Graph output requires compatible tools for downstream analysis.
- **Compaction**: Over-compaction may lose biological information.

## Examples

### Build de Bruijn graph
**Args:** `cuttlefish build -i reads.fastq -k 31 -o graph/`
**Explanation:** Build compacted de Bruijn graph with k-mer size 31.

### Count k-mers
**Args:** `cuttlefish count -i reads.fastq -k 25 -o kmer_counts.txt`
**Explanation:** Count k-mers in sequencing reads with k=25.

### Build graph with multiple files
**Args:** `cuttlefish build -i reads1.fastq reads2.fastq -k 31 -o combined_graph/`
**Explanation:** Build graph from multiple sequencing files.
