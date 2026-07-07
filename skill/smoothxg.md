---
name: smoothxg
category: pangenomics
description: smoothxg - Local reconstruction of variation graphs using partial order alignment
tags: [smoothxg, pangenomics, variation-graphs, alignment, partial-order]
author: oxo-call-community
source_url: "https://github.com/pangenome/smoothxg"
---

## Concepts

- **Tool Overview**: smoothxg (v0.8.2) - A tool for constructing and manipulating variation graphs
- **Core Function**: Builds variation graphs from multiple sequence alignments
- **Input/Output**: Accepts FASTA/GFA files; outputs variation graphs in GFA format
- **Algorithm**: Uses partial order alignment for graph construction
- **Installation**: `conda install -c bioconda smoothxg`
- **Key Features**: Pangenome graph construction, local alignment, graph refinement

## Pitfalls

- **Input Requirements**: Requires properly formatted input sequences
- **Computation Time**: Large datasets can be computationally intensive
- **Memory Usage**: May require significant memory for large graphs
- **Graph Complexity**: Complex graphs may be difficult to interpret
- **Reference Dependence**: Performance depends on reference quality
- **Output Size**: Graph files can be very large

## Examples

### Display help
**Args:** `smoothxg --help`
**Explanation:** Shows available options and usage information.

### Build variation graph
**Args:** `smoothxg -i input.fasta -o graph.gfa`
**Explanation:** Build variation graph from input sequences.

### With reference genome
**Args:** `smoothxg -i input.fasta -r reference.fasta -o graph.gfa`
**Explanation:** Use reference genome to guide graph construction.

### Refine existing graph
**Args:** `smoothxg -i graph.gfa -o refined.gfa -R`
**Explanation:** Refine and simplify existing variation graph.

### Extract subgraph
**Args:** `smoothxg -i graph.gfa -o subgraph.gfa -c chr1:1-10000`
**Explanation:** Extract subgraph for specific genomic region.

### Convert to FASTA
**Args:** `smoothxg -i graph.gfa -o sequences.fasta -f fasta`
**Explanation:** Convert graph back to FASTA sequences.

### Merge graphs
**Args:** `smoothxg -i graph1.gfa graph2.gfa -o merged.gfa -M`
**Explanation:** Merge multiple variation graphs.

### Generate statistics
**Args:** `smoothxg -i graph.gfa -s stats.txt`
**Explanation:** Generate graph statistics report.