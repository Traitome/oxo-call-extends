---
name: nanopack
category: qc
description: NanoPack - Meta package for Oxford Nanopore long-read processing tools
tags: [nanopack, qc, nanopore, meta-package, long-reads, quality-control]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanopack"
---

## Concepts

- **Tool Overview**: NanoPack v1.1.1 is a meta package that bundles multiple Oxford Nanopore sequencing data processing and quality control tools into a single installation.
- **Core Function**: Provides a unified suite of tools for Nanopore data analysis including visualization, filtering, trimming, and statistics generation.
- **Components**: Includes NanoPlot (visualization), NanoFilt (filtering), NanoComp (comparison), NanoStat (statistics), NanoGet (extraction), NanoLyse (lambda filtering), and NanoMath (utilities).
- **Input Format**: Each component tool accepts different formats including FASTQ, BAM, and sequencing summary files.
- **Output**: Produces quality control reports, filtered reads, statistical summaries, and visualizations.
- **Use Case**: Comprehensive quality control and preprocessing of Nanopore sequencing data, pipeline integration, and data analysis workflows.

## Pitfalls

- **Version Compatibility**: Individual tool versions may vary. Check component versions before use.
- **Component Dependencies**: Some tools depend on others. Ensure proper installation order if installing individually.
- **Memory Usage**: Processing large datasets requires sufficient memory. Consider subsampling for very large files.
- **File Compression**: Ensure consistent compression when piping between tools. Mixed compression may cause issues.
- **Tool Specificity**: Each component has specific requirements. Refer to individual tool documentation.
- **Python Version**: Requires Python 3.6+. Older versions may cause compatibility issues.

## Examples

### Install NanoPack
**Args:** `conda install -c bioconda nanopack`
**Explanation:** Installs the complete NanoPack suite of tools.

### Run NanoPlot
**Args:** `NanoPlot -i reads.fastq.gz -o qc_plots/`
**Explanation:** Generates quality control plots from Nanopore reads.

### Filter reads with NanoFilt
**Args:** `gunzip -c reads.fastq.gz | NanoFilt -q 10 | gzip > filtered.fastq.gz`
**Explanation:** Filters reads by quality using NanoFilt.

### Compare runs with NanoComp
**Args:** `NanoComp -f run1.fastq run2.fastq -n Run1 Run2 -o comparison/`
**Explanation:** Compares multiple sequencing runs.

### Display component help
**Args:** `NanoStat --help`
**Explanation:** Shows help for specific component tool.
