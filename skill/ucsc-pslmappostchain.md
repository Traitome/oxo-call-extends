---
name: ucsc-pslmappostchain
category: alignment
description: Post genomic pslMap (TransMap) chaining. This takes transcripts that have been mapped via genomic chains adds back in blocks that didn't get include in genomic chains due to complex rearrangements or other issues.
tags: [ucsc-pslmappostchain, alignment]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-pslmappostchain (v482) - Post genomic pslMap (TransMap) chaining. This takes transcripts that have been mapped via genomic chains adds back in blocks that didn't get include in genomic chains due to complex rearrangements or other issues.
- **Core Function**: Post genomic pslMap (TransMap) chaining. This takes transcripts that have been mapped via genomic chains adds back in blocks that didn't get include in genomic chains due to complex rearrangements or other issues.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-pslmappostchain`

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
