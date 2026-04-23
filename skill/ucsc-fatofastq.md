---
name: ucsc-fatofastq
category: qc
description: Convert fa to fastq format, just faking quality values.
tags: [ucsc-fatofastq, qc, fastq]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-fatofastq (v482) - Convert fa to fastq format, just faking quality values.
- **Core Function**: Convert fa to fastq format, just faking quality values.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-fatofastq`

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
