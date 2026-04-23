---
name: metaprob
category: expression
description: assembly-assisted tool for un-supervised metagenomic binning
tags: [metaprob, expression]
author: oxo-call-community
source_url: "https://bitbucket.org/samu661/metaprob/"
---

## Concepts

- **Tool Overview**: metaprob v2 - MetaProb is a novel assembly-assisted tool for un-supervised metagenomic binning. The novelty of MetaProb derives from solving a few important problems: how to divide reads into groups of independent reads, so that l-mer frequencies are not overestimated; how to convert l-mer counts into probabilistic sequence signatures, that will correct for variable distribution of l-mers, and for unbalanced groups of reads, in order to produce better estimates of the underlying genome statistic. We show that MetaProb is effective for both simulated and real datasets. It can accurately (with F-measures of 87 for short reads and 97 long reads) and efficiently bin short and long reads with varying abundance ratios..
- **Core Function**: assembly-assisted tool for un-supervised metagenomic binning
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metaprob`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
