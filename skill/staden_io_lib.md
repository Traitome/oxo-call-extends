---
name: staden_io_lib
category: programming
description: Staden io_lib is a library of file reading and writing code for SAM/BAM/CRAM and other bioinformatics formats.
tags: [staden_io_lib, file-io, sam, bam, cram]
author: oxo-call-community
source_url: "https://github.com/jkbonfield/io_lib/blob/io_lib-1-15-1/README.md"
---

## Concepts

- **Tool Overview**: staden_io_lib (v1.15.1) is a C library and set of utilities for reading and writing bioinformatics file formats.
- **Core Function**: Provides low-level I/O operations for SAM/BAM/CRAM, FASTQ, FASTA, and other sequencing formats.
- **Format Support**: SAM, BAM, CRAM, FASTQ, FASTA, SCF, ABIF, and various trace file formats.
- **Input/Output**: Input: Bioinformatics data files; Output: Formatted data or converted file formats.
- **API**: C library with bindings for Perl, Python, and other languages; command-line utilities also available.
- **Installation**: `conda install -c bioconda staden_io_lib` or compile from source.

## Pitfalls

- **File Corruption**: Corrupted BAM/CRAM files may cause crashes or incorrect parsing.
- **Version Compatibility**: Format specification changes affect older library versions.
- **Memory Management**: Improper memory handling in custom code can cause memory leaks.
- **Compression Issues**: CRAM compression requires reference genome for decompression.
- **Index Files**: Missing index files (BAI/CSI) prevent random access to BAM/CRAM.
- **Large Files**: Very large files may require special handling for memory efficiency.

## Examples

### Display help
**Args:** `io_lib_info --help`
**Explanation:** Shows available options and usage information.

### Convert BAM to SAM
**Args:** `bam2sam input.bam output.sam`
**Explanation:** Convert BAM file to SAM format.

### Convert SAM to BAM
**Args:** `sam2bam input.sam output.bam`
**Explanation:** Convert SAM file to BAM format.

### BAM statistics
**Args:** `bam_stats input.bam`
**Explanation:** Generate statistics from BAM file.

### Extract reads
**Args:** `bam_extract -r chr1:1000-2000 input.bam output.sam`
**Explanation:** Extract reads from specific genomic region.

### CRAM to BAM conversion
**Args:** `cram2bam -r reference.fasta input.cram output.bam`
**Explanation:** Convert CRAM to BAM with reference genome.

### FASTQ quality filtering
**Args:** `fastq_filter -q 20 input.fastq output.fastq`
**Explanation:** Filter FASTQ reads by quality score.

### Validate BAM file
**Args:** `bam_validate input.bam`
**Explanation:** Validate BAM file integrity.
