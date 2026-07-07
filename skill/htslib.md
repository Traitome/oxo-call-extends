---
name: htslib
category: formatting
description: HTSlib is a C library for reading and writing high-throughput sequencing data formats including SAM, BAM, CRAM, VCF, and BCF.
tags: [htslib, formatting, SAM, BAM, CRAM, VCF, library]
author: oxo-call-community
source_url: "http://www.htslib.org/"
---

## Concepts

- **Library Overview**: HTSlib is a foundational C library providing I/O operations for standard bioinformatics data formats.
- **Format Support**: Core support for SAM, BAM, CRAM (alignment formats) and VCF, BCF (variant formats).
- **Compression**: Built-in BGZF compression support enabling efficient storage and random access.
- **Indexing**: Supports BAI and CSI indexing for fast random access to genomic regions.
- **Reference-Guided Compression**: CRAM format uses reference genome for highly efficient compression.
- **Installation**: `conda install -c bioconda htslib`

## Pitfalls

- **C Library**: Requires C/C++ development skills for direct integration; use wrappers for other languages.
- **Memory Management**: Manual memory management required when using C API directly.
- **Format Versions**: Different versions of CRAM may require specific library versions.
- **Reference Requirements**: CRAM decompression requires access to the reference genome used during compression.
- **Concurrency**: Thread safety considerations when using library in multi-threaded applications.
- **API Stability**: Some API functions may change between major versions.

## Examples

### Build FASTA index
**Args:** `samtools faidx reference.fasta`
**Explanation:** Creates an index (.fai) for a FASTA file to enable random access using htslib.

### Convert SAM to BAM
**Args:** `samtools view -bS input.sam -o output.bam`
**Explanation:** Converts a SAM file to compressed BAM format using htslib via samtools.

### Sort and index BAM
**Args:** `samtools sort input.bam -o sorted.bam && samtools index sorted.bam`
**Explanation:** Sorts a BAM file by coordinate and creates an index for random access.

### Query specific region
**Args:** `samtools view sorted.bam chr1:1,000,000-2,000,000 > region.sam`
**Explanation:** Extracts reads from a specific genomic region using htslib's random access capabilities.

### Convert BAM to CRAM
**Args:** `samtools view -C -T ref.fasta input.bam -o output.cram`
**Explanation:** Converts BAM to CRAM format using reference-guided compression for reduced file size.