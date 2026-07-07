---
name: methpipe
category: epigenomics
description: A pipeline for analyzing DNA methylation data from bisulfite sequencing.
tags: [methpipe, epigenomics, methylation]
author: oxo-call-community
source_url: "https://github.com/smithlabcode/methpipe"
---

## Concepts

- **Tool Overview**: MethPipe v5.0.1 is a comprehensive pipeline for analyzing DNA methylation data from bisulfite sequencing experiments.
- **Core Function**: Analyzes bisulfite sequencing data to identify and quantify DNA methylation patterns.
- **Bisulfite Sequencing**: Specialized for bisulfite-converted sequencing data analysis.
- **Methylation Calling**: Identifies methylated and unmethylated cytosines.
- **Input/Output**: Accepts aligned bisulfite sequencing reads; outputs methylation calls and statistics.
- **Multi-step Pipeline**: Includes quality control, alignment, methylation calling, and analysis.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Analysis of large bisulfite datasets can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input read quality.
- **Alignment Quality**: Methylation calling accuracy depends on alignment quality.

## Examples

### Run methylation analysis
**Args:** `methpipe -i reads.bam -o methylation.txt`
**Explanation:** Analyzes bisulfite sequencing data for methylation patterns.

### With reference genome
**Args:** `methpipe -i reads.bam -r reference.fasta -o methylation.txt`
**Explanation:** Uses reference genome for methylation calling.

### Quality control
**Args:** `methpipe qc -i reads.bam -o qc_report.txt`
**Explanation:** Performs quality control on bisulfite sequencing data.

### Differential methylation
**Args:** `methpipe diff -i sample1.txt sample2.txt -o diff.txt`
**Explanation:** Identifies differentially methylated regions.

### Batch processing
**Args:** `methpipe batch -i bam/ -o methylation/`
**Explanation:** Processes multiple samples in batch mode.