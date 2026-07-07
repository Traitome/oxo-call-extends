---
name: coral
category: expression
description: Efficient tool to bridge paired-end RNA-seq reads
tags: [coral, rna-seq, paired-end, read-bridging, expression]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/coral"
---

## Concepts

- **Tool Overview**: Coral is an efficient tool for bridging paired-end RNA-seq reads, enabling more accurate transcript quantification by connecting fragmented read pairs.
- **Core Function**: Bridges paired-end reads that map to different exons or transcripts, improving mapping completeness and transcript assembly.
- **Algorithm**: Uses splice-aware alignment strategies to bridge gaps between paired reads across introns and transcript boundaries.
- **Input**: Paired-end RNA-seq reads (FASTQ), reference genome or transcriptome.
- **Output**: Bridged read alignments, improved transcriptome assembly, quantification estimates.
- **Application**: RNA-seq data analysis, transcript quantification, alternative splicing detection.
- **Installation**: Install via bioconda: `conda install -c bioconda coral`

## Pitfalls

- **Read Length**: Performance depends on read length and insert size.
- **Splice Sites**: Requires accurate splice site annotations or de novo detection.
- **Mapping Quality**: Low-quality mappings can affect bridging accuracy.
- **Library Prep**: Strand-specific libraries require appropriate handling.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Bridge paired-end reads
**Args:** `coral -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o bridged.bam`
**Explanation:** Bridges paired-end RNA-seq reads against reference genome.

### With strand-specific library
**Args:** `coral -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta --strand-specific -o bridged.bam`
**Explanation:** Handles strand-specific RNA-seq libraries.

### Generate transcript quantification
**Args:** `coral -1 reads_1.fastq -2 reads_2.fastq -t transcripts.fasta -o quantification.txt`
**Explanation:** Quantifies transcript expression using bridged reads.

### Display help
**Args:** `coral --help`
**Explanation:** Shows all available options and usage information.