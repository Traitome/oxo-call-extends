---
name: gfinisher
category: assembly
description: GFinisher is an application tools for refinement and finalization of prokaryotic genomes assemblies using the bias of GC Skew to identify assembly errors and organizes the contigs/scaffolds with genomes references.
tags: [gfinisher, assembly]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/gfinisher/"
---

## Concepts

- **Tool Overview**: gfinisher (v1.4) - GFinisher is an application tools for refinement and finalization of prokaryotic genomes assemblies using the bias of GC Skew to identify assembly errors and organizes the contigs/scaffolds with genomes references.
- **Core Function**: Provides functionality for assembly tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda gfinisher`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
