---
name: mgems
category: utility
description: mGEMS - sequencing data binning based on probabilistic classification
tags: [mgems, utility, binning]
author: oxo-call-community
source_url: "https://github.com/PROBIC/mGEMS"
---

## Concepts

- **Tool Overview**: mGEMS v1.3.3 is a sequencing data binning tool based on probabilistic classification.
- **Core Function**: Bins sequencing reads into taxonomic groups.
- **Probabilistic Binning**: Uses probabilistic models for classification.
- **Taxonomic Classification**: Assigns reads to taxonomic groups.
- **Input/Output**: Accepts sequencing reads; outputs taxonomic assignments.
- **Metagenomic Analysis**: Optimized for metagenomic data analysis.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal binning.
- **Data Quality**: Classification accuracy depends on input data quality.
- **Reference Database**: Requires comprehensive reference database.
- **Runtime**: Binning large datasets can be time-consuming.

## Examples

### Bin sequencing reads
**Args:** `mgems -i reads.fastq -o bins.txt`
**Explanation:** Bins sequencing reads into taxonomic groups.

### With custom database
**Args:** `mgems -i reads.fastq -d database/ -o bins.txt`
**Explanation:** Uses custom reference database.

### Paired-end analysis
**Args:** `mgems -i reads_1.fastq -r reads_2.fastq -o bins.txt`
**Explanation:** Processes paired-end sequencing data.

### Generate report
**Args:** `mgems -i reads.fastq -o bins.txt -r report.html`
**Explanation:** Generates detailed binning report.

### Batch processing
**Args:** `mgems -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.