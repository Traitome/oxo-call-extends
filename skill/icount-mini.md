---
name: icount-mini
category: bioinformatics
description: Lightweight computational pipeline for analysis of iCLIP data.
tags: [icount-mini, bioinformatics, iCLIP, RNA-binding, peaks]
author: oxo-call-community
source_url: "https://github.com/ulelab/iCount-Mini"
---

## Concepts

- **Tool Overview**: iCount-Mini (v4.0.0) is a lightweight version of iCount for processing iCLIP sequencing data with a focus on peak calling.
- **Peak Detection**: Specializes in identifying significant cross-link sites from iCLIP data.
- **BED Format Support**: Works with BED files for cross-link site quantification.
- **Dependencies**: Requires bedtools, cutadapt, pandas, and pysam for data processing.
- **nf-core Integration**: Available as a module in the nf-core/clipseq pipeline.
- **Installation**: `conda install -c bioconda icount-mini`

## Pitfalls

- **Input Requirements**: Requires pre-processed BED files of crosslinks.
- **Reference Dependencies**: Results depend on the quality of input annotation files.
- **Threshold Sensitivity**: Peak calling parameters may need adjustment for different datasets.
- **Memory Usage**: Large datasets may require significant memory resources.
- **Annotation Quality**: Accurate gene annotations are essential for meaningful results.
- **Barcode Collision**: Rare barcode collisions can affect quantification accuracy.

## Examples

### Call peaks from crosslinks
**Args:** `icount-mini peaks crosslinks.bed sigxls.tsv peaks.bed`
**Explanation:** Identifies significant cross-link peaks from BED file.

### Cluster significant sites
**Args:** `icount-mini clusters peaks.bed clusters.bed`
**Explanation:** Groups significant cross-link sites into clusters.

### Annotate peaks
**Args:** `icount-mini annotate peaks.bed genes.gtf annotated_peaks.tsv`
**Explanation:** Annotates peaks with gene information from GTF file.

### Generate summary statistics
**Args:** `icount-mini stats peaks.bed genes.gtf stats.json`
**Explanation:** Produces summary statistics for the iCLIP experiment.

### Filter peaks by score
**Args:** `icount-mini filter peaks.bed --min-score 5.0 filtered_peaks.bed`
**Explanation:** Filters peaks to include only those with score >= 5.0.