---
name: panacus
category: utility
description: panacus computes counting statistics for GFA (Graphical Fragment Assembly) files.
tags: [panacus, utility, gfa, assembly-graph]
author: oxo-call-community
source_url: "https://github.com/codialab/panacus"
---

## Concepts

- **Tool Overview**: panacus analyzes assembly graphs in GFA format.
- **Core Function**: Computes statistics for assembly graphs.
- **Algorithm**: Parses GFA format and computes graph metrics.
- **Input Format**: Accepts GFA assembly graph files.
- **Output**: Produces graph statistics and metrics.
- **Use Case**: Pangenome analysis, assembly quality control, and graph analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large graphs require memory.
- **Format Compatibility**: May not support all GFA features.
- **Graph Complexity**: Complex graphs may be slow to process.
- **Validation**: Results should be validated for correctness.
- **Error Handling**: May have issues with malformed GFA files.

## Examples

### Display help
**Args:** `panacus --help`
**Explanation:** Shows available options and usage instructions.

### Compute statistics
**Args:** `panacus stats -i graph.gfa -o stats.txt`
**Explanation:** Computes graph statistics.

### Count nodes
**Args:** `panacus count -i graph.gfa -o counts.txt`
**Explanation:** Counts nodes and edges.

### Validate GFA
**Args:** `panacus validate -i graph.gfa`
**Explanation:** Validates GFA file format.

### Verbose mode
**Args:** `panacus stats -v -i graph.gfa -o stats.txt`
**Explanation:** Runs with verbose output.

### Output JSON
**Args:** `panacus stats -i graph.gfa -o stats.json --json`
**Explanation:** Outputs in JSON format.

### Filter graph
**Args:** `panacus filter -i graph.gfa -m 1000 -o filtered.gfa`
**Explanation:** Filters by minimum node length.