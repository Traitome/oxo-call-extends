---
name: sample_grouping
category: utility
description: Merge sequencing reads based on metadata groups
tags: ["sample_grouping", "metadata", "merging", "FASTQ", "utility"]
author: oxo-call-community
source_url: "https://github.com/SantaMcCloud/Sample_grouping"
---

## Concepts

- **Tool Overview**: sample_grouping (v1.0.0) is a tool for merging sequencing reads from multiple samples based on metadata groups, enabling combined analysis of related samples.
- **Core Function**: Groups and merges sequencing reads according to metadata categories, facilitating batch processing and comparative analysis.
- **Algorithm**: Parses metadata files to group samples, then merges corresponding sequence files into group-specific outputs.
- **Input Format**: FASTQ files, metadata CSV/TSV files, sample mapping files.
- **Output Format**: Merged FASTQ files per group, summary reports, group statistics.
- **Use Case**: Batch processing, cohort analysis, multi-sample sequencing projects.

## Pitfalls

- **Metadata format**: Requires properly formatted metadata files.
- **File matching**: Sample names must match between metadata and sequence files.
- **Memory usage**: Merging large files requires significant memory.
- **Duplicate samples**: May create redundant outputs if samples belong to multiple groups.
- **Output organization**: Requires careful output directory management.
- **Compression**: May require decompression for gzipped input files.

## Examples

### Basic grouping
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir`
**Explanation:** `-i` metadata file; `-d` directory with FASTQ files; `-o` output directory.

### Group by category
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir -c group_column`
**Explanation:** `-c` specifies metadata column for grouping.

### Paired-end reads
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir --paired-end`
**Explanation:** `--paired-end` handles paired-end sequencing data.

### Gzipped output
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir --gzip`
**Explanation:** `--gzip` compresses output FASTQ files.

### Dry run
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir --dry-run`
**Explanation:** `--dry-run` shows what would be merged without executing.

### Output statistics
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir -s stats.txt`
**Explanation:** `-s` outputs grouping statistics.

### Custom pattern
**Args:** `sample_grouping -i metadata.csv -d fastq_dir -o output_dir -p "*_R1.fastq"`
**Explanation:** `-p` specifies file pattern for matching.