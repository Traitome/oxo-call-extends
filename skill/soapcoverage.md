---
name: soapcoverage
category: utility
description: SOAPcoverarge can calculate sequencing coverage or physical coverage as well as duplication rate and details of specific block for each segments and whole genome by using SOAP, BLAT, BLAST, BlastZ, mum- mer and MAQ aligement results with multi-thread.
tags: [soapcoverage, utility]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapaligner.html"
---

## Concepts

- **Tool Overview**: soapcoverage (v2.7.7) - SOAPcoverarge can calculate sequencing coverage or physical coverage as well as duplication rate and details of specific block for each segments and whole genome by using SOAP, BLAT, BLAST, BlastZ, mum- mer and MAQ aligement results with multi-thread.
- **Core Function**: SOAPcoverarge can calculate sequencing coverage or physical coverage as well as duplication rate and details of specific block for each segments and whole genome by using SOAP, BLAT, BLAST, BlastZ, mum- mer and MAQ aligement results with multi-thread.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda soapcoverage`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `soapcoverage -i <input_file> -o <output_file>`
**Explanation:** Run soapcoverage with typical input and output options.
