---
name: methylartist
category: epigenomics
description: Tools for parsing and plotting nanopore methylation data.
tags: [methylartist, epigenomics, methylation]
author: oxo-call-community
source_url: "https://github.com/adamewing/methylartist"
---

## Concepts

- **Tool Overview**: MethylArtist v1.5.3 provides tools for parsing and visualizing nanopore methylation data.
- **Core Function**: Parses and plots methylation data from Oxford Nanopore sequencing.
- **Nanopore Specific**: Optimized for Oxford Nanopore sequencing data.
- **Visualization**: Generates visual representations of methylation patterns.
- **Input/Output**: Accepts nanopore sequencing reads; outputs methylation plots and statistics.
- **Single-molecule Resolution**: Enables visualization of methylation at single-molecule level.

## Pitfalls

- **Nanopore Specific**: Designed specifically for Nanopore data.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal visualization.
- **Data Quality**: Visualization quality depends on input data quality.
- **Runtime**: Processing large datasets can be time-consuming.

## Examples

### Parse nanopore methylation data
**Args:** `methylartist parse -i reads.fast5 -o methylation.txt`
**Explanation:** Parses methylation information from Nanopore reads.

### Generate methylation plot
**Args:** `methylartist plot -i methylation.txt -o plot.png`
**Explanation:** Generates visualization of methylation patterns.

### With reference genome
**Args:** `methylartist plot -i methylation.txt -r reference.fasta -o plot.png`
**Explanation:** Uses reference genome for coordinate-based plotting.

### Multiple samples
**Args:** `methylartist compare -i sample1.txt sample2.txt -o comparison.png`
**Explanation:** Compares methylation patterns across samples.

### Batch processing
**Args:** `methylartist batch -i fast5/ -o plots/`
**Explanation:** Processes multiple datasets in batch mode.