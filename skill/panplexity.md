---
name: panplexity
category: utility
description: Panplexity identifies low-complexity regions in pangenome graphs.
tags: [panplexity, utility, pangenome, complexity]
author: oxo-call-community
source_url: "https://github.com/AndreaGuarracino/panplexity"
---

## Concepts

- **Tool Overview**: Panplexity detects low-complexity regions in pangenome graphs.
- **Core Function**: Identifies repetitive and low-complexity sequences.
- **Algorithm**: Uses entropy-based complexity measurement.
- **Input Format**: Accepts pangenome graph files (GFA format).
- **Output**: Produces annotations of low-complexity regions.
- **Use Case**: Pangenome analysis, repeat masking, and sequence quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large graphs require memory.
- **Threshold Selection**: Results depend on complexity threshold.
- **Graph Quality**: Results depend on input graph quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `panplexity --help`
**Explanation:** Shows available options and usage instructions.

### Analyze graph
**Args:** `panplexity -i graph.gfa -o low_complexity.bed`
**Explanation:** Identifies low-complexity regions in graph.

### Complexity threshold
**Args:** `panplexity -i graph.gfa -t 0.5 -o low_complexity.bed`
**Explanation:** Sets complexity threshold to 0.5.

### Verbose mode
**Args:** `panplexity -v -i graph.gfa -o low_complexity.bed`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `panplexity -i graph.gfa -o low_complexity.gff --gff`
**Explanation:** Outputs in GFF format.

### Number of threads
**Args:** `panplexity -t 8 -i graph.gfa -o low_complexity.bed`
**Explanation:** Uses 8 threads for parallel processing.

### Filter by length
**Args:** `panplexity -m 100 -i graph.gfa -o low_complexity.bed`
**Explanation:** Filters regions shorter than 100 bp.