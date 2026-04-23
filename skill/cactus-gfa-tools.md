---
name: cactus-gfa-tools
category: formatting
description: Command-line utilities for the Cactus Pangenome Pipeline
tags: [cactus, gfa, pangenome, graph]
author: oxo-call-community
source_url: "https://github.com/ComparativeGenomicsToolkit/cactus-gfa-tools"
---

## Concepts

- **Tool Overview**: cactus-gfa-tools provides utilities for working with GFA graphs in the Cactus pangenome pipeline.
- **Core Function**: Converts and processes GFA format graphs for pangenome analysis.
- **Input**: GFA format assembly or variation graphs.
- **Output**: Processed GFA files compatible with Cactus pipeline.
- **Application**: Pangenome graph construction and manipulation.
- **Installation**: Install via bioconda: `conda install -c bioconda cactus-gfa-tools`

## Pitfalls

- **GFA Format**: Requires GFA v1 or v2 format input.
- **Graph Complexity**: Large graphs may require significant memory.
- **Cactus Dependency**: Designed as part of the Cactus pangenome pipeline.

## Examples

### Convert GFA format
**Args:** `cactus-gfa-tools convert -i input.gfa -o output.gfa`
**Explanation:** Converts GFA graph to compatible format for Cactus pipeline.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
