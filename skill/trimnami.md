---
name: trimnami
category: analysis
description: TrimNami - Tool for analyzing RNA-seq read trimming efficiency.
tags: [trimnami, rna-seq, trimming-analysis, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/trimnami"
---

## Concepts

- **Tool Overview**: TrimNami - A tool for analyzing the efficiency of read trimming operations.
- **Core Function**: Evaluates trimming quality, identifies over-trimming, and provides statistics.
- **Input**: Raw and trimmed FASTQ files.
- **Output**: Trimming efficiency reports, quality metrics, diagnostic plots.
- **Installation**: `pip install trimnami` or `conda install -c bioconda trimnami`
- **Use Case**: Quality control, trimming optimization, sequencing data analysis.

## Pitfalls

- **Comparison**: Requires both raw and trimmed files for comparison.
- **Performance**: May be slow for large datasets.

## Examples

### Analyze trimming
**Args:** `trimnami -r raw.fastq -t trimmed.fastq -o report/`
**Explanation:** Analyze trimming efficiency.

### Generate report
**Args:** `trimnami report -i raw/ -o trimmed/ -s summary.txt`
**Explanation:** Generate trimming summary report.
