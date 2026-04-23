---
name: htstream
category: qc
description: "HTStream is a quality control and processing pipeline for High Throughput Sequencing data. The difference between HTStream and other tools is that HTStream uses a tab delimited fastq format that allows for streaming from application to application. This streaming creates some awesome efficiencies when processing HTS data and makes it fully interoperable with other standard Linux tools."
tags: [htstream, qc, FASTQ]
author: oxo-call-community
source_url: "https://s4hts.github.io/HTStream"
---

## Concepts

- **Tool Overview**: htstream (v1.4.1) - "HTStream is a quality control and processing pipeline for High Throughput Sequencing data. The difference between HTStream and other tools is that HTStream uses a tab delimited fastq format that allows for streaming from application to application. This streaming creates some awesome efficiencies when processing HTS data and makes it fully interoperable with other standard Linux tools."
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda htstream`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
