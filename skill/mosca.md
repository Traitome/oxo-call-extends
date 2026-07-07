---
name: mosca
category: metagenomics
description: MOSCA - Meta-Omics Software for Community Analysis
tags: [mosca, metagenomics, multi-omics]
author: oxo-call-community
source_url: "https://github.com/iquasere/MOSCA"
---

## Concepts

- **Tool Overview**: MOSCA v2.3.0 performs integrated meta-omics data analysis.
- **Core Function**: Integrates metagenomics, metatranscriptomics, and metaproteomics.
- **Multi-Omics Integration**: Combines MG, MT, and MP data for comprehensive analysis.
- **Automated Workflow**: Fully automated pipeline from raw data to results.
- **Annotation**: Uses UniProt and COG databases for functional annotation.
- **Input/Output**: Accepts sequencing data; outputs analysis results and reports.

## Pitfalls

- **Computational Resources**: Requires significant computational resources.
- **Memory Requirements**: Memory usage depends on dataset complexity.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Results depend on sequencing quality.
- **Database Dependence**: Requires UniProt and COG databases.
- **Runtime**: Complex workflows may take significant time.

## Examples

### Run complete pipeline
**Args:** `mosca -i reads.fastq -o results/`
**Explanation:** Runs integrated meta-omics analysis.

### Metagenomics only
**Args:** `mosca -i reads.fastq -m mg -o results/`
**Explanation:** Performs metagenomics analysis only.

### With metatranscriptomics
**Args:** `mosca -i reads.fastq -mt mt_reads.fastq -o results/`
**Explanation:** Integrates metagenomics and metatranscriptomics.

### With metaproteomics
**Args:** `mosca -i reads.fastq -mp spectra.mzML -o results/`
**Explanation:** Integrates metagenomics and metaproteomics.

### Generate report
**Args:** `mosca -i reads.fastq -r report.html -o results/`
**Explanation:** Generates analysis report.