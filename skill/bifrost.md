---
name: bifrost
category: assembly
description: Bifrost - Highly parallel construction and indexing of colored and compacted de Bruijn graphs
tags: [de-bruijn-graph, k-mer, indexing, colored-graph]
author: oxo-call-community
source_url: "https://github.com/pmelsted/bifrost"
---

## Concepts
- **Tool Overview**: Bifrost is a tool for highly parallel construction and indexing of colored and compacted de Bruijn graphs. It builds cDBGs from sets of sequences and supports efficient querying.
- **Colored de Bruijn Graph**: A de Bruijn graph where each k-mer is associated with colors indicating which input samples contain it. Useful for comparative genomics and pangenomics.
- **Compacted Graph**: Compacts linear chains of nodes into single edges, reducing graph size while preserving topology.
- **Performance**: Uses parallel algorithms for fast graph construction and supports both command-line and C++ API usage.
- **Applications**: Pangenome analysis, read classification, variant detection, and metagenomics.

## Pitfalls
- **K-mer Size**: Choice of k-mer size affects graph structure. Smaller k-mers produce more connected graphs; larger k-mers are more specific but may fragment.
- **Memory Usage**: Large datasets require substantial memory for graph construction.
- **Input Format**: Accepts FASTA/FASTQ files and can use reference genomes for coloring.

## Examples
### Build a de Bruijn graph
**Args:** `bifrost build -k 31 -s sample1.fa -s sample2.fa -o graph`
**Explanation:** Builds a compacted de Bruijn graph with k=31 from two input samples.

### Build colored graph
**Args:** `bifrost build -k 31 -s sample1.fa -c color1 -s sample2.fa -c color2 -o colored_graph`
**Explanation:** Builds a colored cDBG where each sample gets a distinct color.

### Query graph with sequences
**Args:** `bifrost query -g graph -q queries.fa -o results.tsv`
**Explanation:** Queries the graph for presence/absence of query sequences.

### Update graph with new samples
**Args:** `bifrost update -g graph -s new_sample.fa -c new_color -o updated_graph`
**Explanation:** Adds a new sample to an existing colored de Bruijn graph.
