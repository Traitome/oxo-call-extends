---
name: bcbreport
category: utility
description: bcbreport - Rmd templates for generating bcbio-nextgen analysis reports
tags: [bcbreport, utility, Rmd, report-generation, bcbio-nextgen]
author: oxo-call-community
source_url: "https://github.com/lpantano/bcbio.coverage"
---

## Concepts

- **Tool Overview**: bcbreport (v0.99.29) provides R Markdown templates for generating comprehensive analysis reports from bcbio-nextgen sequencing analyses.
- **Core Function**: Generates automated reports using R Markdown templates for bcbio-nextgen results.
- **R Markdown Templates**: Provides pre-built Rmd templates for various sequencing analysis types.
- **Report Generation**: Creates HTML/PDF reports with quality metrics, coverage statistics, and visualizations.
- **Integration**: Works seamlessly with bcbio-nextgen analysis outputs.
- **Input/Output**: Accepts bcbio-nextgen analysis directories; outputs HTML/PDF reports.
- **Installation**: `conda install -c bioconda bcbreport`.

## Pitfalls

- **R Dependency**: Requires R and several R packages for report generation.
- **bcbio-nextgen Output**: Requires properly formatted bcbio-nextgen analysis output.
- **Template Configuration**: May require customization of templates for specific needs.
- **Version Compatibility**: Ensure compatibility with bcbio-nextgen version.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Generate basic report
**Args:** `bcbreport /path/to/bcbio/work/dir -o report.html`
**Explanation:** Generates HTML report from bcbio-nextgen analysis.

### Generate PDF report
**Args:** `bcbreport /path/to/work/dir -o report.pdf --pdf`
**Explanation:** Generates PDF version of the analysis report.

### With custom template
**Args:** `bcbreport /path/to/work/dir -t custom_template.Rmd -o report.html`
**Explanation:** Uses custom R Markdown template for report generation.

### Coverage report
**Args:** `bcbreport /path/to/work/dir --coverage -o coverage_report.html`
**Explanation:** Generates report focused on sequencing coverage metrics.

### Variant report
**Args:** `bcbreport /path/to/work/dir --variant -o variant_report.html`
**Explanation:** Generates report focused on variant calling results.

### Multi-sample comparison
**Args:** `bcbreport /path/to/work/dir --compare -o comparison_report.html`
**Explanation:** Generates comparative report across multiple samples.

### Display help
**Args:** `bcbreport --help`
**Explanation:** Shows all available command-line options and usage information.