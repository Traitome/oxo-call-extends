---
name: dart
category: alignment
description: Dart - fast and accurate RNA-seq mapper
tags: [dart, alignment, RNA-seq, mapping, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/hsinnan75/Dart"
---

## Concepts

- **Tool Overview**: dart (v1.4.6+) is a fast and accurate RNA-seq read mapper designed for efficient alignment of transcriptomic data.
- **Core Function**: Aligns RNA-seq reads to reference genomes with splice junction awareness.
- **Input/Output**: Input: FASTQ reads, reference genome. Output: SAM/BAM alignments.
- **Algorithm**: Uses seed-and-extend approach with splice-aware alignment for accurate transcript mapping.
- **Key Features**: Splice junction detection, fast performance, supports paired-end reads.
- **Installation**: `conda install -c bioconda dart`

## Pitfalls

- **Splice Junction Detection**: Requires known or predicted splice sites for optimal performance.
- **Read Length**: Performance may vary with different read lengths.
- **Memory Usage**: Large genomes may require significant memory.
- **Multi-mapping**: May produce multiple mappings for reads with repetitive sequences.
- **Strand Specificity**: Requires proper handling of strand-specific RNA-seq protocols.

## Examples

### Map RNA-seq reads
**Args:** `dart -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Map RNA-seq reads to reference genome with splice-aware alignment.

### Paired-end mapping
**Args:** `dart -1 R1.fastq -2 R2.fastq -r reference.fasta -o alignments.bam`
**Explanation:** Map paired-end RNA-seq reads to reference genome.

### Specify splice junctions
**Args:** `dart -i reads.fastq -r reference.fasta -j junctions.bed -o alignments.sam`
**Explanation:** Use known splice junctions for improved mapping accuracy.
