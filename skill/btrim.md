---
name: btrim
category: assembly
description: Remove tips and sequencing errors from compacted de Bruijn graphs
tags: [btrim, debruijn, graph, error-correction, tip-removal]
author: oxo-call-community
source_url: "https://github.com/Malfoy/BTRIM"
---

## Concepts

- **Tool Overview**: BTRIM removes tips (short dead ends) from compacted de Bruijn graphs.
- **Core Function**: Cleans assembly graphs by removing sequencing error artifacts.
- **Input**: Compacted de Bruijn graph file.
- **Output**: Cleaned graph with tips removed.
- **Application**: Graph cleaning before assembly or variant calling.
- **Installation**: Install via bioconda: `conda install -c bioconda btrim`

## Pitfalls

- **Graph Format**: Requires compacted de Bruijn graph format.
- **Tip Length**: Set appropriate tip length threshold for your data.
- **Over-trimming**: Aggressive settings may remove valid short sequences.

## Examples

### Remove tips from graph
**Args:** `btrim -i graph.gfa -o cleaned.gfa`
**Explanation:** Removes tips from compacted de Bruijn graph.

### Set maximum tip length
**Args:** `btrim -i graph.gfa -l 200 -o cleaned.gfa`
**Explanation:** Removes tips shorter than 200bp.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
