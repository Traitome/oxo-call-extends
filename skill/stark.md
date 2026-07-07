---
name: stark
category: sequence-analysis
description: A tool for bluntifying a bidirected de Bruijn graph by removing overlaps.
tags: [stark, de-bruijn-graph, assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hnikaein/stark"
---

## Concepts

- **Tool Overview**: stark (v0.1.1) is a tool for processing bidirected de Bruijn graphs by removing overlaps between nodes.
- **Core Function**: "Bluntifies" de Bruijn graphs by removing overlapping k-mers between adjacent nodes.
- **Algorithm**: Uses graph traversal to identify and remove overlapping sequences between connected nodes.
- **Input/Output**: Input: de Bruijn graph in GFA or similar format; Output: Bluntified graph with reduced overlaps.
- **Applications**: Genome assembly refinement, graph simplification for variant calling.
- **Installation**: `conda install -c bioconda stark` or compile from source.

## Pitfalls

- **Graph Format**: Requires specific graph format; incorrect formatting causes processing failures.
- **k-mer Size**: Incorrect k-mer size affects graph structure and overlap detection.
- **Memory Requirements**: Large graphs require significant memory for processing.
- **Graph Complexity**: Highly complex graphs may produce unexpected results.
- **Edge Cases**: Circular graphs or disconnected components may require special handling.
- **Output Validation**: Always validate output graph integrity after processing.

## Examples

### Display help
**Args:** `stark --help`
**Explanation:** Shows available options and usage information.

### Basic graph bluntification
**Args:** `stark -i graph.gfa -o bluntified.gfa`
**Explanation:** Bluntify de Bruijn graph by removing overlaps.

### With specific k-mer size
**Args:** `stark -i graph.gfa -o bluntified.gfa -k 31`
**Explanation:** Specify k-mer size used in graph construction.

### Verbose mode
**Args:** `stark -i graph.gfa -o bluntified.gfa -v`
**Explanation:** Run with detailed logging for debugging.

### Stats output
**Args:** `stark -i graph.gfa -o bluntified.gfa --stats stats.txt`
**Explanation:** Generate statistics about graph transformation.

### Force processing
**Args:** `stark -i graph.gfa -o bluntified.gfa -f`
**Explanation:** Force processing even if errors are detected.

### Multiple graphs
**Args:** `stark -i graph1.gfa graph2.gfa -o output/`
**Explanation:** Process multiple graphs together.

### Validate output
**Args:** `stark -i graph.gfa -o bluntified.gfa --validate`
**Explanation:** Validate output graph for consistency.

### Compressed input
**Args:** `stark -i graph.gfa.gz -o bluntified.gfa`
**Explanation:** Process compressed graph file.
