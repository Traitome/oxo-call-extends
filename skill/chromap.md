---
name: chromap
category: alignment
description: Fast alignment and preprocessing of chromatin profiles (ChIP-seq, ATAC-seq, Hi-C)
tags: [chromap, alignment, chip-seq, atac-seq, hi-c, chromatin, single-cell]
author: oxo-call-community
source_url: "https://github.com/haowenz/chromap"
---

## Concepts

- **Tool Overview**: Chromap is an ultra-fast alignment and preprocessing tool for chromatin profiling data including ChIP-seq, ATAC-seq, scATAC-seq, and Hi-C.
- **Core Function**: Aligns short reads to a reference genome and performs preprocessing (duplicate removal, Tn5 shift, barcode correction) in a single step.
- **Input/Output**: Input: FASTQ reads and reference genome. Output: BED, TagAlign, SAM, or pairs format. Supports gzip-compressed input.
- **Preset Modes**: Provides optimized parameter presets for common assays: `--preset chip`, `--preset atac`, `--preset hic`.
- **Single-Cell Support**: Native barcode handling with whitelist correction, cell-level duplicate removal, and custom read format specification.
- **Two-Step Workflow**: First build index (`-i`), then align reads. Index parameters cannot be changed after creation.
- **Memory Efficient**: Supports `--low-mem` mode for large datasets and `--remove-pcr-duplicates` for deduplication.

## Pitfalls

- **Index Required**: Must build index before alignment. Index parameters (-k, -w) are fixed after creation.
- **Preset Selection**: Always use appropriate preset (`--preset chip/atac/hic`) for best results. Each preset optimizes parameters for the assay type.
- **Output Format**: BED format is recommended for bulk data. SAM output is not fully optimized and may be slower.
- **Barcode Format**: For non-standard barcode positions, use `--read-format` to specify custom layout (e.g., `bc:0:15,r1:16:-1`).
- **Tn5 Shift**: Only apply `--Tn5-shift` for ATAC-seq data. Not applicable for ChIP-seq or Hi-C.
- **Chromosome Order**: For Hi-C pairs format, specify chromosome order with `--chr-order` or `--pairs-natural-chr-order`.

## Examples

### Build reference index
**Args:** `-i -r reference.fa -o ref.index`
**Explanation:** Creates a chromap index from the reference genome, required before any alignment.

### Align ChIP-seq reads
**Args:** `--preset chip -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz -o aln.bed`
**Explanation:** Aligns ChIP-seq paired-end reads using optimized preset, outputs in BED format.

### Align ATAC-seq with Tn5 shift and deduplication
**Args:** `--preset atac -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz --Tn5-shift --remove-pcr-duplicates -o aln.bed`
**Explanation:** Aligns ATAC-seq reads with Tn5 offset correction and PCR duplicate removal for peak calling.

### Align scATAC-seq with barcode correction
**Args:** `--preset atac -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz -b barcode.fq.gz --barcode-whitelist whitelist.txt -o aln.bed`
**Explanation:** Aligns single-cell ATAC-seq reads with barcode whitelist correction, outputs cell-tagged BED format.

### Align Hi-C data in pairs format
**Args:** `--preset hic -x ref.index -r reference.fa -1 read1.fq -2 read2.fq --pairs -o aln.pairs`
**Explanation:** Aligns Hi-C reads and outputs in pairs format for downstream analysis with tools like pairix.

### Output SAM format
**Args:** `--preset chip -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz --SAM -o aln.sam`
**Explanation:** Outputs SAM format for compatibility with tools that require SAM/BAM input.

### Process multiple FASTQ files
**Args:** `--preset chip -x ref.index -r reference.fa -1 s1_r1.fq,s2_r1.fq -2 s1_r2.fq,s2_r2.fq -o aln.bed`
**Explanation:** Aligns multiple FASTQ file pairs using comma-separated lists.

### Custom barcode format
**Args:** `--preset atac -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz -b barcode.fq.gz --read-format bc:0:15,r1:16:-1 -o aln.bed`
**Explanation:** Specifies custom barcode position (first 16bp of read1) for non-standard library preparations.

### Generate alignment summary
**Args:** `--preset atac -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz --summary summary.csv -o aln.bed`
**Explanation:** Produces a summary CSV with per-barcode statistics including total fragments, duplicates, and FRiP estimates.

### Cell-level deduplication for scATAC-seq
**Args:** `--preset atac -x ref.index -r reference.fa -1 read1.fq.gz -2 read2.fq.gz -b barcode.fq.gz --barcode-whitelist whitelist.txt --remove-pcr-duplicates-at-cell-level -o aln.bed`
**Explanation:** Removes PCR duplicates at the cell level (same fragment in same cell) rather than globally, preserving biological duplicates across cells.
