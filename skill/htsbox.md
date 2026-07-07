---
name: htsbox
category: utility
description: HTSbox is a fork of early HTSlib. It is a collection of small experimental tools manipulating HTS-related files.
tags: [htsbox, utility, SAM, BAM, CRAM]
author: oxo-call-community
source_url: "https://github.com/lh3/htsbox"
---

## Concepts

- **Tool Overview**: htsbox is a fork of early HTSlib containing experimental utilities for manipulating high-throughput sequencing (HTS) data files including SAM, BAM, and CRAM formats.
- **Core Functionality**: Provides lightweight tools for file conversion, filtering, and basic manipulation of sequencing alignment files.
- **Format Support**: Handles SAM (text), BAM (binary compressed), and CRAM (reference-guided compression) formats.
- **Stream Processing**: Designed for efficient stream-based processing, supporting Unix pipe workflows.
- **Compression**: Built-in support for BGZF compression enabling random access to compressed files.
- **Installation**: `conda install -c bioconda htsbox`

## Pitfalls

- **Version Compatibility**: As a fork of early HTSlib, options may differ from current samtools versions.
- **Format Requirements**: BAM files must be coordinate-sorted for certain operations like indexing.
- **Index Dependencies**: Some operations require index files (.bai for BAM, .csi for CRAM).
- **Memory Considerations**: Large files may require sufficient memory for sorting operations.
- **Reference Requirements**: CRAM format requires access to reference genome for decompression.
- **Performance**: Being experimental, some tools may not be as optimized as samtools equivalents.

## Examples

### Convert SAM to BAM
**Args:** `htsbox view -bS input.sam -o output.bam`
**Explanation:** Converts a SAM file to a compressed BAM file using -b for BAM output and -S to specify SAM input format.

### Sort BAM file
**Args:** `htsbox sort input.bam -o sorted.bam`
**Explanation:** Sorts a BAM file by coordinate position, producing a sorted BAM file ready for indexing.

### Index BAM file
**Args:** `htsbox index sorted.bam`
**Explanation:** Creates a BAM index file (.bai) enabling random access to specific genomic regions.

### Extract reads from region
**Args:** `htsbox view sorted.bam chr1:1,000,000-2,000,000 -o region.bam`
**Explanation:** Extracts reads aligned to a specific genomic region from a sorted and indexed BAM file.

### Convert BAM to CRAM
**Args:** `htsbox view -C -T ref.fasta input.bam -o output.cram`
**Explanation:** Converts BAM to CRAM format using reference-guided compression, reducing file size significantly.