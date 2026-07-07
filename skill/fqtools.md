---
name: fqtools
category: formatting
description: An efficient FASTQ manipulation suite.
tags: [fqtools, FASTQ, sequence processing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/alastair-droop/fqtools"
---

## Concepts
- **FASTQ Manipulation**: Comprehensive suite for FASTQ file operations.
- **Efficient Processing**: Optimized for speed and memory efficiency.
- **Quality Control**: Built-in quality assessment tools.
- **Filtering**: Supports various filtering strategies.
- **Format Conversion**: Converts between different sequence formats.

## Pitfalls
- **Memory Usage**: May require significant memory for large files.
- **Format Compatibility**: Some non-standard FASTQ formats may not be supported.
- **Compression**: Limited support for compressed formats.
- **Performance**: Slower on certain operations compared to specialized tools.
- **Documentation**: Limited documentation for advanced features.

## Examples
### Count reads
**Args:** `fqtools count reads.fastq`
**Explanation:** Counts the number of reads in the FASTQ file.

### Filter by quality
**Args:** `fqtools filter -q 20 -i reads.fastq -o filtered.fastq`
**Explanation:** Filters reads with minimum average quality of 20.

### Convert to FASTA
**Args:** `fqtools fasta -i reads.fastq -o reads.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Trim low-quality ends
**Args:** `fqtools trim -q 15 -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims bases with quality below 15 from read ends.

### Extract subset of reads
**Args:** `fqtools sample -n 1000 -i reads.fastq -o sample.fastq`
**Explanation:** Extracts 1000 random reads from the input.