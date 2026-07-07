---
name: bcbio-rnaseq
category: expression
description: bcbio-rnaseq - Report generation for bcbio-nextgen RNA-seq analysis
tags: [bcbio-rnaseq, expression, RNA-seq, report-generation, visualization]
author: oxo-call-community
source_url: "https://github.com/roryk/bcbio.rnaseq"
---

## Concepts

- **Tool Overview**: bcbio-rnaseq (v1.2.0) generates comprehensive reports for bcbio-nextgen RNA-seq analysis runs, providing visualization and quality assessment.
- **Core Function**: Generates high-quality HTML reports summarizing RNA-seq analysis results.
- **Report Generation**: Creates interactive HTML reports with quality metrics and visualizations.
- **Integration**: Works seamlessly with bcbio-nextgen RNA-seq pipeline outputs.
- **Visualization**: Includes PCA plots, expression heatmaps, quality control metrics, and differential expression results.
- **Input/Output**: Accepts bcbio-nextgen analysis results; outputs HTML reports.
- **Installation**: `conda install -c bioconda bcbio-rnaseq`.

## Pitfalls

- **bcbio-nextgen Dependency**: Requires bcbio-nextgen analysis output as input.
- **Configuration**: Requires properly configured analysis directory structure.
- **Data Quality**: Report quality depends on input data quality and completeness.
- **Version Compatibility**: Ensure compatibility with bcbio-nextgen version.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Generate basic report
**Args:** `bcbio_rnaseq.py /path/to/bcbio/work/dir -o report.html`
**Explanation:** Generates HTML report from bcbio-nextgen RNA-seq analysis.

### With sample configuration
**Args:** `bcbio_rnaseq.py /path/to/work/dir -c sample_config.yaml -o report.html`
**Explanation:** Uses specified sample configuration for report generation.

### Include differential expression
**Args:** `bcbio_rnaseq.py /path/to/work/dir --de-analysis -o report.html`
**Explanation:** Includes differential expression analysis in report.

### Custom report template
**Args:** `bcbio_rnaseq.py /path/to/work/dir --template custom_template.html -o report.html`
**Explanation:** Uses custom HTML template for report generation.

### Generate PDF report
**Args:** `bcbio_rnaseq.py /path/to/work/dir --pdf -o report.pdf`
**Explanation:** Generates PDF version of the report.

### Include QC metrics
**Args:** `bcbio_rnaseq.py /path/to/work/dir --qc-only -o qc_report.html`
**Explanation:** Generates report with only quality control metrics.

### Display help
**Args:** `bcbio_rnaseq.py --help`
**Explanation:** Shows all available command-line options and usage information.