---
name: stringmeup
category: metagenomics
description: A post-processing tool to reclassify Kraken 2 output based on the confidence score and/or minimum minimizer hit groups.
tags: [stringmeup, metagenomics]
author: oxo-call-community
source_url: "https://github.com/danisven/StringMeUp"
---

## Concepts

- **Tool Overview**: stringmeup (v0.1.5) - A post-processing tool to reclassify Kraken 2 output based on the confidence score and/or minimum minimizer hit groups.
- **Core Function**: A post-processing tool to reclassify Kraken 2 output based on the confidence score and/or minimum minimizer hit groups.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stringmeup`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stringmeup -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run stringmeup with typical input and output options.
