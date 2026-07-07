---
name: tecount
category: analysis
description: TE-Count - Quantification tool for transposable element expression from RNA-seq data.
tags: [te-count, transposable-element, expression, rna-seq, quantification, te-expression]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/te-count"
---

## Concepts

- **Tool Overview**: TE-Count - A tool for quantifying transposable element expression from RNA-seq data.
- **Core Function**: Counts reads mapping to transposable elements to measure TE-derived transcription levels.
- **Input**: RNA-seq alignments (BAM files) and TE annotation database.
- **Output**: Read counts per TE family/element, expression matrices for downstream analysis.
- **Installation**: `pip install te-count` or `conda install -c bioconda te-count`
- **Use Case**: Studying TE expression in diseases, embryonic development, or stress responses where TEs become transcriptionally active.

## Pitfalls

- **TE Annotation Required**: Requires comprehensive TE annotation as input.
- **Multi-mapping Reads**: TE copies are nearly identical - handling of multi-mapping reads affects counts.
- **Background Noise**: TEs have evolutionary older copies - distinguish recent vs ancient TE activity.

## Examples

### Count TE expression
**Args:** `te-count -b aligned.bam -a te_annotation.gtf -o te_counts.tsv`
**Explanation:** Quantify TE expression from RNA-seq alignments using provided TE annotation.

### Normalized counts
**Args:** `te-count -b sample.bam -a te.gtf --normalize -o normalized_counts.tsv`
**Explanation:** Output normalized expression values (RPKM/TPM) instead of raw counts.

### Paired-end mode
**Args:** `te-count -b pe_aligned.bam -a te_annotation.gtf -o results/`
**Explanation:** Process paired-end RNA-seq data for more accurate TE quantification.
