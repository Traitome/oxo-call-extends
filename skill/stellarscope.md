---
name: stellarscope
category: rna-seq
description: Single-cell Transposable Element Locus Level Analysis of scRNA Sequencing.
tags: [stellarscope, transposable-elements, scRNA-seq, single-cell]
author: oxo-call-community
source_url: "https://github.com/nixonlab/stellarscope/blob/1.5/docs/protocol.md"
---

## Concepts

- **Tool Overview**: stellarscope (v1.5) is a tool for analyzing transposable element (TE) expression at locus level in single-cell RNA sequencing data.
- **Core Function**: Identifies and quantifies TE expression at individual loci across single cells.
- **Algorithm**: Uses unique molecular identifiers (UMIs) to count TE expression at specific genomic loci.
- **Input/Output**: Input: scRNA-seq BAM file, TE annotation; Output: TE expression matrix at locus resolution.
- **Applications**: Studying TE expression dynamics in development, cancer, and cell differentiation.
- **Installation**: `conda install -c bioconda stellarscope` or download from GitHub.

## Pitfalls

- **UMI Quality**: Poor UMI design affects quantification accuracy.
- **TE Annotation**: Outdated or incomplete TE annotations miss loci.
- **Mapping Quality**: Low-quality mappings produce false positives.
- **Memory Requirements**: Large scRNA-seq datasets require significant memory.
- **Cell Filtering**: Poor quality cells affect downstream analysis.
- **Batch Effects**: Batch effects between samples affect comparison.

## Examples

### Display help
**Args:** `stellarscope --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `stellarscope -i aligned.bam -t te_annotations.gtf -o results/`
**Explanation:** Analyze TE expression at locus level from scRNA-seq data.

### With UMI correction
**Args:** `stellarscope -i aligned.bam -t te_annotations.gtf -o results/ --umi-correct`
**Explanation:** Apply UMI-based deduplication for accurate counting.

### Cell filtering
**Args:** `stellarscope -i aligned.bam -t te_annotations.gtf -o results/ -m 1000`
**Explanation:** Filter cells with fewer than 1000 UMIs.

### Verbose mode
**Args:** `stellarscope -i aligned.bam -t te_annotations.gtf -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `stellarscope -i aligned.bam -t te_annotations.gtf -o results/ --plot`
**Explanation:** Generate visualization of TE expression patterns.

### Custom TE database
**Args:** `stellarscope -i aligned.bam -t custom_te.gtf -o results/`
**Explanation:** Use custom TE annotation file.

### Batch processing
**Args:** `stellarscope -i batch/ -t te_annotations.gtf -o results/`
**Explanation:** Process multiple samples in batch mode.

### Generate report
**Args:** `stellarscope -i aligned.bam -t te_annotations.gtf -o results/ --report`
**Explanation:** Generate comprehensive HTML report.
