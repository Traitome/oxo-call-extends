---
name: sistr_cmd
category: alignment
description: Salmonella In Silico Typing Resource (SISTR) commandline tool for serovar prediction
tags: [sistr_cmd, alignment]
author: oxo-call-community
source_url: "https://github.com/phac-nml/sistr_cmd/"
---

## Concepts

- **Tool Overview**: sistr_cmd (v1.1.3) - Salmonella In Silico Typing Resource (SISTR) commandline tool for serovar prediction
- **Core Function**: Salmonella In Silico Typing Resource (SISTR) commandline tool for serovar prediction
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sistr_cmd`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sistr_cmd -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run sistr_cmd with typical input and output options.
