---
name: multiqc
category: qc
description: Aggregate results from bioinformatics analyses across many samples into a single report.
tags: [multiqc, qc, alignment, bioinformatics, reporting]
author: oxo-call-community
source_url: "https://seqera.io/multiqc"
---

## Concepts

- **Tool Overview**: MultiQC (v1.33+) is a tool for aggregating bioinformatics analysis results across multiple samples into a single interactive HTML report. It supports over 100 different bioinformatics tools and formats.
- **Core Function**: Scans analysis directories for log files and report outputs, parses them, and generates a comprehensive summary report with interactive plots and tables.
- **Input/Output**: Input: Directory containing analysis results from various tools. Output: Interactive HTML report with aggregated QC metrics.
- **Algorithm**: Uses a plugin system to parse different tool outputs, aggregates metrics, and generates reports using Jinja2 templates.
- **Key Features**: Supports many bioinformatics tools (FastQC, STAR, Salmon, samtools, etc.), interactive visualizations, and customizable reports.
- **Installation**: `conda install -c bioconda multiqc`

## Pitfalls

- **Tool Detection**: MultiQC relies on specific file patterns to detect tool outputs. Ensure your analysis tools output standard file formats.
- **Missing Tools**: Not all bioinformatics tools are supported. Check the MultiQC documentation for supported tools before running.
- **Report Size**: Reports with many samples can become large. Use `-x` to exclude certain tools or samples if needed.
- **Output Directory**: By default, MultiQC creates a report in the current directory. Use `-o` to specify an output directory.
- **Custom Templates**: Custom report templates require proper Jinja2 syntax. Test templates before production use.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Generate report from analysis directory
**Args:** `/path/to/analysis_dir`
**Explanation:** Scans the directory for bioinformatics reports and generates a single MultiQC HTML report in the current directory.

### Generate report with custom output directory
**Args:** `-o output_dir /path/to/analysis_dir`
**Explanation:** Generates report to the specified output directory.

### Force overwrite existing report
**Args:** `-f -o output_dir /path/to/analysis_dir`
**Explanation:** Forces overwrite of any existing report in the output directory.

### Exclude specific tools
**Args:** `-x fastqc -x star /path/to/analysis_dir`
**Explanation:** Excludes FastQC and STAR results from the report.

### Include only specific tools
**Args:** `-i fastqc -i samtools /path/to/analysis_dir`
**Explanation:** Only includes FastQC and samtools results in the report.

### Custom report title
**Args:** `-n "My Project QC Report" /path/to/analysis_dir`
**Explanation:** Sets a custom title for the HTML report.

### Multi-sample report with sample names
**Args:** `-d /path/to/samples/ -o multiqc_report/`
**Explanation:** Scans multiple sample directories under /path/to/samples/ and generates a combined report.

### Generate PDF report
**Args:** `--pdf /path/to/analysis_dir`
**Explanation:** Generates a PDF version of the report alongside the HTML version.