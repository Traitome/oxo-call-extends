---
name: unimap
category: alignment
description: Unimap is a fork of minimap2 optimized for assembly-to-reference alignment.
tags: [unimap, alignment]
author: oxo-call-community
source_url: "https://github.com/lh3/unimap"
---

## Concepts

- **Tool Overview**: unimap (v0.1) - Unimap is a fork of minimap2 optimized for assembly-to-reference alignment. It integrates the minigraph chaining algorithm and can align through long INDELs (up to 100kb by default) much faster than minimap2. Unimap is a better fit for resolving segmental duplications and is recommended over minimap2 for alignment between high-quality assemblies.  Unimap does not replace minimap2 for other types of alignment. It drops the support of multi-part index and short-read mapping. Its long-read alignment is different from minimap2 but is not necessarily better. Unimap is more of a specialized minimap2 at the moment.
- **Core Function**: Unimap is a fork of minimap2 optimized for assembly-to-reference alignment.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda unimap`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
