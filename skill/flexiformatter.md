---
name: flexiformatter
category: formatting
description: "Flexiformatter moves flexiplex barcode and UMI sequences to BAM tags for downstream analysis and visualization."
tags: [flexiformatter, formatting, bam, barcode, umi, bioinformatics, sequencing]
author: oxo-call-community
source_url: "https://github.com/ljwharbers/flexiformatter"
---

## Concepts
- **Tool Overview**: Flexiformatter is a tool for extracting barcode and UMI sequences from flexiplex-processed reads and storing them as BAM tags for downstream analysis tools.
- **Core Function**: Converts flexiplex-formatted read names into standard BAM tags, enabling seamless integration with variant callers and other analysis tools.
- **Input/Output**: Input: BAM file from flexiplex demultiplexing. Output: BAM file with annotated barcode and UMI tags.
- **Tag Standards**: Implements SAM specification tags for barcode (BC) and UMI (UQ) for compatibility with GATK, Picard, and other tools.
- **Flexiplex Compatibility**: Works with flexiplex output format where barcode and UMI are embedded in read names.
- **Validation**: Validates tag formatting and reports any inconsistencies in the BAM file.
- **Installation**: `conda install -c bioconda flexiformatter` or clone from GitHub. Requires Python 3.x and pysam.

## Pitfalls
- **Flexiplex Format Requirement**: Designed specifically for flexiplex output. Other demultiplexing tools may have different formats.
- **BAM File Requirements**: Input BAM must be properly sorted and indexed. Unsorted BAM files may cause issues.
- **Tag Conflicts**: Existing BC/UQ tags will be replaced. Use caution when processing already-tagged BAM files.
- **Barcode/UMI Parsing**: Incorrect read name parsing may produce empty or incorrect tags. Verify output with samtools.
- **Memory Considerations**: Process large BAM files in chunks or use streaming to avoid memory issues.
- **Quality Filtering**: Does not perform quality filtering. Apply quality filters before or after tagging.

## Examples
### Basic tag formatting
**Args:** `flexiformatter -i flexiplex_output.bam -o tagged.bam`
**Explanation:** Converts flexiplex read names to BAM tags in output file.

### Add UMI quality tag
**Args:** `flexiformatter -i input.bam -o output.bam --umi-quality-tag`
**Explanation:** Adds UMI quality tag (UQ) in addition to barcode tag.

### Custom output prefix
**Args:** `flexiformatter -i input.bam --prefix processed_`
**Explanation:** Creates output file with specified prefix while preserving original filename.

### Include statistics
**Args:** `flexiformatter -i input.bam -o output.bam --stats stats.txt`
**Explanation:** Generates statistics file with tag counts and distribution.

### Force overwrite
**Args:** `flexiformatter -i input.bam -o output.bam --force`
**Explanation:** Overwrites existing output file without prompting for confirmation.
