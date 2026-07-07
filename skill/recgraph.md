---
name: recgraph
category: alignment
description: RecGraph performs optimal sequence-to-graph alignment with recombinations for variant analysis.
tags: [recgraph, alignment, graph-alignment, recombination]
author: oxo-call-community
source_url: "https://github.com/AlgoLab/RecGraph"
---

## Concepts

- **Tool Overview**: recgraph aligns to graphs.
- **Core Function**: Graph alignment.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts sequences.
- **Output**: Produces graph alignments.
- **Use Case**: Variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large graphs require memory.
- **Graph Quality**: Affects alignment.
- **Parameters**: Must be configured.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recgraph --help`
**Explanation:** Shows available options and usage instructions.

### Align to graph
**Args:** `recgraph align -i sequences.fasta -g graph.gfa -o alignments.txt`
**Explanation:** Aligns sequences to graph.

### With parameters
**Args:** `recgraph align -i sequences.fasta -p params.yaml -o alignments.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recgraph -v align -i sequences.fasta -o alignments.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recgraph -t 4 align -i sequences.fasta -o alignments.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With recombination
**Args:** `recgraph align -i sequences.fasta -r recombination.txt -o alignments.txt`
**Explanation:** Uses recombination info.

### Generate report
**Args:** `recgraph align -i sequences.fasta -o alignments.txt --report report.html`
**Explanation:** Generates HTML report.