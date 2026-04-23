---
name: accusnv
category: variant-calling
description: High-accuracy SNV calling for bacterial isolates using AccuSNV.
tags: [accusnv, variant-calling, snv, bacteria, snp]
author: oxo-call-community
source_url: "https://github.com/liaoherui/AccuSNV"
---

## Concepts

- **Tool Overview**: High-accuracy SNV calling tool designed specifically for bacterial isolate sequencing data. Version 1.0.0.5.
- **Core Function**: Identifies single nucleotide variants in bacterial genomes with high accuracy, accounting for bacterial-specific challenges like low diversity and clonal populations.
- **Input/Output**: Input is aligned reads (BAM) and reference genome (FASTA); output is SNV calls (VCF).
- **Installation**: Install via bioconda: `conda install -c bioconda accusnv`
- **Platform Support**: Platform-independent (noarch)
- **Bacterial Optimized**: Specifically designed for bacterial isolate data, handling challenges like high coverage and clonal populations.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Bacterial Only**: Optimized for bacterial isolates. May not perform well on eukaryotic or viral data.
- **Coverage Requirements**: Requires sufficient sequencing coverage for accurate SNV calling.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Call SNVs from aligned reads
**Args:** `-r reference.fa -b aligned.bam -o variants.vcf`
**Explanation:** Calls SNVs from the aligned BAM file using the specified reference genome. Output is in VCF format.

### Run with minimum coverage filter
**Args:** `-r ref.fa -b aligned.bam --min-depth 10 --min-qual 30 -o filtered_variants.vcf`
**Explanation:** Filters SNVs by minimum depth (10x) and quality score (30). Higher thresholds reduce false positives.
