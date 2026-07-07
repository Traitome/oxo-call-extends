---
name: simba_pbg
category: utility
description: simba_pbg - Customized PyTorch-BigGraph for SIMBA
tags: ["simba_pbg", "utility", "pytorch", "biggraph"]
author: oxo-call-community
source_url: "https://github.com/pinellolab/simba_pbg"
---

## Concepts

- **Tool Overview**: simba_pbg (v1.2) is a customized PyTorch-BigGraph package for SIMBA.
- **Core Function**: Provides graph embedding capabilities for single-cell data.
- **Algorithm**: Uses PyTorch-BigGraph for scalable graph representation learning.
- **Input/Output**: Accepts graph data and produces embeddings.
- **Graph Embedding**: Specialized for large-scale graph representation learning.
- **Applications**: Single-cell analysis, graph-based embedding.

## Pitfalls

- **Memory Usage**: High memory requirements for large graphs.
- **PyTorch Dependency**: Requires PyTorch installation.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.
- **GPU Requirements**: May require GPU for optimal performance.

## Examples

### Train embedding
**Args:** `simba_pbg train -i graph.txt -o embeddings/`
**Explanation:** `-i` input graph file; `-o` output directory.

### With configuration
**Args:** `simba_pbg train -i graph.txt -c config.yaml -o embeddings/`
**Explanation:** `-c` configuration file.

### Inference mode
**Args:** `simba_pbg infer -i new_graph.txt -m model.pt -o new_embeddings/`
**Explanation:** `-m` trained model file.

### Help command
**Args:** `simba_pbg --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simba_pbg --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simba_pbg -v train -i graph.txt -o embeddings/`
**Explanation:** `-v` verbose output.

### GPU mode
**Args:** `simba_pbg train -i graph.txt -g -o embeddings/`
**Explanation:** `-g` use GPU acceleration.
