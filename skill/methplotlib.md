---
name: methplotlib
category: epigenomics
description: Plot methylation data obtained from nanopolish
tags: [methplotlib, epigenomics, methylation, nanopore, visualization]
author: oxo-call-community
source_url: "https://github.com/wdecoster/methplotlib"
---

## Concepts

- **Tool Overview**: methplotlib v0.21.2 visualizes modified nucleotides from Oxford Nanopore Technologies sequencing.
- **Core Function**: Generates browser-based visualizations of methylation data from nanopolish output.
- **Input Formats**: Accepts nanopolish methylation calls, nanocompore, ont-cram (MM/ML tags), and bedgraph formats.
- **Output**: Creates interactive HTML visualization of per-position and per-read methylation frequencies.
- **Integration**: Works with Snakemake workflows for streamlined nanopore analysis pipelines.
- **Installation**: Available via PyPI (`pip install methplotlib`) and Bioconda (`conda install -c bioconda methplotlib`).

## Pitfalls

- **Data Quality**: Results depend heavily on basecalling quality and methylation detection accuracy.
- **Memory Usage**: Large datasets with many reads may require significant memory for visualization.
- **Coordinate Requirements**: The `--window` parameter must specify valid genomic coordinates.
- **Reference Dependencies**: Requires reference genome FASTA for chromosome-level windows.
- **Format Compatibility**: Input files must be in supported formats (nanopolish, nanocompore, ont-cram, bedgraph).
- **Browser Compatibility**: Interactive visualizations require a modern web browser.

## Examples

### Visualize methylation data
**Args:** `methplotlib -m methylation.tsv -n sample1 -w chr20:1-1000000`
**Explanation:** Creates HTML visualization of methylation data for a genomic region.

### Add gene annotation
**Args:** `methplotlib -m calls.tsv -n sample1 -w chr1:1-500000 -g annotation.gtf`
**Explanation:** Visualizes methylation with gene annotation track from GTF file.

### Split by strand
**Args:** `methplotlib -m meth.tsv -n sample1 -w chr1:1-1000000 --split`
**Explanation:** Generates separate tracks for forward and reverse strand methylation.

### Static image output
**Args:** `methplotlib -m meth.tsv -n sample1 -w chr1:1-500000 --static output.png`
**Explanation:** Exports a static PNG image instead of interactive HTML.

### Multiple samples comparison
**Args:** `methplotlib -m sample1.tsv sample2.tsv -n sample1 sample2 -w chr1:1-1000000`
**Explanation:** Overlays methylation data from two samples for comparative visualization.
