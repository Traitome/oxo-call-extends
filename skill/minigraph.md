---
name: minigraph
category: alignment
description: Proof-of-concept seq-to-graph mapper and graph generator.
tags: [minigraph, alignment, graph]
author: oxo-call-community
source_url: "https://github.com/lh3/minigraph"
---

## Concepts

- **Tool Overview**: Minigraph v0.21 maps sequences to variation graphs.
- **Core Function**: Maps sequencing reads to graph-based references.
- **Graph Mapping**: Aligns sequences to variation graphs.
- **Graph Construction**: Builds variation graphs from multiple sequences.
- **Input/Output**: Accepts sequences; outputs graph alignments.
- **Pan-genomics**: Supports pan-genome analysis workflows.

## Pitfalls

- **Graph-based**: Requires graph reference format.
- **Computational Resources**: Mapping may require significant resources.
- **Memory Requirements**: Memory usage depends on graph size.
- **Parameter Tuning**: May require parameter adjustment for optimal mapping.
- **Data Quality**: Mapping accuracy depends on input data quality.
- **Graph Complexity**: Performance may vary with graph complexity.

## Examples

### Build graph from sequences
**Args:** `minigraph -x lr ref.fasta alts.fasta > graph.gfa`
**Explanation:** Builds variation graph from reference and alternatives.

### Map reads to graph
**Args:** `minigraph -x lr graph.gfa reads.fastq > alignments.gaf`
**Explanation:** Maps reads to variation graph.

### With custom parameters
**Args:** `minigraph -x lr -k 19 graph.gfa reads.fastq > alignments.gaf`
**Explanation:** Uses k-mer size of 19 for mapping.

### Batch processing
**Args:** `minigraph -x lr graph.gfa fastq/*.fastq > alignments.gaf`
**Explanation:** Processes multiple read files.

### Simplify graph
**Args:** `minigraph -x lr -m 100 ref.fasta alts.fasta > graph.gfa`
**Explanation:** Merges similar paths in the graph.