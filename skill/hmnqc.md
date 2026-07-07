---
name: hmnqc
category: qc
description: HmnQc computes quality metrics, identity checks, and coverage statistics from targeted next-generation sequencing data.
tags: [hmnqc, quality-control, ngs, targeted-sequencing, coverage, qc-metrics]
author: oxo-call-community
source_url: "https://github.com/guillaume-gricourt/HmnQc"
---

## Concepts

- **Tool Overview**: HmnQc (v0.5.1) is a quality control tool for targeted next-generation sequencing (NGS) data. It computes comprehensive metrics to assess sequencing quality, sample identity, and target coverage.

- **Quality Metrics**: Calculates base quality scores, read length distribution, GC content, duplication rates, and adapter contamination levels.

- **Coverage Analysis**: Provides detailed coverage statistics including mean depth, minimum depth, coverage uniformity, and percentage of targets meeting coverage thresholds (e.g., ≥30x, ≥100x).

- **Identity Verification**: Checks sample identity through comparison of variant allele frequencies with expected genotypes or by detecting sample swaps using genetic markers.

- **Targeted Panel Assessment**: Evaluates panel performance metrics such as on-target rate, off-target distribution, and probe efficiency.

- **Report Generation**: Produces comprehensive HTML reports with visualizations of quality metrics for quick assessment of sequencing run quality.

## Pitfalls

- **BAM File Requirements**: Input BAM files must be sorted and indexed. Unsorted BAMs will produce incorrect coverage calculations.

- **Bed File Compatibility**: Target region BED files must use the same coordinate system as the aligned BAM (0-based vs 1-based).

- **Coverage Thresholds**: Default thresholds may not be appropriate for all applications. Adjust based on specific project requirements (e.g., higher coverage for low-frequency variant detection).

- **Sample Contamination**: High levels of cross-sample contamination can affect identity verification. Include negative controls to assess contamination rates.

- **Reference Genome Consistency**: Ensure the reference genome used for alignment matches the one used for coverage calculations.

- **Performance Considerations**: Processing large BAM files can be memory-intensive. Monitor resource usage for whole-genome sequencing data.

## Examples

### Run basic QC on targeted sequencing data
**Args:** `hmnqc -b sample.bam -t targets.bed -o qc_report.html`
**Explanation:** Generates comprehensive QC report from BAM file and target regions BED file.

### Specify coverage thresholds
**Args:** `hmnqc -b sample.bam -t targets.bed -cov 30 100 500 -o qc_report.html`
**Explanation:** Reports coverage at 30x, 100x, and 500x thresholds for different sensitivity requirements.

### Check sample identity
**Args:** `hmnqc -b sample.bam -t targets.bed -identity expected_genotypes.vcf -o qc_report.html`
**Explanation:** Verifies sample identity by comparing detected variants with expected genotypes from a reference VCF.

### Compare multiple samples
**Args:** `hmnqc -b sample1.bam sample2.bam sample3.bam -t targets.bed -o multi_sample_qc.html`
**Explanation:** Generates combined QC report for multiple samples, enabling batch comparison.

### Output coverage statistics to CSV
**Args:** `hmnqc -b sample.bam -t targets.bed -csv coverage_stats.csv -o qc_report.html`
**Explanation:** Exports detailed coverage statistics to CSV file for further analysis in spreadsheet tools.

### Assess panel performance
**Args:** `hmnqc -b sample.bam -t targets.bed -panel -o panel_qc.html`
**Explanation:** Focuses on panel-specific metrics including probe efficiency and on-target rates.

### Generate summary statistics
**Args:** `hmnqc -b sample.bam -t targets.bed -summary summary.txt -o qc_report.html`
**Explanation:** Creates a concise text summary of key QC metrics for quick review.