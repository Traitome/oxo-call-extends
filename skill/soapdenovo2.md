---
name: soapdenovo2
category: assembly
description: SOAPdenovo is a novel short-read assembly method that can build a de novo draft assembly for the human-sized genomes.
tags: [soapdenovo2, assembly]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapdenovo.html"
---

## Concepts

- **Tool Overview**: soapdenovo2 (v2.40) - SOAPdenovo is a novel short-read assembly method that can build a de novo draft assembly for the human-sized genomes.
- **Core Function**: SOAPdenovo is a novel short-read assembly method that can build a de novo draft assembly for the human-sized genomes.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda soapdenovo2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `soapdenovo2 -i <reads.fastq> -o <output_dir>`
**Explanation:** Run soapdenovo2 with typical input and output options.
