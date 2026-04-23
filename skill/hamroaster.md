---
name: hamroaster
category: hpc
description: An analysis pipeline to compare the output of different AMR detection tools and provide metrics of their performance
tags: [hamroaster, hpc]
author: oxo-call-community
source_url: "https://github.com/ewissel/hAMRoaster"
---

## Concepts

- **Tool Overview**: hamroaster (v2.0) - An analysis pipeline to compare the output of different AMR detection tools and provide metrics of their performance
- **Core Function**: Provides functionality for hpc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hamroaster`

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
