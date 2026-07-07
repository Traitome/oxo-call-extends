---
name: cartools
category: qc
description: Coverage Analysis Report tool for assessment of per-base quality of NGS data
tags: [cartools, qc, coverage, ngs, quality-control]
author: oxo-call-community
source_url: "https://github.com/clinical-genomics-uppsala/CARtool/blob/master/README.md"
---

## Concepts

- **Tool Overview**: CARtools generates coverage analysis reports for NGS data quality assessment.
- **Core Function**: Evaluates per-base quality metrics and coverage statistics for sequencing data.
- **Input**: BAM/SAM alignment files and VCF variant files.
- **Output**: HTML quality report with coverage statistics and visualizations.
- **Features**: Coverage depth, uniformity, and variant assessment.
- **Application**: NGS data quality control and coverage validation.
- **Installation**: Install via bioconda: `conda install -c bioconda cartools`

## Pitfalls

- **BAM Required**: Requires sorted and indexed BAM file.
- **Reference Match**: Must use matching reference genome.
- **Memory Usage**: Large datasets require significant memory.
- **Report Generation**: HTML report generation may take time for large data.

## Examples

### Generate coverage report
**Args:** `CARtool -b aligned.bam -v variants.vcf -o qc_report/`
**Explanation:** Generates coverage analysis report from BAM and VCF files.

### With target regions
**Args:** `CARtool -b aligned.bam -t targets.bed -o qc_report/`
**Explanation:** Generates report focusing on specific target regions.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.