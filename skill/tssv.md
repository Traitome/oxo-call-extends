---
name: tssv
category: analysis
description: TSSV - Tool for detecting tissue-specific splice variants.
tags: [tssv, alternative-splicing, rna-seq, gene-expression, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/tssv"
---

## Concepts

- **Tool Overview**: TSSV - A tool for detecting tissue-specific splice variants from RNA-seq data.
- **Core Function**: Identifies splice variants that show tissue-specific expression patterns.
- **Input**: RNA-seq data from multiple tissues, gene annotations.
- **Output**: Tissue-specific splice variants, expression patterns, differential splicing.
- **Installation**: `pip install tssv` or `conda install -c bioconda tssv`
- **Use Case**: Alternative splicing analysis, gene expression, transcriptomics.

## Pitfalls

- **Multiple Samples**: Requires data from multiple tissues.
- **Expression Levels**: Requires sufficient expression for detection.

## Examples

### Detect tissue-specific variants
**Args:** `tssv -i rnaseq/ -a genes.gtf -o tissue_variants/`
**Explanation:** Detect tissue-specific splice variants.

### Differential splicing
**Args:** `tssv diff -i samples/ -o diff_splicing.txt`
**Explanation:** Identify differential splicing events.
