---
name: chanjo
category: sequencing
description: Coverage analysis tool for clinical sequencing data
tags: [chanjo, coverage, sequencing, clinical, bioinformatics]
author: oxo-call-community
source_url: "https://chanjo.readthedocs.io"
---

## Concepts

- **Tool Overview**: Chanjo is a coverage analysis tool designed for clinical sequencing data to assess sequencing coverage across target regions.
- **Core Function**: Calculates and reports sequencing coverage statistics for genomic regions of interest.
- **Features**: Coverage calculation, gene-level statistics, threshold-based reporting, and visualization.
- **Input**: BAM alignment files and BED target region files.
- **Output**: Coverage reports, statistics tables, and visualization files.
- **Application**: Clinical sequencing quality control and coverage assessment.
- **Installation**: Install via bioconda: `conda install -c bioconda chanjo`

## Pitfalls

- **Alignment Quality**: Requires properly aligned BAM files.
- **Target Regions**: BED file must define regions of interest correctly.
- **Memory Usage**: Large BAM files may require significant memory.
- **Threshold Settings**: Coverage thresholds affect reporting results.

## Examples

### Calculate coverage
**Args:** `chanjo calculate -b alignments.bam -t targets.bed -o coverage.tsv`
**Explanation:** Calculates coverage for target regions.

### Generate report
**Args:** `chanjo report -i coverage.tsv -o report.html`
**Explanation:** Generates HTML coverage report.

### Summarize by gene
**Args:** `chanjo summarize -i coverage.tsv -g genes.bed -o gene_summary.tsv`
**Explanation:** Summarizes coverage at gene level.

### Display help
**Args:** `chanjo --help`
**Explanation:** Shows all available options and usage information.