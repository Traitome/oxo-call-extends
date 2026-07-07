---
name: seq2c
category: variant-analysis
description: seq2c - Cohort-based copy number calling in gene regions
tags: ["seq2c", "variant-analysis", "copy-number", "CNV"]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/Seq2C"
---

## Concepts

- **Tool Overview**: seq2c (v2019.05.30) performs cohort-based copy number calling in gene regions.
- **Core Function**: Calls copy number variations (CNVs) across gene regions using cohort data.
- **Algorithm**: Uses read depth analysis for CNV detection.
- **Input/Output**: Accepts BAM files and produces CNV calls.
- **Cohort Analysis**: Focuses on cohort-based copy number analysis.
- **Applications**: Cancer genomics, somatic CNV detection, and cohort studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Reference Genome**: Requires proper reference genome setup.
- **False Positives**: May produce false positive calls.

## Examples

### Call CNVs
**Args:** `seq2c.pl -i input.bam -o output.txt`
**Explanation:** `-i` input BAM; `-o` output file.

### With panel
**Args:** `seq2c.pl -i input.bam -p panel.bed -o output.txt`
**Explanation:** `-p` specifies target panel.

### Verbose logging
**Args:** `seq2c.pl -i input.bam -v -o output.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seq2c.pl --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seq2c.pl --version`
**Explanation:** Shows current version.

### Cohort analysis
**Args:** `seq2c.pl -i cohort.list -o output.txt`
**Explanation:** Analyzes multiple samples in cohort.

### Filter output
**Args:** `seq2c.pl -i input.bam -f 0.1 -o output.txt`
**Explanation:** `-f 0.1` filters by confidence threshold.