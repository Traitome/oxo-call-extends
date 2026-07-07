---
name: compare-reads
category: qc
description: Cythonized function to compare sequencing reads by name
tags: [compare-reads, read-comparison, pysam, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/mvdbeek/pysam-compare-reads"
---

## Concepts

- **Tool Overview**: compare-reads is a cythonized function for efficiently comparing sequencing reads by name, optimized for speed using Cython compilation.
- **Core Function**: Compares reads between BAM/SAM files based on read names, useful for validating alignments or comparing different mapping results.
- **Algorithm**: Uses hash-based lookup for efficient read name matching between files.
- **Input**: BAM or SAM files containing aligned sequencing reads.
- **Output**: Comparison report indicating matching and non-matching reads.
- **Application**: Alignment validation, pipeline quality control, and read set comparison.
- **Installation**: Install via bioconda: `conda install -c bioconda compare-reads`

## Pitfalls

- **Read Names**: Requires consistent read naming between files.
- **File Format**: Must use properly formatted BAM/SAM files.
- **Memory Usage**: Large files may require significant memory for hash tables.
- **Sorting**: Files may need to be sorted or indexed for optimal performance.
- **Duplicate Names**: Duplicate read names may cause ambiguous matches.

## Examples

### Compare two BAM files
**Args:** `compare-reads -i file1.bam file2.bam -o comparison.txt`
**Explanation:** Compares reads between two BAM files by name.

### With specific read names
**Args:** `compare-reads -i file1.bam file2.bam -n read_names.txt -o comparison.txt`
**Explanation:** Compares only specified read names.

### Generate statistics
**Args:** `compare-reads -i file1.bam file2.bam -s -o stats.txt`
**Explanation:** Generates detailed comparison statistics.

### Display help
**Args:** `compare-reads --help`
**Explanation:** Shows all available options and usage information.