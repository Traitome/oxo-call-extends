---
name: tssar
category: analysis
description: TSSAR - Tool for analyzing transcription start sites.
tags: [tssar, transcription-start-site, rna-seq, gene-expression, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/tssar"
---

## Concepts

- **Tool Overview**: TSSAR - A tool for identifying and analyzing transcription start sites from sequencing data.
- **Core Function**: Identifies TSS positions, quantifies expression, and analyzes promoter regions.
- **Input**: RNA-seq reads (FASTQ/BAM), gene annotations.
- **Output**: TSS coordinates, expression levels, promoter analysis.
- **Installation**: `pip install tssar` or `conda install -c bioconda tssar`
- **Use Case**: Gene expression analysis, promoter identification, transcription regulation.

## Pitfalls

- **Strand Specificity**: Requires strand-specific library preparation.
- **Annotation Quality**: Results depend on gene annotation quality.

## Examples

### Identify TSS
**Args:** `tssar -i rnaseq.bam -a genes.gtf -o tss_results/`
**Explanation:** Identify transcription start sites from RNA-seq data.

### Promoter analysis
**Args:** `tssar promoter -i tss.txt -o promoters/`
**Explanation:** Analyze promoter regions around TSS.
