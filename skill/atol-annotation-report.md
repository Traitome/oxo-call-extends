---
name: atol-annotation-report
category: annotation
description: AToL Annotation Report - Generate standard PDF report for genome annotations
tags: [annotation, report-generation, pdf, visualization]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-annotation-report"
---

## Concepts

- **Tool Overview**: Generates standardized PDF reports for genome annotations in AToL Genome Engine workflow.

- **Summary Statistics**: Includes gene counts, feature distributions, and functional annotation summaries.

- **Visualizations**: Creates charts and graphs showing annotation characteristics.

- **Standard Format**: Produces consistent, publication-ready reports for genome annotation projects.

## Pitfalls

- **Large Genomes**: Very large genomes may generate extremely long reports. Consider summarization options.

- **Functional Annotation**: Requires functional annotation data for complete reports. Missing data results in incomplete sections.

- **PDF Generation**: Large reports may be slow to generate. Allow sufficient time.

## Examples

### Basic report generation
**Args:** `atol-annotation-report --annotation genes.gtf --output report.pdf`
**Explanation:** Generates PDF report from GTF annotation file.

### Include functional annotation
**Args:** `atol-annotation-report --annotation genes.gtf --functional-annotation functional.tsv --output report.pdf`
**Explanation:** Includes functional annotation data in report for comprehensive summary.

### Custom report title
**Args:** `atol-annotation-report --annotation genes.gtf --title "My organism annotation" --output report.pdf`
**Explanation:** Sets custom title for the annotation report.

### Detailed statistics
**Args:** `atol-annotation-report --annotation genes.gtf --detailed --output report.pdf`
**Explanation:** Includes detailed statistics and breakdowns in report.
