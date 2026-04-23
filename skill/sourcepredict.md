---
name: sourcepredict
category: metagenomics
description: Classification and prediction of the origin of metagenomic samples.
tags: [sourcepredict, metagenomics, sam]
author: oxo-call-community
source_url: "https://github.com/maxibor/sourcepredict"
---

## Concepts

- **Tool Overview**: sourcepredict (v0.5.1) - Classification and prediction of the origin of metagenomic samples.
- **Core Function**: Classification and prediction of the origin of metagenomic samples.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sourcepredict`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sourcepredict -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run sourcepredict with typical input and output options.
