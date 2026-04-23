---
name: soapdenovo-trans
category: expression
description: SOAPdenovo-Trans is a de novo transcriptome assembler basing on the SOAPdenovo framework, adapt to alternative splicing and different expression level among transcripts.
tags: [soapdenovo-trans, expression]
author: oxo-call-community
source_url: "https://github.com/aquaskyline/SOAPdenovo-Trans/blob/1.0.5/README.md"
---

## Concepts

- **Tool Overview**: soapdenovo-trans (v1.04) - SOAPdenovo-Trans is a de novo transcriptome assembler basing on the SOAPdenovo framework, adapt to alternative splicing and different expression level among transcripts.
- **Core Function**: SOAPdenovo-Trans is a de novo transcriptome assembler basing on the SOAPdenovo framework, adapt to alternative splicing and different expression level among transcripts.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda soapdenovo-trans`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `soapdenovo-trans -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run soapdenovo-trans with typical input and output options.
