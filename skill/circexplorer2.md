---
name: circexplorer2
category: expression
description: Circular RNA analysis toolkit for circRNA identification and characterization
tags: [circexplorer2, circrna, circular-rna, rna-seq, annotation]
author: oxo-call-community
source_url: "https://github.com/YangLab/CIRCexplorer2"
---

## Concepts

- **Tool Overview**: CIRCexplorer2 is an integrated circular RNA analysis toolkit that supports circRNA identification, annotation, and characterization from RNA-seq data.
- **Core Function**: Detects back-spliced junctions (BSJ) from RNA-seq alignments and annotates circRNAs with genomic features.
- **Five Modules**: Align (alignment), Parse (junction extraction), Annotate (genomic annotation), Assemble (full-length assembly), Denovo (de novo detection).
- **Input/Output**: Input: RNA-seq FASTQ files and reference genome. Output: Annotated circRNA list with genomic coordinates and features.
- **One-Step Mode**: Provides `CIRCexplorer2 annotate` for quick annotation from existing BAM files.
- **Multiple Aligners**: Supports TopHat, TopHat2, BWA, STAR, HISAT2, and Bowtie2 for different alignment strategies.

## Pitfalls

- **Alignment Strategy**: Fusion-aware aligners (STAR, TopHat-Fusion) are required for detecting BSJ reads. Standard aligners will miss circRNA junctions.
- **Reference Genome**: Must use the same reference genome version for alignment and annotation (GTF file).
- **Strand Information**: circRNA strand is inferred from splice site signals. Ensure correct library preparation type.
- **Low Expression**: circRNAs are often lowly expressed. Sufficient sequencing depth is required for reliable detection.
- **False Positives**: Filter results by junction read count (minimum 2 reads recommended) to reduce false positives.

## Examples

### Full pipeline: align and parse
**Args:** `CIRCexplorer2 align -G /path/to/genome.fa -r /path/to/reads.fq -o align_output --STAR`
**Explanation:** Aligns RNA-seq reads using STAR in chimeric mode to detect back-spliced junctions.

### Parse junctions from alignment
**Args:** `CIRCexplorer2 parse -t STAR -b align_output.bam -o parsed_junctions.txt`
**Explanation:** Extracts back-spliced junction reads from the STAR-aligned BAM file.

### Annotate circRNAs
**Args:** `CIRCexplorer2 annotate -r parsed_junctions.txt -g /path/to/annotation.gtf -o annotated_circrnas.txt -b /path/to/genome.fa`
**Explanation:** Annotates detected circRNAs with gene names, exon/intron features, and genomic coordinates using the GTF annotation.

### One-step annotation from BAM
**Args:** `CIRCexplorer2 annotate -r junctions.txt -g annotation.gtf -b genome.fa -o output.txt --bed`
**Explanation:** Quick annotation of pre-extracted junctions, outputs BED format for downstream analysis.

### Assemble full-length circRNAs
**Args:** `CIRCexplorer2 assemble -r annotated_circrnas.txt -g annotation.gtf -b genome.fa -j junctions.bam -o assembled.fa`
**Explanation:** Reconstructs full-length circRNA sequences from annotated junctions and alignment data.

### De novo circRNA detection
**Args:** `CIRCexplorer2 denovo -G genome.fa -r reads.fq -o denovo_output`
**Explanation:** Performs de novo circRNA detection without relying on existing annotation, useful for discovering novel circRNAs.
