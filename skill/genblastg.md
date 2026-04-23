---
name: genblastg
category: alignment
description: genBlast is a program suite, consisting of two programs: genBlastA and genBlastG. genBlastA parses local alignments, or high-scoring segment pairs (HSPs) produced by local sequence alignment programs such as BLAST and WU-BLAST and identify groups of HSPs.
tags: [genblastg, alignment]
author: oxo-call-community
source_url: "http://genome.sfu.ca/genblast/download.html"
---

## Concepts

- **Tool Overview**: genblastg (v1.39) - genBlast is a program suite, consisting of two programs: genBlastA and genBlastG. genBlastA parses local alignments, or high-scoring segment pairs (HSPs) produced by local sequence alignment programs such as BLAST and WU-BLAST and identify groups of HSPs.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda genblastg`

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
