---
name: magicblast
category: alignment
description: NCBI BLAST next generation read mapper
tags: [magicblast, alignment, BLAST, RNA-seq]
author: oxo-call-community
source_url: "https://ncbi.github.io/magicblast/"
---

## Concepts

- **Tool Overview**: magicblast v1.7.0 - Magic-BLAST is a tool for mapping large next-generation RNA or DNA sequencing runs against a whole genome or transcriptome with special handling of RNA-seq data.
- **Core Function**: Maps sequencing reads to reference genomes/transcriptomes with support for splice-aware alignment and paired-end data.
- **Input/Output**: Input: FASTQ files; Output: SAM/BAM alignment files.
- **Installation**: `conda install -c bioconda magicblast`
- **Splice-aware Alignment**: Specifically optimized for RNA-seq data with built-in intron detection.
- **Composite Scoring**: Optimizes alignment scores by considering both reads of a pair simultaneously.

## Pitfalls

- **Memory Usage**: Mapping large datasets requires significant memory.
- **Index Building**: Reference index must be built before mapping.
- **Strand Specificity**: RNA-seq strand-specific libraries require special handling.
- **Read Length**: Optimal performance with reads of at least 50bp.
- **Transcriptome Mapping**: Requires proper transcriptome index for splice-aware mapping.
- **Output Format**: Incorrect format specification may cause downstream issues.

## Examples

### Map reads to genome
**Args:** `magicblast -query reads.fastq -db genome -out alignments.sam`
**Explanation:** Maps reads to genomic reference.

### RNA-seq mapping
**Args:** `magicblast -query reads.fastq -db transcriptome -out alignments.sam -splice`
**Explanation:** Performs splice-aware mapping for RNA-seq data.

### Paired-end mapping
**Args:** `magicblast -query read1.fastq -query_mate read2.fastq -db genome -out alignments.sam`
**Explanation:** Maps paired-end reads to reference.

### BAM output
**Args:** `magicblast -query reads.fastq -db genome -out alignments.bam -outfmt bam`
**Explanation:** Outputs alignments in BAM format.

### Strand-specific RNA-seq
**Args:** `magicblast -query reads.fastq -db transcriptome -out alignments.sam -splice -strand plus`
**Explanation:** Handles strand-specific RNA-seq data.

### Build database index
**Args:** `makeblastdb -in genome.fasta -dbtype nucl -out genome`
**Explanation:** Creates BLAST database index.