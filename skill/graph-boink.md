---
name: graph-boink
category: bioinformatics
description: graph-boink performs streaming de Bruijn graph compaction and sketching for efficient sequence analysis.
tags: [graph-boink, de-bruijn-graph, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/camillescott/boink"
---

## Concepts

- **De Bruijn Graph Compaction**: graph-boink compacts de Bruijn graphs to reduce memory usage while preserving structural information.

- **Streaming Processing**: Processes sequence data in a streaming fashion, enabling analysis of large datasets without loading everything into memory.

- **Graph Sketching**: Creates compact representations (sketches) of de Bruijn graphs for efficient comparison and analysis.

- **k-mer Analysis**: Analyzes k-mer frequencies and distributions to understand sequence composition.

- **Memory Efficiency**: Optimized for memory usage, making it suitable for large-scale sequence analysis.

- **Multiple Input Formats**: Supports various input formats including FASTA, FASTQ, and compressed files.

## Pitfalls

- **k-mer Size Selection**: Choosing appropriate k-mer size is critical. Too small may increase noise, too large may fragment the graph.

- **Memory Management**: Very large datasets may still require significant memory despite streaming approach.

- **Graph Complexity**: Highly repetitive sequences can create very complex graphs.

- **Input Quality**: Low-quality sequences can produce noisy graphs. Preprocess sequences carefully.

- **Parameter Tuning**: Adjust parameters based on dataset characteristics and desired output.

## Examples

### Build de Bruijn graph
**Args:** `boink build -i reads.fastq -k 31 -o graph.gfa`
**Explanation:** Builds a de Bruijn graph with k-mer size 31 from sequencing reads.

### Compact graph
**Args:** `boink compact -i graph.gfa -o compacted.gfa`
**Explanation:** Compacts the de Bruijn graph to reduce size.

### Generate graph sketch
**Args:** `boink sketch -i graph.gfa -o sketch.txt`
**Explanation:** Creates a compact sketch of the de Bruijn graph.

### Analyze k-mer frequencies
**Args:** `boink kmers -i reads.fastq -k 21 -o kmer_counts.txt`
**Explanation:** Counts k-mer frequencies in the input reads.

### Stream processing
**Args:** `cat reads.fastq | boink stream -k 31 -o graph.gfa`
**Explanation:** Processes reads from standard input in streaming mode.

### Compare graphs
**Args:** `boink compare -i graph1.gfa graph2.gfa -o comparison.txt`
**Explanation:** Compares two de Bruijn graphs and outputs differences.

### Filter low-abundance k-mers
**Args:** `boink filter -i graph.gfa -m 5 -o filtered.gfa`
**Explanation:** Removes k-mers with abundance below 5 from the graph.