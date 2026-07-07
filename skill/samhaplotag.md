---
name: samhaplotag
category: alignment
description: Process haplotag barcodes in SAM/BAM format
tags: ["samhaplotag", "haplotag", "barcode", "SAM", "phasing"]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/SamHaplotag"
---

## Concepts

- **Tool Overview**: SamHaplotag (v0.0.4) is a tool for processing haplotag barcodes in SAM/BAM alignment files, enabling haplotype-specific read phasing and analysis.
- **Core Function**: Processes haplotag information embedded in read names or tags to phase reads to specific haplotypes, useful for allele-specific expression and phasing analyses.
- **Algorithm**: Parses haplotag barcodes from read identifiers or SAM tags, groups reads by haplotype, and outputs phased alignments.
- **Input Format**: SAM/BAM files with haplotag barcodes in read names or tags.
- **Output Format**: Phased SAM/BAM files, haplotype-specific statistics, phasing reports.
- **Use Case**: Allele-specific expression analysis, haplotype phasing, long-read sequencing analysis.

## Pitfalls

- **Barcode format**: Requires consistent haplotag barcode format in input reads.
- **Read naming**: Barcodes must be properly encoded in read identifiers.
- **Phasing accuracy**: Depends on correct barcode assignment during library preparation.
- **Memory usage**: Large BAM files require significant memory.
- **Performance**: Processing millions of reads can be time-consuming.
- **Tag parsing**: Custom SAM tags may require specific handling.

## Examples

### Phase reads by haplotype
**Args:** `samhaplotag -i input.bam -o phased.bam`
**Explanation:** `-i` input BAM; `-o` phased output BAM.

### Extract specific haplotype
**Args:** `samhaplotag -i input.bam -o hap1.bam --haplotype 1`
**Explanation:** `--haplotype` extracts reads from specific haplotype.

### Barcode in read name
**Args:** `samhaplotag -i input.bam -o phased.bam --barcode-in-name`
**Explanation:** `--barcode-in-name` parses barcode from read name.

### Barcode in tag
**Args:** `samhaplotag -i input.bam -o phased.bam --tag HP`
**Explanation:** `--tag` specifies SAM tag containing haplotype info.

### Output statistics
**Args:** `samhaplotag -i input.bam -o phased.bam -s stats.txt`
**Explanation:** `-s` outputs phasing statistics.

### Filter by quality
**Args:** `samhaplotag -i input.bam -o phased.bam -q 30`
**Explanation:** `-q` minimum mapping quality threshold.

### Split by haplotype
**Args:** `samhaplotag -i input.bam --split -o haplotype_`
**Explanation:** `--split` creates separate BAM files for each haplotype.