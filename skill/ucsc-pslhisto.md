---
name: ucsc-pslhisto
category: alignment
description: Collect counts on PSL alignments for making histograms. These then be analyzed with R, textHistogram, etc.
tags: [ucsc-pslhisto, alignment]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-pslhisto (v482) - Collect counts on PSL alignments for making histograms. These then be analyzed with R, textHistogram, etc.
- **Core Function**: Collect counts on PSL alignments for making histograms. These then be analyzed with R, textHistogram, etc.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-pslhisto`

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
