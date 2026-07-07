---
name: baredsc
category: expression
description: baredSC - Bayesian Approach to Retrieve Expression Distribution of Single Cell RNA-seq data
tags: [baredsc, expression, single-cell, RNA-seq, Bayesian, MCMC]
author: oxo-call-community
source_url: "https://github.com/lldelisle/baredSC/"
---

## Concepts

- **Tool Overview**: baredSC (v1.1.3) is a Bayesian tool that uses Monte-Carlo Markov Chain (MCMC) to estimate confidence intervals on the probability density function (PDF) of gene expression from single-cell RNA-seq data.
- **Core Function**: Estimates expression distribution PDFs and their confidence intervals for single or pairs of genes from scRNA-seq data.
- **Bayesian Inference**: Uses MCMC sampling to infer posterior distributions of expression parameters.
- **Single Gene Analysis**: Analyzes expression distribution of individual genes.
- **Gene Pair Analysis**: Investigates co-expression relationships between pairs of genes.
- **Input/Output**: Accepts scRNA-seq count matrices; outputs PDF estimates and confidence intervals.
- **Installation**: `conda install -c bioconda baredsc`.

## Pitfalls

- **Convergence Check**: MCMC chains require convergence validation. Insufficient sampling may produce unreliable results.
- **Data Quality**: Requires high-quality scRNA-seq data with minimal dropout events.
- **Computational Time**: MCMC sampling can be computationally intensive for large datasets.
- **Memory Usage**: Large single-cell datasets may require substantial memory.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Analyze single gene expression
**Args:** `baredsc --input counts.csv --gene GeneX --output genex_distribution.pdf`
**Explanation:** Estimates expression PDF for single gene from count matrix.

### Analyze gene pair co-expression
**Args:** `baredsc --input counts.csv --gene GeneX --gene2 GeneY --output coexpression.pdf`
**Explanation:** Investigates co-expression relationship between two genes.

### Specify MCMC iterations
**Args:** `baredsc --input counts.csv --gene GeneX --iterations 10000 --output genex_distribution.pdf`
**Explanation:** Runs MCMC with specified number of iterations.

### Output confidence interval
**Args:** `baredsc --input counts.csv --gene GeneX --ci 95 --output genex_distribution.pdf`
**Explanation:** Computes 95% confidence interval for expression distribution.

### Multiple genes batch analysis
**Args:** `baredsc --input counts.csv --gene-list genes.txt --output-dir results/`
**Explanation:** Processes multiple genes in batch mode.

### Generate summary statistics
**Args:** `baredsc --input counts.csv --gene GeneX --stats --output stats.txt`
**Explanation:** Outputs summary statistics alongside visualization.

### Display help
**Args:** `baredsc --help`
**Explanation:** Shows all available command-line options and usage information.