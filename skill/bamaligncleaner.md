---
name: bamaligncleaner
category: alignment
description: bamAlignCleaner - Remove unaligned references from BAM alignment files
tags: [bamaligncleaner, alignment, BAM, reference-filtering, cleaning]
author: oxo-call-community
source_url: "https://github.com/maxibor/bamAlignCleaner"
---

## Concepts

- **Tool Overview**: bamAlignCleaner removes unaligned references from BAM alignment files, cleaning up alignment data by removing sequences with no mapped reads. Version 0.3.
- **Core Function**: Filters BAM files to retain only reference sequences that have at least one aligned read.
- **Reference Cleaning**: Removes empty reference sequences from BAM header and alignments.
- **Alignment Filtering**: Filters out alignments to references with no coverage.
- **Header Update**: Updates BAM header to reflect remaining references.
- **Input/Output**: Accepts BAM files, outputs cleaned BAM files with reduced reference set.
- **Installation**: `conda install -c bioconda bamaligncleaner`.

## Pitfalls

- **BAM Index**: May require re-indexing output BAM file.
- **Reference Order**: May change reference order in output file.
- **Version Compatibility**: Options may vary between versions. Check help for your version.
- **Memory Usage**: Large BAM files may require significant memory.

## Examples

### Basic cleaning
**Args:** `bamaligncleaner -i input.bam -o cleaned.bam`
**Explanation:** Removes unaligned references from BAM file.

### Keep original index
**Args:** `bamaligncleaner -i input.bam -o cleaned.bam --keep-index`
**Explanation:** Preserves original BAM index if available.

### Verbose mode
**Args:** `bamaligncleaner -i input.bam -o cleaned.bam -v`
**Explanation:** Shows detailed information about cleaning process.

### Minimum coverage
**Args:** `bamaligncleaner -i input.bam -o cleaned.bam --min-coverage 10`
**Explanation:** Keeps only references with at least 10x coverage.

### Output statistics
**Args:** `bamaligncleaner -i input.bam -o cleaned.bam --stats stats.txt`
**Explanation:** Outputs statistics about removed references.

### Force overwrite
**Args:** `bamaligncleaner -i input.bam -o cleaned.bam -f`
**Explanation:** Overwrites output file if it exists.

### Display help
**Args:** `bamaligncleaner --help`
**Explanation:** Shows all available command-line options and usage information.