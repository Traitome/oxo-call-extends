---
name: rustybam
category: alignment
description: Mitchell Vollger's bioinformatics Rust utilities for BAM file manipulation.
tags: ["rustybam", "BAM", "alignment", "Rust", "bioinformatics"]
author: oxo-call-community
source_url: "https://vollgerlab.com/rustybam"
---

## Concepts

- **Tool Overview**: rustybam (v0.2.0) is a collection of Rust-based bioinformatics utilities for BAM file manipulation developed by Mitchell Vollger. It provides fast and memory-efficient tools for processing aligned sequencing data.
- **Core Function**: Offers utilities for BAM file processing including filtering, sorting, merging, and extraction of specific reads or regions.
- **Algorithm**: Leverages Rust's performance and memory safety for efficient BAM file operations. Implements parallel processing for large datasets.
- **Input Format**: BAM/SAM files with aligned sequencing reads. Supports both coordinate-sorted and queryname-sorted files.
- **Output Format**: BAM/SAM files, VCF files for variant calling utilities, and various text formats for reporting.
- **Use Case**: Preprocessing alignment data, quality filtering of BAM files, extracting specific genomic regions, generating alignment statistics.

## Pitfalls

- **BAM format requirements**: Requires properly formatted BAM files with correct headers.
- **Index requirements**: Some operations require BAM index files (BAI).
- **Memory usage**: Large BAM files may require significant memory for processing.
- **Version compatibility**: Different BAM versions may have compatibility issues.
- **Sorting requirements**: Some operations require coordinate-sorted BAM files.
- **Filtering complexity**: Complex filtering criteria may require multiple passes.

## Examples

### Filter BAM by mapping quality
**Args:** `rustybam filter -i input.bam -o filtered.bam -q 30`
**Explanation:** `-q` minimum mapping quality. Filters reads with MAPQ < 30.

### Extract reads from region
**Args:** `rustybam extract -i input.bam -o region.bam -r chr1:100000-200000`
**Explanation:** `-r` genomic region in format chr:start-end.

### Sort BAM file
**Args:** `rustybam sort -i input.bam -o sorted.bam`
**Explanation:** Sorts BAM file by coordinate.

### Merge BAM files
**Args:** `rustybam merge -o merged.bam input1.bam input2.bam input3.bam`
**Explanation:** Merges multiple BAM files into one.

### Remove duplicates
**Args:** `rustybam dedup -i input.bam -o deduped.bam`
**Explanation:** Removes duplicate reads from BAM file.

### Generate alignment statistics
**Args:** `rustybam stats -i input.bam -o stats.txt`
**Explanation:** Generates statistics including mapping rate, coverage, and insert size.

### Convert SAM to BAM
**Args:** `rustybam view -i input.sam -o output.bam -b`
**Explanation:** `-b` outputs BAM format instead of SAM.
