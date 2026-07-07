---
name: sambamba
category: alignment
description: High-performance SAM/BAM processing toolkit
tags: ["sambamba", "BAM", "SAM", "alignment", "variant calling"]
author: oxo-call-community
source_url: "https://lomereiter.github.io/sambamba/docs/sambamba-view.html"
---

## Concepts

- **Tool Overview**: Sambamba (v1.0.1) is a high-performance toolkit for processing SAM/BAM files, offering fast alternatives to samtools for common operations like sorting, indexing, and variant calling.
- **Core Function**: Provides efficient manipulation of alignment files, including viewing, sorting, indexing, merging, and variant calling operations.
- **Algorithm**: Implements optimized parallel processing for BAM operations, leveraging multithreading for improved performance.
- **Input Format**: SAM/BAM/CRAM alignment files, VCF/BCF variant files.
- **Output Format**: Processed SAM/BAM files, VCF variants, statistics reports.
- **Use Case**: Alignment processing, variant calling, quality control, sequence analysis.

## Pitfalls

- **Memory requirements**: Sorting large BAM files requires significant memory.
- **File permissions**: Requires write permissions for output directories.
- **Format compatibility**: Some rare SAM tags may not be supported.
- **Multi-threading**: Optimal thread count depends on system resources.
- **CRAM support**: Requires reference genome for CRAM operations.
- **Version compatibility**: Older BAM formats may have limited support.

## Examples

### View BAM file
**Args:** `sambamba view input.bam | head -100`
**Explanation:** Views first 100 alignments in SAM format.

### Sort BAM file
**Args:** `sambamba sort -o sorted.bam -t 8 input.bam`
**Explanation:** `-o` output file; `-t` number of threads.

### Index BAM file
**Args:** `sambamba index input.bam`
**Explanation:** Creates BAM index (BAI file).

### Merge BAM files
**Args:** `sambamba merge merged.bam input1.bam input2.bam`
**Explanation:** Merges multiple BAM files into one.

### Mark duplicates
**Args:** `sambamba markdup -o dedup.bam input.bam`
**Explanation:** Marks duplicate reads in BAM file.

### Variant calling
**Args:** `sambamba mpileup -f reference.fasta input.bam | bcftools call -mv -o variants.vcf`
**Explanation:** Generates pileup and calls variants.

### Filter by mapping quality
**Args:** `sambamba view -f bam -o filtered.bam -F "mapping_quality >= 30" input.bam`
**Explanation:** Filters reads with mapping quality >= 30.