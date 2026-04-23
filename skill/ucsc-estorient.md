---
name: ucsc-estorient
category: expression
description: Read ESTs from a database and determine orientation based on estOrientInfo table or direction in gbCdnaInfo table.  Update PSLs so that the strand reflects the direction of transcription. By default, PSLs where the direction can't be determined are dropped.
tags: [ucsc-estorient, expression]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-estorient (v482) - Read ESTs from a database and determine orientation based on estOrientInfo table or direction in gbCdnaInfo table.  Update PSLs so that the strand reflects the direction of transcription. By default, PSLs where the direction can't be determined are dropped.
- **Core Function**: Read ESTs from a database and determine orientation based on estOrientInfo table or direction in gbCdnaInfo table.  Update PSLs so that the strand reflects the direction of transcription. By default, PSLs where the direction can't be determined are dropped.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-estorient`

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
