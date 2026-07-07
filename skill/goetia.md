---
name: goetia
category: bioinformatics
description: Goetia provides streaming de Bruijn graph compaction and sketching for efficient sequence analysis and comparison.
tags: [goetia, de-bruijn-graph, sequence-analysis, streaming, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/camillescott/goetia"
---

## Concepts

- **De Bruijn Graph Compaction**: Goetia efficiently compacts de Bruijn graphs by removing redundant nodes and edges, reducing memory footprint.

- **Streaming Processing**: Processes sequence data in a streaming fashion, enabling analysis of large datasets without loading everything into memory.

- **Graph Sketching**: Creates compact representations (sketches) of de Bruijn graphs for efficient comparison between datasets.

- **k-mer Analysis**: Supports flexible k-mer sizes and provides tools for k-mer counting and frequency analysis.

- **Assembly Support**: Integrates with assembly pipelines to improve contig assembly and scaffolding.

- **Metagenomics Applications**: Optimized for metagenomic data analysis, enabling efficient comparison of microbial communities.

## Pitfalls

- **k-mer Size Selection**: Choosing the appropriate k-mer size is critical. Too small k-mers increase noise, too large k-mers reduce sensitivity.

- **Memory Management**: While streaming reduces memory usage, very large datasets may still require careful resource management.

- **Graph Complexity**: Highly complex graphs with many branching paths can be computationally intensive to process.

- **Quality Trimming**: Low-quality reads can introduce errors in the de Bruijn graph. Always preprocess reads before analysis.

- **Reference Bias**: De Bruijn graph-based approaches may have inherent bias towards reference sequences if used in mapping contexts.

## Examples

### Build de Bruijn graph from reads
**Args:** `goetia build -i reads.fastq -k 31 -o graph.gfa`
**Explanation:** Builds a de Bruijn graph with k-mer size 31 from the input reads and saves it in GFA format.

### Compact existing graph
**Args:** `goetia compact -i graph.gfa -o compacted.gfa`
**Explanation:** Compacts the de Bruijn graph by removing redundant nodes and edges.

### Generate graph sketch
**Args:** `goetia sketch -i graph.gfa -o sketch.json`
**Explanation:** Creates a compact sketch representation of the de Bruijn graph for efficient comparison.

### Compare multiple graphs
**Args:** `goetia compare -i graph1.gfa graph2.gfa -o comparison.txt`
**Explanation:** Compares two de Bruijn graphs and outputs similarity metrics.

### Stream processing mode
**Args:** `cat reads.fastq | goetia stream -k 27 -o streaming_graph.gfa`
**Explanation:** Processes reads from standard input in streaming mode, building the graph incrementally.

### Extract k-mer frequencies
**Args:** `goetia kmers -i reads.fastq -k 21 -o frequencies.txt`
**Explanation:** Counts k-mer frequencies in the input reads and outputs a frequency table.

### Filter low-abundance k-mers
**Args:** `goetia filter -i graph.gfa -m 5 -o filtered.gfa`
**Explanation:** Filters out k-mers with abundance below 5, reducing noise in the graph.