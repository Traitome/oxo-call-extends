---
name: multiqc
category: qc
description: Aggregate results from bioinformatics analyses across many samples into a single report.
tags: [multiqc, qc, alignment]
author: oxo-call-community
source_url: "https://seqera.io/multiqc"
---

## Concepts

- **Tool Overview**: multiqc v1.33 - Aggregate results from bioinformatics analyses across many samples into a single report..
- **Core Function**: Aggregate results from bioinformatics analyses across many samples into a single report.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda multiqc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Generate report
**Args:** `/path/to/analysis_dir`
**Explanation:** Scans directory for bioinformatics reports and generates a single MultiQC HTML report.

### Force overwrite
**Args:** `-f -o output_dir /path/to/analysis_dir`
**Explanation:** Generates report with forced overwrite to specified output directory.

