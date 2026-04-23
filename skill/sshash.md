---
name: sshash
category: formatting
description: SSHash is a compressed dictionary data structure for k-mers (strings of length k over the DNA alphabet {A,C,G,T}), based on Sparse and Skew Hashing.
tags: [sshash, formatting]
author: oxo-call-community
source_url: "https://github.com/jermp/sshash"
---

## Concepts

- **Tool Overview**: sshash (v5.1.0) - SSHash is a compressed dictionary data structure for k-mers (strings of length k over the DNA alphabet {A,C,G,T}), based on Sparse and Skew Hashing.
- **Core Function**: SSHash is a compressed dictionary data structure for k-mers (strings of length k over the DNA alphabet {A,C,G,T}), based on Sparse and Skew Hashing.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sshash`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sshash -i <input_file> -o <output_file>`
**Explanation:** Run sshash with typical input and output options.
