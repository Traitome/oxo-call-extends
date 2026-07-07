---
name: nspdk
category: machine-learning
description: NSPDK (Neighborhood Subgraph Pairwise Distance Kernel) is a graph kernel for machine learning.
tags: [nspdk, machine-learning, graph-kernel, bioinformatics]
author: oxo-call-community
source_url: "http://dtai.cs.kuleuven.be/ml/systems/nspdk"
---

## Concepts

- **Tool Overview**: NSPDK computes graph kernels for machine learning applications.
- **Core Function**: Calculates pairwise distances between graph neighborhoods.
- **Algorithm**: Uses subgraph isomorphism for kernel computation.
- **Input Format**: Accepts graph representations in various formats.
- **Output**: Produces kernel matrix for machine learning.
- **Use Case**: Graph classification, bioinformatics, and pattern recognition.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Computational Cost**: Kernel computation can be intensive.
- **Memory Usage**: Large graphs require memory.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Graph Size**: Limited by graph size and complexity.
- **Documentation**: Limited documentation.

## Examples

### Display help
**Args:** `nspdk --help`
**Explanation:** Shows available options and usage instructions.

### Compute kernel
**Args:** `nspdk -i graphs.txt -o kernel.txt`
**Explanation:** Computes kernel matrix from graphs.

### GraphML input
**Args:** `nspdk -i graphs.graphml -o kernel.txt --graphml`
**Explanation:** Reads GraphML format graphs.

### Neighborhood size
**Args:** `nspdk -i graphs.txt -o kernel.txt -k 3`
**Explanation:** Sets neighborhood size to 3.

### Output similarity
**Args:** `nspdk -i graphs.txt -o similarity.txt --similarity`
**Explanation:** Outputs similarity matrix instead of distance.

### Threads
**Args:** `nspdk -i graphs.txt -o kernel.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nspdk -i graphs.txt -o kernel.txt -v`
**Explanation:** Runs with verbose output.