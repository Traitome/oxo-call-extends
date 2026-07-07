---
name: fba
category: expression
description: "Tools for single-cell feature barcoding analysis. Citation: Duan, et al (2021) <doi:10.1093/bioinformatics/btab375>."
tags: [fba, expression, single-cell, feature-barcoding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jlduan/fba"
---

## Concepts

- **Tool Overview**: fba is a flexible toolbox for single-cell feature barcoding analysis, including quality control, quantification, and demultiplexing.
- **Core Function**: Performs quality control, quantification, and demultiplexing of single-cell feature barcoding assays.
- **Input/Output**: Input: Single-cell sequencing data. Output: Feature counts, demultiplexing results, QC reports.
- **Algorithm**: Implements feature barcoding analysis algorithms for single-cell data.
- **Key Features**: Flexible analysis, CRISPR construct support, targeted enrichment, customizable parameters, quality control module.
- **Installation**: `conda install -c bioconda fba`

## Pitfalls

- **Data Quality**: Requires high-quality single-cell data.
- **Barcode Design**: Results depend on barcode design quality.
- **Memory Usage**: Large datasets may require significant memory.
- **Demultiplexing**: May require careful parameter tuning.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic analysis
**Args:** `fba count -i data/ -o results/`
**Explanation:** Performs basic feature barcoding analysis.

### Quality control
**Args:** `fba qc -i data/ -o qc_report/`
**Explanation:** Generates quality control report.

### Demultiplexing
**Args:** `fba demux -i data/ -o results/ -c config.json`
**Explanation:** Demultiplexes single-cell data.

### CRISPR analysis
**Args:** `fba crispr -i data/ -o results/ --guideRNAs guides.txt`
**Explanation:** Analyzes CRISPR perturbations.

### Custom parameters
**Args:** `fba count -i data/ -o results/ -p params.json`
**Explanation:** Uses custom analysis parameters.