---
name: methylpy
category: expression
description: Bisulfite sequencing data processing and differential methylation analysis
tags: [methylpy, expression, methylation]
author: oxo-call-community
source_url: "https://github.com/yupenghe/methylpy"
---

## Concepts

- **Tool Overview**: MethylPy v1.4.7 is a Python package for bisulfite sequencing data processing and differential methylation analysis.
- **Core Function**: Processes bisulfite sequencing data and performs differential methylation analysis.
- **Bisulfite Processing**: Handles quality control, alignment, and methylation calling.
- **Differential Analysis**: Identifies differentially methylated regions between samples.
- **Input/Output**: Accepts bisulfite sequencing reads; outputs methylation calls and differential analysis results.
- **Integrated Pipeline**: Combines multiple analysis steps into a single workflow.

## Pitfalls

- **Python Dependency**: Requires Python environment with specific dependencies.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input data quality.
- **Runtime**: Analysis of large bisulfite datasets can be time-consuming.

## Examples

### Run bisulfite processing
**Args:** `methylpy process -i reads.fastq -o methylation.txt`
**Explanation:** Processes bisulfite sequencing data and calls methylation.

### Differential methylation analysis
**Args:** `methylpy diff -i sample1.txt sample2.txt -o diff.txt`
**Explanation:** Identifies differentially methylated regions.

### With reference genome
**Args:** `methylpy process -i reads.fastq -r reference.fasta -o methylation.txt`
**Explanation:** Uses reference genome for mapping.

### Quality control
**Args:** `methylpy qc -i reads.fastq -o qc_report.txt`
**Explanation:** Performs quality control on bisulfite data.

### Batch processing
**Args:** `methylpy batch -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.