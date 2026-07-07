---
name: rigel
category: expression
description: Rigel performs Bayesian RNA-seq quantification with deconvolution.
tags: [rigel, expression, rna-seq, bayesian]
author: oxo-call-community
source_url: "https://github.com/mkiyer/rigel/blob/main/docs/MANUAL.md"
---

## Concepts

- **Tool Overview**: rigel quantifies RNA-seq.
- **Core Function**: Bayesian transcript quantification.
- **Algorithm**: Uses Bayesian methods.
- **Input Format**: Accepts RNA-seq data.
- **Output**: Produces expression estimates.
- **Use Case**: Gene expression analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Affects quantification.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rigel --help`
**Explanation:** Shows available options and usage instructions.

### Quantify transcripts
**Args:** `rigel quant -i rnaseq.bam -o quant.tsv`
**Explanation:** Performs Bayesian transcript quantification.

### With parameters
**Args:** `rigel quant -i rnaseq.bam -p params.yaml -o quant.tsv`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rigel -v quant -i rnaseq.bam -o quant.tsv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rigel -t 4 quant -i rnaseq.bam -o quant.tsv`
**Explanation:** Uses 4 threads for parallel processing.

### With annotation
**Args:** `rigel quant -i rnaseq.bam -a genes.gtf -o quant.tsv`
**Explanation:** Uses gene annotation.

### With deconvolution
**Args:** `rigel quant -i rnaseq.bam --deconvolve -o quant.tsv`
**Explanation:** Enables mRNA/nRNA/gDNA deconvolution.