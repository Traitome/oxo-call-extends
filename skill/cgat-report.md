---
name: cgat-report
category: reporting
description: Python-based report generator built on Sphinx for bioinformatics analyses
tags: [cgat-report, reporting, sphinx, bioinformatics, documentation]
author: oxo-call-community
source_url: "https://github.com/AndreasHeger/CGATReport"
---

## Concepts

- **Tool Overview**: CGAT-Report is a Python-based report generator built on Sphinx for creating bioinformatics analysis reports.
- **Core Function**: Generates comprehensive reports from analysis results with integrated visualization.
- **Features**: Automated report generation, embedded plots, table generation, and PDF export.
- **Input**: Analysis results, configuration files, and documentation sources.
- **Output**: HTML reports, PDF documents, and interactive visualizations.
- **Application**: Documenting bioinformatics pipeline results and analysis workflows.
- **Installation**: Install via bioconda: `conda install -c bioconda cgat-report`

## Pitfalls

- **Sphinx Dependencies**: Requires Sphinx and related packages.
- **Template Customization**: May require template modification for specific needs.
- **Large Reports**: Complex reports may require significant build time.
- **LaTeX Requirements**: PDF generation requires LaTeX installation.

## Examples

### Generate report from configuration
**Args:** `cgat-report build report.conf`
**Explanation:** Builds report from configuration file.

### Generate PDF report
**Args:** `cgat-report build --pdf report.conf`
**Explanation:** Generates PDF version of the report.

### Initialize report project
**Args:** `cgat-report init my_report`
**Explanation:** Creates template files for new report project.

### Display help
**Args:** `cgat-report --help`
**Explanation:** Shows all available options and usage information.