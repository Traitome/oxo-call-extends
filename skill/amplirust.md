---
name: amplirust
category: utility
description: In-silico PCR primer matching and product extraction tool
tags: [amplirust, utility, FASTA]
author: oxo-call-community
source_url: "https://github.com/erdikilic/amplirust"
---

## Concepts

- **Tool Overview**: amplirust (v0.2.0) - In-silico PCR primer matching and product extraction tool
- **Core Function**: Amplirust is a high-performance in-silico PCR tool written in Rust that performs primer matching and PCR product extraction from FASTA sequences. Features include SIMD-accelerated approximate matching...
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda amplirust`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `--input input_file --output output_file`
**Explanation:** Process input and generate output
