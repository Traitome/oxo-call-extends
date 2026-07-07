---
name: nanosplit
category: qc
description: NanoSplit performs splitting of Oxford Nanopore sequencing data into pass and fail datasets based on quality metrics.
tags: [nanosplit, qc, nanopore, splitting, filtering]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanosplit"
---

## Concepts

- **Tool Overview**: NanoSplit v0.1.4 is a quality control tool for splitting Nanopore sequencing data into pass and fail categories.
- **Core Function**: Separates Nanopore reads based on quality thresholds defined by the sequencing instrument or user-specified criteria.
- **Algorithm**: Parses FASTQ quality scores and compares against predefined or custom quality thresholds.
- **Input Format**: Accepts FASTQ files (gzipped or uncompressed) from Oxford Nanopore sequencing runs.
- **Output**: Produces separate FASTQ files for pass and fail reads, along with summary statistics.
- **Use Case**: Quality filtering of Nanopore data, preparing high-quality reads for downstream analysis.

## Pitfalls

- **Quality Thresholds**: Default thresholds may not be appropriate for all sequencing runs.
- **Input Requirements**: Requires properly formatted FASTQ with quality scores.
- **Memory Usage**: May require significant memory for very large FASTQ files.
- **Compression Issues**: Gzipped files need proper decompression handling.
- **Batch Processing**: Processing multiple files requires careful scripting.
- **Output Management**: Multiple output files can clutter the working directory.

## Examples

### Display help
**Args:** `nanosplit --help`
**Explanation:** Shows available options and usage instructions.

### Basic usage
**Args:** `nanosplit -i reads.fastq -o output_dir`
**Explanation:** Splits reads into pass and fail FASTQ files using default thresholds.

### Custom quality threshold
**Args:** `nanosplit -i reads.fastq -q 10 -o output_dir`
**Explanation:** Sets minimum quality threshold to Q10 for passing reads.

### Gzipped input
**Args:** `nanosplit -i reads.fastq.gz -o output_dir`
**Explanation:** Processes gzipped FASTQ file directly.

### Custom output prefix
**Args:** `nanosplit -i reads.fastq -o output_dir -p sample1`
**Explanation:** Adds custom prefix to output filenames.

### Length filtering
**Args:** `nanosplit -i reads.fastq -l 1000 -o output_dir`
**Explanation:** Filters reads with minimum length of 1000bp.