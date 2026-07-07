---
name: sarscov2summary
category: formatting
description: Summary report generator for Galaxy SARS-CoV2 Selection Analysis Workflow
tags: ["sarscov2summary", "formatting", "SARS-CoV2", "COVID-19", "reporting"]
author: oxo-call-community
source_url: "https://github.com/nickeener/sarscov2formatter"
---

## Concepts

- **Tool Overview**: sarscov2summary (v0.5) is a summary report generator for Galaxy SARS-CoV-2 selection analysis workflows, producing comprehensive reports of viral sequencing analyses.
- **Core Function**: Aggregates analysis results and generates human-readable summaries of SARS-CoV-2 variant detection and selection analysis.
- **Input/Output**: Takes analysis results from multiple tools and produces consolidated reports in various formats.
- **Report Types**: Generates variant summaries, quality metrics, and selection analysis reports.
- **Visualization**: Creates charts and graphs for visual representation of sequencing data.
- **Applications**: Used in COVID-19 genomic surveillance and research pipelines.

## Pitfalls

- **Workflow Integration**: Designed for specific Galaxy workflow outputs.
- **Input Compatibility**: Requires specific result formats from upstream tools.
- **Resource Requirements**: May require significant memory for large datasets.
- **Report Complexity**: Generated reports can be large and require careful interpretation.
- **Dependency Management**: Relies on multiple bioinformatics tools for input data.
- **Time Constraints**: Report generation can be time-consuming for large sample sets.

## Examples

### Generate basic summary
**Args:** `sarscov2summary -i analysis_results/ -o summary_report.txt`
**Explanation:** `-i` input directory with analysis results; `-o` output summary report.

### HTML report with visualizations
**Args:** `sarscov2summary -i results/ -o report.html -f html -v`
**Explanation:** `-f html` outputs HTML format; `-v` includes visualizations.

### Variant frequency table
**Args:** `sarscov2summary -i variants.vcf -o freq_table.tsv --frequency`
**Explanation:** Generates variant frequency table from VCF file.

### Quality metrics report
**Args:** `sarscov2summary -i qc_results/ -o qc_report.pdf -q`
**Explanation:** `-q` generates quality control metrics report in PDF format.

### Multi-sample comparison
**Args:** `sarscov2summary -i samples/ -o comparison_report.html -m`
**Explanation:** `-m` enables multi-sample comparison mode.

### Custom report template
**Args:** `sarscov2summary -i results/ -o report.html -t template.jinja`
**Explanation:** `-t` specifies custom Jinja2 template for report generation.

### Statistics only
**Args:** `sarscov2summary -i results/ -o stats.json --stats-only`
**Explanation:** Outputs only statistical data in JSON format for downstream processing.