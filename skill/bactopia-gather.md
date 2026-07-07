---
name: bactopia-gather
category: formatting
description: Bactopia Gather - Sample collection and aggregation tool for Bactopia pipeline
tags: [bactopia-gather, formatting, sample-management, aggregation, bactopia]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: Bactopia Gather is a component of the Bactopia pipeline that collects and aggregates results from multiple samples into a unified format for downstream analysis. Version 1.0.5.
- **Core Function**: Gathers individual sample results from Bactopia runs into aggregated reports and data structures.
- **Sample Aggregation**: Combines results from multiple samples into comprehensive summaries.
- **Report Generation**: Creates consolidated reports across all samples in a Bactopia project.
- **Data Formatting**: Converts and standardizes output formats for consistency across samples.
- **Input/Output**: Processes Bactopia sample outputs, generates aggregated reports.
- **Installation**: `conda install -c bioconda bactopia-gather`.

## Pitfalls

- **Version Compatibility**: Must match Bactopia pipeline version for proper integration.
- **Sample Consistency**: Requires consistent analysis parameters across all samples.
- **Missing Data**: Incomplete sample results can affect aggregation quality.
- **Storage Requirements**: Aggregated data can be large. Ensure sufficient disk space.

## Examples

### Gather all samples
**Args:** `bactopia-gather --input samples/ --output aggregated_results/`
**Explanation:** Gathers results from all samples in input directory into aggregated output.

### Specify sample list
**Args:** `bactopia-gather --samples samples.txt --input runs/ --output aggregated/`
**Explanation:** Processes only samples listed in samples.txt file.

### Generate summary report
**Args:** `bactopia-gather --input samples/ --output aggregated/ --report summary.html`
**Explanation:** Generates HTML summary report of all sample results.

### Combine variant calls
**Args:** `bactopia-gather --input samples/ --output aggregated/ --variants combined.vcf`
**Explanation:** Combines variant calls from all samples into single VCF file.

### Quality metrics aggregation
**Args:** `bactopia-gather --input samples/ --output aggregated/ --quality-metrics qc_report.tsv`
**Explanation:** Aggregates quality control metrics across all samples.

### Custom output format
**Args:** `bactopia-gather --input samples/ --output aggregated/ --format json`
**Explanation:** Outputs aggregated results in JSON format instead of default.

### Display help
**Args:** `bactopia-gather --help`
**Explanation:** Shows all available command-line options and usage information.