---
name: juicebox_scripts
category: formatting
description: A collection of scripts for working with Hi-C data, Juicebox, and other genomic file formats.
tags: [juicebox_scripts, formatting, Hi-C, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/phasegenomics/juicebox_scripts"
---

## Concepts

- **Tool Overview**: juicebox_scripts (v0.1.0) - A collection of scripts for processing and manipulating Hi-C data and Juicebox-related file formats.
- **Hi-C Data Processing**: Handles Hi-C sequencing data processing and analysis.
- **File Format Conversion**: Converts between different Hi-C data formats.
- **Quality Control**: Provides QC metrics for Hi-C experiments.
- **Data Filtering**: Filters and processes Hi-C contact maps.
- **Integration**: Works with Juicebox visualization software.

## Pitfalls

- **File Size**: Hi-C files can be extremely large.
- **Memory Requirements**: Processing large Hi-C datasets requires significant memory.
- **Format Compatibility**: Different Hi-C formats may not be compatible.
- **Mapping Quality**: Poorly mapped reads can affect results.
- **Normalization**: Different normalization methods can affect downstream analysis.
- **Chromosome Naming**: Inconsistent chromosome naming can cause issues.

## Examples

### Convert Hi-C file format
**Args:** `juicebox_scripts convert --input hic.hic --output hic.cool`
**Explanation:** Converts Hi-C file from .hic to .cool format.

### Filter contacts by distance
**Args:** `juicebox_scripts filter --input hic.hic --min-dist 10000 --output filtered.hic`
**Explanation:** Filters contacts with minimum distance of 10kb.

### Extract specific chromosomes
**Args:** `juicebox_scripts extract --input hic.hic --chr chr1 chr2 --output subset.hic`
**Explanation:** Extracts contacts involving specified chromosomes.

### Generate QC report
**Args:** `juicebox_scripts qc --input hic.hic --output qc_report.html`
**Explanation:** Generates quality control report for Hi-C data.

### Merge multiple Hi-C files
**Args:** `juicebox_scripts merge --input file1.hic file2.hic --output merged.hic`
**Explanation:** Merges multiple Hi-C files into one.

### Downsample Hi-C data
**Args:** `juicebox_scripts downsample --input hic.hic --fraction 0.5 --output downsampled.hic`
**Explanation:** Downsamples Hi-C data to 50% of original contacts.