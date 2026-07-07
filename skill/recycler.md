---
name: recycler
category: assembly
description: Recycler extracts circular sequences from de novo assembly graphs for plasmid detection.
tags: [recycler, assembly, circular-sequences, plasmid-detection]
author: oxo-call-community
source_url: "https://github.com/Shamir-Lab/Recycler"
---

## Concepts

- **Tool Overview**: recycler extracts circles.
- **Core Function**: Circular sequence extraction.
- **Algorithm**: Uses graph methods.
- **Input Format**: Accepts assembly graphs.
- **Output**: Produces circular sequences.
- **Use Case**: Plasmid detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large graphs require memory.
- **Graph Quality**: Affects extraction.
- **Parameters**: Must be configured.
- **Runtime**: Extraction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recycler --help`
**Explanation:** Shows available options and usage instructions.

### Extract circles
**Args:** `recycler extract -i assembly_graph.gfa -o circular_sequences.fasta`
**Explanation:** Extracts circular sequences.

### With parameters
**Args:** `recycler extract -i assembly_graph.gfa -p params.yaml -o circular_sequences.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recycler -v extract -i assembly_graph.gfa -o circular_sequences.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recycler -t 4 extract -i assembly_graph.gfa -o circular_sequences.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With minimum length
**Args:** `recycler extract -i assembly_graph.gfa -l 1000 -o circular_sequences.fasta`
**Explanation:** Uses minimum length threshold.

### Generate report
**Args:** `recycler extract -i assembly_graph.gfa -o circular_sequences.fasta --report report.html`
**Explanation:** Generates HTML report.