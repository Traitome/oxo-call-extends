---
name: vardict-java
category: variant-calling
description: Java port of the VarDict variant discovery program
tags: [vardict-java, variant-calling]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/VarDictJava"
---

## Concepts

- **Tool Overview**: vardict-java (v1.8.3) - Java port of the VarDict variant discovery program
- **Core Function**: Java port of the VarDict variant discovery program
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vardict-java`

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
