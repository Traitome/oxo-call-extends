---
name: sis
category: assembly
description: A tool that uses mummer to scaffold small genomes.
tags: [sis, assembly]
author: oxo-call-community
source_url: "http://marte.ic.unicamp.br:8747/"
---

## Concepts

- **Tool Overview**: sis (v0.1.2) - A tool that uses mummer to scaffold small genomes.
- **Core Function**: A tool that uses mummer to scaffold small genomes.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sis`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sis -i <reads.fastq> -o <output_dir>`
**Explanation:** Run sis with typical input and output options.
