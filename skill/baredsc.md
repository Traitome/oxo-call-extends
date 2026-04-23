---
name: baredsc
category: expression
description: baredSC (Bayesian Approach to Retreive Expression Distribution of Single Cell) is a tool that uses a Monte-Carlo Markov Chain to estimate a confidence interval on the probability density function (PDF) of expression of one or two genes from single-cell RNA-seq data.
tags: [baredsc, expression]
author: oxo-call-community
source_url: "https://github.com/lldelisle/baredSC/"
---

## Concepts

- **Tool Overview**: baredsc (v1.1.3) - baredSC (Bayesian Approach to Retreive Expression Distribution of Single Cell) is a tool that uses a Monte-Carlo Markov Chain to estimate a confidence interval on the probability density function (PDF) of expression of one or two genes from single-cell RNA-seq data.
- **Core Function**: baredSC (Bayesian Approach to Retreive Expression Distribution of Single Cell) is a tool that uses a Monte-Carlo Markov Chain to estimate a confidence interval on the probability density function (PDF) of expression of one or two genes from single-cell RNA-seq data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda baredsc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
