---
name: tidyp
category: qc
description: Program for cleaning up and validating HTML
tags: [tidyp, qc]
author: oxo-call-community
source_url: "http://www.tidyp.com/"
---

## Concepts

- **Tool Overview**: tidyp (v1.04) - Program for cleaning up and validating HTML
- **Core Function**: Program for cleaning up and validating HTML
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tidyp`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tidyp -i <input.fastq> -o <output_dir>`
**Explanation:** Run tidyp with typical input and output options.
