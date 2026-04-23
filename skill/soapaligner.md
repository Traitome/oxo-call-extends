---
name: soapaligner
category: alignment
description: SOAPaligner/soap2 is an updated version of SOAP software for short oligonucleotide alignment.
tags: [soapaligner, alignment]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapaligner.html"
---

## Concepts

- **Tool Overview**: soapaligner (v2.21) - SOAPaligner/soap2 is an updated version of SOAP software for short oligonucleotide alignment.
- **Core Function**: SOAPaligner/soap2 is an updated version of SOAP software for short oligonucleotide alignment.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda soapaligner`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `soapaligner -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run soapaligner with typical input and output options.
