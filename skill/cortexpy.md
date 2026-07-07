---
name: cortexpy
category: assembly
description: Python API for manipulating Cortex de novo assembly graph data
tags: [cortexpy, python-api, assembly-graph, cortex, bioinformatics]
author: oxo-call-community
source_url: "https://cortexpy.readthedocs.io"
---

## Concepts

- **Tool Overview**: Cortexpy is a Python API for manipulating (Mc)Cortex de novo assembly graph and link data, providing programmatic access to assembly graph operations.
- **Core Function**: Enables programmatic manipulation of Cortex assembly graphs, including graph traversal, visualization, and analysis.
- **Algorithm**: Provides Python bindings for Cortex graph data structures and operations.
- **Input**: Cortex graph files (.ctx), sequence data.
- **Output**: Manipulated graphs, analysis reports, visualizations.
- **Application**: Assembly graph analysis, variant detection, graph manipulation in pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda cortexpy`

## Pitfalls

- **Graph Complexity**: Large assembly graphs can be memory-intensive.
- **Version Compatibility**: API may change between versions.
- **Graph Integrity**: Modifying graphs requires careful handling to maintain consistency.
- **Performance**: Graph operations on large datasets may be slow.
- **Documentation**: Requires understanding of Cortex file format.

## Examples

### Load graph
**Args:** `from cortexpy.graph import Graph; graph = Graph.from_file('assembly.ctx')`
**Explanation:** Loads Cortex graph from file.

### Traverse graph
**Args:** `for node in graph.nodes(): print(node.kmer, node.coverage)`
**Explanation:** Iterates through all nodes in the graph.

### Extract subgraph
**Args:** `subgraph = graph.extract_region('chr1:1000-2000')`
**Explanation:** Extracts subgraph for specific genomic region.

### Visualize graph
**Args:** `graph.visualize('graph.png', layout='circular')`
**Explanation:** Generates visualization of the assembly graph.

### Display help
**Args:** `python -c "import cortexpy; help(cortexpy)"`
**Explanation:** Shows available API documentation.