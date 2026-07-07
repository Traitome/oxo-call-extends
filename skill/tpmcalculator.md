---
name: tpmcalculator
category: analysis
description: TPMcalculator - Tool for calculating Transcripts Per Million (TPM).
tags: [tpmcalculator, tpm, gene-expression, rna-seq, quantification]
author: oxo-call-community
source_url: "https://github.com/compbio/tpmcalculator"
---

## Concepts

- **Tool Overview**: TPMcalculator - A tool for calculating Transcripts Per Million (TPM) from RNA-seq data.
- **Core Function**: Computes TPM values for gene expression quantification.
- **Input**: Read counts, gene lengths, annotation files.
- **Output**: TPM values, expression matrices, statistics.
- **Installation**: `pip install tpmcalculator` or `conda install -c bioconda tpmcalculator`
- **Use Case**: Gene expression analysis, RNA-seq quantification, differential expression.

## Pitfalls

- **Gene Length**: Accurate gene lengths are essential for correct TPM calculation.
- **Normalization**: Requires proper normalization of raw counts.

## Examples

### Calculate TPM
**Args:** `tpmcalculator -i counts.txt -l gene_lengths.txt -o tpm_results/`
**Explanation:** Calculate TPM values from read counts.

### With RNA-seq data
**Args:** `tpmcalculator -b rnaseq.bam -a annotations.gtf -o tpm/`
**Explanation:** Calculate TPM directly from BAM file.
