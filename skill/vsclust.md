---
name: vsclust
category: hpc
description: Interactive tool for statistical testing, data browsing and interactive visualization of quantitative omics data
tags: [vsclust, hpc]
author: oxo-call-community
source_url: "https://bitbucket.org/veitveit/vsclust/src/master/"
---

## Concepts

- **Tool Overview**: vsclust (v0.91) - VSClust is a web service (shiny app) and command-line tool for statistical testing, clustering and interactive visualization of quantitative omics data. Its variance-sensitive clustering algorithm improves identification of co-regulated features in noisy data with replicates
- **Core Function**: Interactive tool for statistical testing, data browsing and interactive visualization of quantitative omics data
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vsclust`

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
