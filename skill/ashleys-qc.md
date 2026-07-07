---
name: ashleys-qc
category: qc
description: ASHLEYS-QC - Automated quality control for Strand-seq libraries
tags: [ashleys-qc, qc, strand-seq, library-quality, sequencing]
author: oxo-call-community
source_url: "https://github.com/friendsofstrandseq/ashleys-qc"
---

## Concepts

- **Tool Overview**: ASHLEYS-QC (Automated Selection of High quality Libraries for the Extensive analYsis of Strandseq data) performs automated quality control for Strand-seq sequencing libraries. Version 0.2.1.
- **Core Function**: Automatically assesses and selects high-quality Strand-seq libraries based on multiple quality metrics.
- **Strand-seq Specific**: Designed specifically for Strand-seq data analysis and quality assessment.
- **Quality Metrics**: Evaluates multiple metrics including strand purity, read quality, coverage uniformity, and library complexity.
- **Automated Selection**: Filters and selects high-quality libraries for downstream analysis.
- **Report Generation**: Generates comprehensive quality reports with visualizations.
- **Input/Output**: Accepts BAM files and outputs quality metrics and filtered library lists.
- **Installation**: `conda install -c bioconda ashleys-qc` or install from GitHub.

## Pitfalls

- **Strand-seq Data**: Designed specifically for Strand-seq data. May not work correctly with other sequencing types.
- **BAM Requirements**: Requires properly aligned and sorted BAM files. Poorly formatted BAMs cause errors.
- **Reference Genome**: Requires matching reference genome for proper quality assessment.
- **Library Complexity**: Low complexity libraries may fail quality thresholds. Consider library preparation.
- **Coverage Requirements**: Requires minimum coverage depth for reliable quality assessment.
- **Batch Effects**: Quality thresholds may need adjustment for different sequencing batches.

## Examples

### Display help
**Args:** `ashleys-qc --help`
**Explanation:** Shows all available command-line options and usage information.

### Run quality control
**Args:** `ashleys-qc --input sample1.bam sample2.bam sample3.bam --output qc_results/`
**Explanation:** Runs quality control on multiple Strand-seq libraries. Outputs results to specified directory.

### Set quality thresholds
**Args:** `ashleys-qc --input sample.bam --output qc_results/ --min_strand_purity 0.8 --min_coverage 10`
**Explanation:** Sets custom quality thresholds: minimum strand purity 80%, minimum coverage 10x.

### Generate report
**Args:** `ashleys-qc --input sample.bam --output qc_results/ --report report.html`
**Explanation:** Generates HTML quality report with visualizations of quality metrics.

### Filter libraries
**Args:** `ashleys-qc --input *.bam --output qc_results/ --filter high_quality.txt`
**Explanation:** Filters libraries based on quality metrics and outputs list of high-quality libraries.

### Specify reference genome
**Args:** `ashleys-qc --input sample.bam --output qc_results/ --reference genome.fasta`
**Explanation:** Specifies reference genome for quality assessment. Important for accurate metrics calculation.

### Multi-threaded processing
**Args:** `ashleys-qc --input *.bam --output qc_results/ -t 8`
**Explanation:** Uses 8 threads for parallel processing. Speeds up analysis for multiple samples.

### Compare with previous run
**Args:** `ashleys-qc --input sample.bam --output qc_results/ --compare previous_run/`
**Explanation:** Compares current quality metrics with previous QC run for consistency checks.