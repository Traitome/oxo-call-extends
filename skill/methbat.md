---
name: methbat
category: epigenomics
description: A battery of methylation tools for PacBio HiFi reads
tags: [methbat, epigenomics, methylation]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/MethBat"
---

## Concepts

- **Tool Overview**: MethBat v0.17.0 is a collection of methylation analysis tools specifically designed for PacBio HiFi sequencing reads.
- **Core Function**: Analyzes DNA methylation patterns from PacBio HiFi sequencing data.
- **PacBio Optimization**: Optimized for PacBio HiFi sequencing technology.
- **Methylation Detection**: Detects and quantifies DNA methylation at single-molecule resolution.
- **Input/Output**: Accepts PacBio HiFi reads; outputs methylation calls and statistics.
- **Multi-step Analysis**: Includes methylation calling, filtering, and visualization.

## Pitfalls

- **PacBio Specific**: Designed specifically for PacBio HiFi data.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input read quality.
- **Runtime**: Analysis of large datasets can be time-consuming.

## Examples

### Call methylation
**Args:** `methbat call -i reads.bam -o methylation.txt`
**Explanation:** Calls methylation from PacBio HiFi reads.

### With reference genome
**Args:** `methbat call -i reads.bam -r reference.fasta -o methylation.txt`
**Explanation:** Uses reference genome for methylation calling.

### Filter methylation calls
**Args:** `methbat filter -i methylation.txt -o filtered.txt -q 30`
**Explanation:** Filters methylation calls by quality score 30.

### Generate report
**Args:** `methbat report -i methylation.txt -o report.html`
**Explanation:** Generates methylation analysis report.

### Batch processing
**Args:** `methbat batch -i bam/ -o methylation/`
**Explanation:** Processes multiple BAM files in batch mode.