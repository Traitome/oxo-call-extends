---
name: smalt
category: alignment
description: SMALT aligns DNA sequencing reads with a reference genome using a seed-and-extend approach
tags: [smalt, alignment, dna-sequencing, mapping, ngs]
author: oxo-call-community
source_url: "https://www.sanger.ac.uk/tool/smalt"
---

## Concepts

- **Tool Overview**: smalt (v0.7.6) - A fast DNA sequence aligner for NGS data
- **Core Function**: Aligns sequencing reads to reference genome using seed-and-extend
- **Input/Output**: Accepts FASTA/FASTQ reads; outputs SAM/BAM alignments
- **Algorithm**: Implements Burrows-Wheeler Transform for fast seed finding
- **Installation**: `conda install -c bioconda smalt`
- **Key Features**: Fast alignment, supports paired-end reads, flexible parameters

## Pitfalls

- **Index Building**: Requires pre-built index for reference genome
- **Read Length**: Performance varies with read length
- **Memory Usage**: Large genomes require significant memory for indexing
- **Sensitivity/Speed**: Trade-off between alignment sensitivity and speed
- **Paired-End Handling**: Requires proper mate pairing information
- **Output Size**: BAM files can be very large for high-coverage data

## Examples

### Display help
**Args:** `smalt --help`
**Explanation:** Shows available options and usage information.

### Build index
**Args:** `smalt index -k 13 -s 4 reference index_prefix`
**Explanation:** Build index for reference genome with k=13.

### Align single-end reads
**Args:** `smalt map -f sam -o output.sam index_prefix reads.fastq`
**Explanation:** Align single-end reads to reference.

### Align paired-end reads
**Args:** `smalt map -f sam -o output.sam index_prefix reads_1.fastq reads_2.fastq`
**Explanation:** Align paired-end reads to reference.

### Output BAM format
**Args:** `smalt map -f bam -o output.bam index_prefix reads.fastq`
**Explanation:** Output alignments in BAM format.

### Increase sensitivity
**Args:** `smalt map -f sam -o output.sam -n 10 index_prefix reads.fastq`
**Explanation:** Increase number of seeds for better sensitivity.

### Filter by mapping quality
**Args:** `smalt map -f sam -o output.sam -q 30 index_prefix reads.fastq`
**Explanation:** Filter reads with mapping quality < 30.

### Local alignment
**Args:** `smalt map -f sam -o output.sam -l index_prefix reads.fastq`
**Explanation:** Perform local alignment instead of end-to-end.