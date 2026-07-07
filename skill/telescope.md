---
name: telescope
category: analysis
description: Telescope - Computational tool for analyzing retrotransposon expression from RNA-seq data.
tags: [telescope, retrotransposon, te-expression, rna-seq, transposable-element, endogenous-retrovirus]
author: oxo-call-community
source_url: "https://github.com/skovaka/Telescope"
---

## Concepts

- **Tool Overview**: Telescope - A tool for quantifying retrotransposon expression and endogenous retrovirus (ERV) transcripts from RNA-seq data.
- **Core Function**: Disambiguates multi-mapping RNA-seq reads to their source retrotransposon loci, providing locus-specific expression quantification.
- **Input**: Aligned RNA-seq BAM files and a reference genome with annotated transposable elements.
- **Output**: Expression counts per TE locus, allele-specific counts, and expression matrices.
- **Installation**: `conda install -c bioconda telescope`
- **Use Case**: Studying retrotransposon and ERV expression in cancer, development, and aging.

## Pitfalls

- **TE Annotation Required**: Requires comprehensive TE locus annotation for accurate assignment.
- **Multi-mapping**: Handles multi-mapping reads but choice of assignment algorithm affects results.
- **Strand-specific**: Strand awareness may be needed for certain TE types.

## Examples

### Quantify TE expression
**Args:** `telescope assign -b aligned.bam -a te_annotation.gtf -o te_expression.tsv`
**Explanation:** Assign reads to TE loci and quantify expression.

### With stranded data
**Args:** `telescope assign -b aligned.bam -a te.gtf --stranded -o results.tsv`
**Explanation:** Process strand-specific RNA-seq data for accurate TE quantification.

### Generate report
**Args:** `telescope report -i te_expression.tsv -o report/`
**Explanation:** Generate summary report of TE expression across samples.
