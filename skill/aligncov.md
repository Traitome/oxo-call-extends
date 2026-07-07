---
name: aligncov
category: alignment
description: Obtain tidy alignment coverage info from sorted BAM files
tags: [aligncov, alignment, BAM, coverage, statistics, depth]
author: oxo-call-community
source_url: "https://github.com/pcrxn/aligncov"
---

## Concepts

- **Tool Overview**: AlignCov is a Python package that generates tidy alignment coverage information from sorted BAM files, producing two tab-separated tables for downstream analysis.
- **Core Function**: Extracts alignment summary statistics and per-base read depths from sorted BAM files using SAMtools and Pandas.
- **Output Tables**: 
  - `_stats.tsv`: Alignment summary statistics including fold-coverage and proportion of target covered
  - `_depth.tsv`: Per-base read depths for each position in each target
- **Statistics Provided**: target name, sequence length, total depth, covered length, proportion covered (prop_cov), fold coverage (fold_cov)
- **Dependencies**: Requires samtools >= 1.15 and pandas >= 1.0.0
- **Installation**: Install via bioconda: `conda install -c bioconda aligncov`

## Pitfalls

- **Sorted BAM Required**: Input BAM file must be coordinate-sorted; will not work with unsorted alignments.
- **Index Required**: BAM file must have corresponding index (.bai) file for efficient operations.
- **Memory Usage**: For large BAM files, per-base depth output can be memory-intensive.
- **Output Naming**: Output files are automatically named with `_stats.tsv` and `_depth.tsv` suffixes.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available options and usage instructions.

### Basic usage with output prefix
**Args:** `aligncov -i sorted.bam -o sample`
**Explanation:** Generates `sample_stats.tsv` and `sample_depth.tsv` from sorted BAM file.

### Minimal usage with default output name
**Args:** `aligncov -i sorted.bam`
**Explanation:** Generates `sample_stats.tsv` and `sample_depth.tsv` using default output prefix.

### Output to specific directory
**Args:** `aligncov -i data/sorted.bam -o results/sample1`
**Explanation:** Saves output files to results directory with sample1 prefix.

### Process multiple BAM files
**Args:** `aligncov -i sample1.bam -o sample1 && aligncov -i sample2.bam -o sample2`
**Explanation:** Process multiple BAM files sequentially with separate output files.

### Combine with other tools
**Args:** `aligncov -i sorted.bam -o coverage && cat coverage_stats.tsv`
**Explanation:** Generate coverage stats and view the statistics table.

### Filter specific regions
**Args:** `samtools view -b sorted.bam chr1:1-100000 > region.bam && aligncov -i region.bam -o region_cov`
**Explanation:** Extract specific genomic region and compute coverage for that region.

### Get alignment summary statistics
**Args:** `aligncov -i sorted.bam -o output && grep -v "^#" output_stats.tsv`
**Explanation:** Generate stats and filter out header comments for further processing.

### Calculate mean coverage per target
**Args:** `aligncov -i sorted.bam -o output && awk '{sum += $6; n++} END {print "Mean coverage:", sum/n}' output_stats.tsv`
**Explanation:** Compute average fold coverage across all targets.
