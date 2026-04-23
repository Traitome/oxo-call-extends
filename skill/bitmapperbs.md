---
name: bitmapperbs
category: epigenomics
description: Fast and accurate read aligner for whole-genome bisulfite sequencing
tags: [bitmapperbs, bisulfite, methylation, alignment, wgbs]
author: oxo-call-community
source_url: "https://github.com/chhylp123/BitMapperBS"
---

## Concepts

- **Tool Overview**: BitMapperBS is a fast and accurate aligner specifically designed for whole-genome bisulfite sequencing (WGBS) data.
- **Core Function**: Maps bisulfite-converted reads to reference genome while accounting for C-to-T conversions.
- **Algorithm**: Uses bitmap-based indexing for efficient bisulfite read alignment.
- **Input**: Bisulfite-treated FASTQ files and reference genome.
- **Output**: SAM/BAM alignment files with methylation-aware mapping.
- **Installation**: Install via bioconda: `conda install -c bioconda bitmapperbs`

## Pitfalls

- **Reference Preparation**: Reference genome must be indexed before alignment.
- **Strand Direction**: Bisulfite libraries can be directional or non-directional; specify correctly.
- **Conversion Rate**: Low bisulfite conversion rates can affect alignment accuracy.
- **Memory Usage**: Large genomes require significant memory for indexing.

## Examples

### Index reference genome
**Args:** `BitMapperBS index reference.fa`
**Explanation:** Builds index for bisulfite-aware alignment of reference genome.

### Align single-end bisulfite reads
**Args:** `BitMapperBS align -r reference.fa -1 reads.fq -o aligned.sam`
**Explanation:** Aligns single-end bisulfite reads to reference genome.

### Align paired-end bisulfite reads
**Args:** `BitMapperBS align -r reference.fa -1 R1.fq -2 R2.fq -o aligned.sam`
**Explanation:** Aligns paired-end bisulfite reads with proper pair handling.

### Multi-threaded alignment
**Args:** `BitMapperBS align -r reference.fa -1 reads.fq -t 8 -o aligned.sam`
**Explanation:** Uses 8 threads for faster bisulfite read alignment.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
