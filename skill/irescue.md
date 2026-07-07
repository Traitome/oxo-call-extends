---
name: irescue
category: expression
description: Uncertainty-aware quantification of transposable elements expression in scRNA-seq
tags: [irescue, expression, scRNA-seq, transposable-elements, TE-quantification]
author: oxo-call-community
source_url: "https://github.com/bodegalab/irescue"
---

## Concepts

- **Tool Overview**: IRescue is a Python tool for uncertainty-aware quantification of transposable elements (TEs) expression in single-cell RNA sequencing (scRNA-seq) data.
- **Core Function**: Performs UMI deduplication with sequencing error correction and uses Expectation-Maximization (EM) to probabilistically assign multi-mapping reads to TE subfamilies.
- **Input/Output**: Accepts BAM files with aligned reads and outputs sparse count matrices compatible with Seurat and Scanpy.
- **Installation**: `conda create -n irescue -c conda-forge -c bioconda irescue` or `pip install irescue`
- **TE Annotation**: Requires TE annotation files (RepeatMasker output or custom BED files) for accurate quantification.
- **UMI Handling**: Supports both UMI-based (10X Genomics) and UMI-less (SMART-seq) library protocols.

## Pitfalls

- **Multi-Mapping Reads**: TE sequences are often highly similar, leading to ambiguous read mapping that requires careful handling.
- **UMI Quality**: Low-quality UMIs or sequencing errors can affect deduplication accuracy.
- **Annotation Completeness**: Incomplete TE annotations may miss certain TE families, affecting quantification.
- **Memory Requirements**: Processing large scRNA-seq datasets requires significant memory resources.
- **Batch Effects**: Technical variation between batches can affect TE expression profiles.
- **Reference Genome**: TE quantification depends on the reference genome version and its TE annotation.

## Examples

### Basic TE quantification
**Args:** `irescue --bam input.bam --outdir results/ --genome hg38`
**Explanation:** Quantifies TE expression from aligned scRNA-seq reads using hg38 reference genome annotations.

### Custom TE annotation
**Args:** `irescue --bam cells.bam --outdir output/ --bed custom_repeats.bed`
**Explanation:** Uses a custom BED file containing TE genomic coordinates instead of built-in annotations.

### UMI-less libraries (SMART-seq)
**Args:** `irescue --bam smartseq.bam --outdir results/ --genome mm10 --no-umi`
**Explanation:** Processes SMART-seq data without UMI deduplication, performing read-level quantification instead.

### Specify number of EM iterations
**Args:** `irescue --bam input.bam --outdir output/ --genome hg38 --max-em-iter 50`
**Explanation:** Sets maximum Expectation-Maximization iterations to 50 for multi-mapping read assignment.

### Filter low-confidence assignments
**Args:** `irescue --bam cells.bam --outdir results/ --genome hg38 --min-confidence 0.8`
**Explanation:** Filters out TE assignments with confidence scores below 0.8, retaining only high-confidence mappings.

### Generate sparse matrix for Seurat
**Args:** `irescue --bam input.bam --outdir seurat_data/ --genome hg38 --format mtx`
**Explanation:** Outputs TE count matrix in Matrix Market format for direct import into Seurat.