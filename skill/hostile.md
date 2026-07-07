---
name: hostile
category: utility
description: Hostile is an accurate host decontamination tool for microbial sequencing data, removing human reads while preserving microbial sequences.
tags: [hostile, decontamination, microbial, sequencing]
author: oxo-call-community
source_url: "https://github.com/bede/hostile"
---

## Concepts

- **Host Decontamination**: Hostile removes human host sequences from metagenomic data using subtractive alignment approach, achieving ≥99.6% human read removal while retaining ≥99.989% microbial reads.
- **Alignment Engines**: Supports both Minimap2 (for long reads) and Bowtie2 (for short reads), automatically selecting the appropriate aligner based on input data type.
- **Masked Reference Genome**: Using a masked human reference genome further improves microbial read retention to ≥99.997% with negligible impact on human removal performance.
- **Streaming Processing**: Processes FASTQ files in a streaming manner, supporting gzip-compressed inputs for memory-efficient operation.
- **Paired-End Support**: Properly handles paired-end sequencing data by discarding both mates if either aligns to the host genome.
- **Performance**: Removes 21-23% more human short reads and 21-43 times fewer bacterial reads compared to existing tools, typically in less time.

## Pitfalls

- **Reference Genome Selection**: Using an inappropriate host reference genome can reduce decontamination accuracy; ensure the reference matches the sample source.
- **Read Length Consideration**: Short reads (<50bp) may have reduced alignment specificity, potentially leading to false positives or negatives.
- **Memory Requirements**: Alignment to large reference genomes requires sufficient memory; consider using masked or reduced reference sequences for resource-constrained environments.
- **Compression Handling**: Ensure gzip-compressed inputs are properly formatted; corrupted files may cause processing failures.
- **Output Quality**: Always verify decontamination results with quality metrics to confirm sufficient host removal and microbial retention.
- **Adapter Sequences**: Hostile does not handle adapter trimming; ensure adapters are removed prior to decontamination.

## Examples

### Basic short-read decontamination with Bowtie2
**Args:** `hostile -i input.fastq -o clean.fastq -r hg38`
**Explanation:** Processes short Illumina reads, aligning to hg38 human reference and removing matching sequences while preserving microbial reads.

### Long-read decontamination with Minimap2
**Args:** `hostile -i nanopore_reads.fastq -o clean_nanopore.fastq -r hg38 --aligner minimap2`
**Explanation:** Processes Oxford Nanopore long reads using Minimap2 aligner for more accurate long-read alignment.

### Using masked reference genome
**Args:** `hostile -i input.fastq -o clean.fastq -r hg38_masked.fa --masked`
**Explanation:** Uses a masked human reference genome to further improve microbial read retention, particularly useful for species with high sequence similarity to humans.

### Paired-end processing
**Args:** `hostile -i reads_1.fastq -i reads_2.fastq -o clean_1.fastq -o clean_2.fastq -r hg38`
**Explanation:** Processes paired-end sequencing data, ensuring both mates are discarded if either aligns to the host genome.

### Gzip-compressed input
**Args:** `hostile -i input.fastq.gz -o clean.fastq.gz -r hg38`
**Explanation:** Handles gzip-compressed input and output files directly, saving storage space and processing time.

### Specify output directory
**Args:** `hostile -i input.fastq -r hg38 -d ./clean_data/`
**Explanation:** Processes input file and writes output to specified directory, creating the directory if it doesn't exist.