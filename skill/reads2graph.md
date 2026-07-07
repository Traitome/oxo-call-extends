---
name: reads2graph
category: utility
description: Reads2Graph is an efficient tool for constructing edit-distance-based read graphs from short-read sequencing data.
tags: [reads2graph, utility, read-graph, assembly]
author: oxo-call-community
source_url: "https://github.com/Jappy0/reads2graph"
---

## Concepts

- **Tool Overview**: reads2graph builds graphs.
- **Core Function**: Read graph construction.
- **Algorithm**: Uses edit-distance methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces read graphs.
- **Use Case**: Assembly analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects graph building.
- **Parameters**: Must be configured.
- **Runtime**: Graph building may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reads2graph --help`
**Explanation:** Shows available options and usage instructions.

### Build graph
**Args:** `reads2graph build -i reads.fastq -o graph.gfa`
**Explanation:** Builds read graph.

### With parameters
**Args:** `reads2graph build -i reads.fastq -p params.yaml -o graph.gfa`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reads2graph -v build -i reads.fastq -o graph.gfa`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reads2graph -t 4 build -i reads.fastq -o graph.gfa`
**Explanation:** Uses 4 threads for parallel processing.

### With edit distance
**Args:** `reads2graph build -i reads.fastq -e 5 -o graph.gfa`
**Explanation:** Uses edit distance threshold.

### Generate report
**Args:** `reads2graph build -i reads.fastq -o graph.gfa --report report.html`
**Explanation:** Generates HTML report.