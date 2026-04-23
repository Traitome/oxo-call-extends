---
name: taxburst
category: metagenomics
description: sunburst plots for taxonomy
tags: [taxburst, metagenomics]
author: oxo-call-community
source_url: "https://github.com/taxburst/taxburst"
---

## Concepts

- **Tool Overview**: taxburst (v0.3.2) - sunburst plots for taxonomy
- **Core Function**: sunburst plots for taxonomy
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxburst`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxburst -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxburst with typical input and output options.
