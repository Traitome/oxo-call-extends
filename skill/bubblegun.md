---
name: bubblegun
category: assembly
description: Detecting bubbles and superbubbles in GFA graphs with nested structure reporting
tags: [bubblegun, graph, bubble, superbubble, gfa]
author: oxo-call-community
source_url: "https://github.com/fawaz-dabbaghieh/bubble_gun"
---

## Concepts

- **Tool Overview**: BubbleGun detects bubbles and superbubbles in GFA graphs and reports nested structures.
- **Core Function**: Identifies bubble structures in assembly graphs with hierarchy information.
- **Input**: Assembly graph in GFA format.
- **Output**: Bubble structures with nested hierarchy.
- **Features**: Reports both simple and nested bubble structures.
- **Installation**: Install via bioconda: `conda install -c bioconda bubblegun`

## Pitfalls

- **GFA Format**: Requires GFA format input graph.
- **Nested Structures**: Complex graphs may have deeply nested bubbles.
- **Memory Usage**: Large graphs require significant memory.

## Examples

### Detect bubbles in graph
**Args:** `bubblegun -i assembly.gfa -o bubbles.tsv`
**Explanation:** Detects bubbles and superbubbles in GFA assembly graph.

### Report nested structures
**Args:** `bubblegun -i assembly.gfa --nested -o bubbles_nested.tsv`
**Explanation:** Reports nested bubble structures with hierarchy.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
