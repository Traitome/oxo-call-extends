---
name: gum
category: bioinformatics
description: gum is a header-only C++ library for representation and manipulation of sequence graphs in bioinformatics.
tags: [gum, sequence-graphs, C++, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cartoonist/gum"
---

## Concepts

- **Sequence Graphs**: gum provides data structures for sequence graph representation.

- **Header-only Library**: Distributed as a header-only library for easy integration.

- **Graph Operations**: Supports various graph manipulation operations.

- **Path Finding**: Enables path finding and traversal in sequence graphs.

- **Graph Construction**: Facilitates construction of sequence graphs from sequences.

- **Memory Efficiency**: Designed for memory-efficient graph representation.

## Pitfalls

- **C++ Dependencies**: Requires C++ compilation and appropriate dependencies.

- **Memory Usage**: Large graphs may require significant memory.

- **Graph Complexity**: Complex graphs may affect performance.

- **API Learning Curve**: Requires understanding of graph data structures.

- **Version Compatibility**: Ensure compatibility with C++ compiler version.

## Examples

### Include library
**Args:** `#include <gum/graph.hpp>`
**Explanation:** Includes the gum library header.

### Create graph
**Args:** `gum::Graph graph;`
**Explanation:** Creates a new sequence graph.

### Add node
**Args:** `auto node = graph.add_node("sequence_data");`
**Explanation:** Adds a node to the graph.

### Add edge
**Args:** `graph.add_edge(node1, node2);`
**Explanation:** Adds an edge between two nodes.

### Find path
**Args:** `auto path = graph.find_path(start, end);`
**Explanation:** Finds path between two nodes.

### Export graph
**Args:** `graph.export_dot("graph.dot");`
**Explanation:** Exports graph to DOT format.

### Iterate nodes
**Args:** `for (auto& node : graph.nodes()) { /* process */ }`
**Explanation:** Iterates over all nodes in the graph.