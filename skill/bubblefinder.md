---
name: bubblefinder
category: assembly
description: Detecting superbubbles and snarls in assembly graphs
tags: [bubblefinder, graph, superbubble, snarl, assembly]
author: oxo-call-community
source_url: "https://github.com/algbio/BubbleFinder"
---

## Concepts

- **Tool Overview**: BubbleFinder detects superbubbles and snarls in assembly graphs.
- **Core Function**: Identifies bubble structures representing sequence variations.
- **Input**: Assembly graph in GFA format.
- **Output**: List of superbubbles/snarls with coordinates.
- **Application**: Variation detection in genome assembly graphs.
- **Installation**: Install via bioconda: `conda install -c bioconda bubblefinder`

## Pitfalls

- **Graph Format**: Requires GFA format assembly graph.
- **Complexity**: Large graphs may have many nested bubbles.
- **Interpretation**: Bubbles may represent variants, repeats, or assembly errors.

## Examples

### Find superbubbles
**Args:** `bubblefinder -i assembly.gfa -o bubbles.tsv`
**Explanation:** Detects superbubbles in assembly graph.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
