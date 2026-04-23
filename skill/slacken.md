---
name: slacken
category: metagenomics
description: Slacken is a very scalable implementation of the Kraken 2 metagenomic classification method, based on Apache Spark.
tags: [slacken, metagenomics]
author: oxo-call-community
source_url: "https://github.com/JNP-Solutions/Slacken/blob/v2.0.0/README.md"
---

## Concepts

- **Tool Overview**: slacken (v2.0.0) - Slacken is a very scalable implementation of the Kraken 2 metagenomic classification method, based on Apache Spark.
- **Core Function**: Slacken is a very scalable implementation of the Kraken 2 metagenomic classification method, based on Apache Spark.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda slacken`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `slacken -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run slacken with typical input and output options.
