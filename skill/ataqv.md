---
name: ataqv
category: qc
description: ataqv - Measure, visualize, and compare ATAC-seq quality metrics across samples and experiments
tags: [atac-seq, quality-control, chromatin-accessibility, visualization, metrics]
author: oxo-call-community
source_url: "https://github.com/ParkerLab/ataqv"
---

## Concepts

- **Tool Overview**: ataqv measures and compares ATAC-seq quality control results across samples and experiments. Helps understand assay performance and identify technical issues. Version 1.3.1.
- **Comprehensive Metrics**: Calculates multiple QC metrics: fragment size distribution, TSS enrichment, nucleosome positioning, mitochondrial contamination, and more.
- **Visualization**: Generates interactive HTML reports with plots for all metrics. Easy comparison across multiple samples.
- **Standard Metrics**: Implements standard ATAC-seq QC metrics from literature. Enables comparison with published benchmarks.
- **Bias Detection**: Identifies technical biases in ATAC-seq data. Helps troubleshoot library prep and sequencing issues.
- **Batch Comparison**: Compares metrics across experimental batches. Detects batch effects before downstream analysis.
- **Reference Data**: Includes reference datasets for comparison. Helps assess if samples meet quality standards.

## Pitfalls

- **Alignment Quality**: Requires properly aligned BAM files. Poor alignments produce misleading metrics.
- **Reference Genome**: Must use same reference genome for all samples in comparison. Mismatched references cause errors.
- **Sample Size**: Large sample collections (>100) may slow down report generation. Consider subset analysis.
- **TSS Annotation**: Requires TSS annotation file matching reference genome. Missing annotations cause errors.
- **Mitochondrial Reads**: High mitochondrial contamination (>50%) indicates poor library quality. May need protocol optimization.
- **Fragment Size**: Unusual fragment size distributions may indicate protocol issues. Verify library prep.

## Examples

### Basic ATAC-seq QC
**Args:** `ataqv --species human --bam aligned.bam --output results/ sample_name`
**Explanation:** Calculates ATAC-seq QC metrics from BAM file. Species "human" for appropriate TSS annotations. Outputs metrics and HTML report.

### Compare multiple samples
**Args:** `ataqv --species mouse --bam sample1.bam sample2.bam sample3.bam --output comparison/ project_name`
**Explanation:** Processes multiple BAM files and generates comparative report. All samples in single HTML for easy comparison.

### Specify TSS annotation file
**Args:** `ataqv --species human --tss tss_annotations.bed --bam aligned.bam --output results/ sample_name`
**Explanation:** Uses custom TSS annotation file instead of built-in annotations. Required for non-standard genomes or annotation versions.

### Set fragment size range
**Args:** `ataqv --species human --min-fragment-size 50 --max-fragment-size 1000 --bam aligned.bam --output results/ sample_name`
**Explanation:** Filters fragments to 50-1000bp range. Removes very short and very long fragments that may be artifacts.

### Generate metrics file only
**Args:** `ataqv --species human --bam aligned.bam --output results/ --no-report sample_name`
**Explanation:** Outputs metrics in TSV format without HTML report. Useful for automated pipelines or large-scale analyses.

### Filter low-quality reads
**Args:** `ataqv --species human --min-mapping-quality 30 --bam aligned.bam --output results/ sample_name`
**Explanation:** Uses only reads with mapping quality ≥30. Filters low-quality alignments that may bias metrics.

### Compare with reference data
**Args:** `ataqv --species human --bam aligned.bam --output results/ --reference-data reference_metrics.tsv sample_name`
**Explanation:** Compares sample metrics against reference dataset. Highlights samples deviating from expected quality ranges.

### Output JSON format
**Args:** `ataqv --species human --bam aligned.bam --output results/ --format json sample_name`
**Explanation:** Outputs metrics in JSON format. Easier to parse programmatically for downstream analysis pipelines.