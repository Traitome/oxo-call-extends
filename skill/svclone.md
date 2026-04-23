---
name: svclone
category: utility
description: Computational method for inferring cancer cell fraction of tumour SVs from WGS.
tags: [svclone, utility]
author: oxo-call-community
source_url: "https://github.com/mcmero/SVclone"
---

## Concepts

- **Tool Overview**: svclone (v1.1.4) - Computational method for inferring cancer cell fraction of tumour SVs from WGS.
- **Core Function**: Computational method for inferring cancer cell fraction of tumour SVs from WGS.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svclone`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svclone -i <input_file> -o <output_file>`
**Explanation:** Run svclone with typical input and output options.
