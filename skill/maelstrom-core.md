---
name: maelstrom-core
category: utility
description: Rust utilities for NGS data processing.
tags: [maelstrom-core, utility, NGS, rust]
author: oxo-call-community
source_url: "https://github.com/bihealth/maelstrom-core"
---

## Concepts

- **Tool Overview**: maelstrom-core v0.1.1 - A collection of high-performance Rust utilities for processing next-generation sequencing data.
- **Core Function**: Provides efficient tools for BAM/CRAM processing, variant calling support, and general bioinformatics operations.
- **Input/Output**: Input: BAM, CRAM, VCF files; Output: Processed files, statistics, transformed data.
- **Installation**: `conda install -c bioconda maelstrom-core`
- **Rust Implementation**: Built in Rust for high performance and memory safety.
- **Parallel Processing**: Leverages multi-threading for efficient data processing.

## Pitfalls

- **File Compatibility**: Requires properly formatted BAM/CRAM files with valid indexes.
- **Memory Usage**: Large files may require significant RAM for processing.
- **Version Compatibility**: Tools may not work with older file formats.
- **Reference Genome**: Requires matching reference genome for certain operations.
- **Index Files**: Missing index files will cause errors in many operations.
- **Output Formats**: Some operations have specific output format requirements.

## Examples

### Count reads in BAM
**Args:** `maelstrom-core count -i input.bam`
**Explanation:** Counts total reads in BAM file.

### Extract reads by region
**Args:** `maelstrom-core extract -i input.bam -r chr1:1-1000000 -o output.bam`
**Explanation:** Extracts reads overlapping specified genomic region.

### Filter reads by quality
**Args:** `maelstrom-core filter -i input.bam -q 30 -o filtered.bam`
**Explanation:** Filters reads with mapping quality >= 30.

### Sort BAM file
**Args:** `maelstrom-core sort -i input.bam -o sorted.bam`
**Explanation:** Sorts BAM file by coordinate.

### Index BAM file
**Args:** `maelstrom-core index -i input.bam`
**Explanation:** Creates BAM index file (BAI).

### Merge BAM files
**Args:** `maelstrom-core merge -i input1.bam input2.bam -o merged.bam`
**Explanation:** Merges multiple BAM files into one.