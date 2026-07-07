---
name: ma
category: alignment
description: MA - The Modular Aligner
tags: [ma, alignment, modular-aligner]
author: oxo-call-community
source_url: "https://github.com/ITBE-Lab/MA"
---

## Concepts

- **Tool Overview**: ma v2.0.2 - MA (Modular Aligner) is a flexible, modular sequence aligner designed for customizable alignment strategies.
- **Core Function**: Provides modular alignment components that can be combined for specific use cases.
- **Input/Output**: Input: FASTA/FASTQ sequence files; Output: Aligned sequences, SAM/BAM files.
- **Installation**: `conda install -c bioconda ma`
- **Modular Design**: Allows selection and combination of different alignment modules.
- **Flexible Configuration**: Supports various alignment strategies through module combinations.

## Pitfalls

- **Module Selection**: Choosing inappropriate modules affects alignment quality.
- **Configuration Complexity**: Multiple configuration options require careful setup.
- **Memory Usage**: Large datasets require significant memory.
- **Performance**: Some module combinations may be slower than specialized aligners.
- **Output Format**: Multiple output formats require proper handling.
- **Learning Curve**: Understanding module interactions requires documentation study.

## Examples

### Basic alignment
**Args:** `ma align -i reads.fastq -r reference.fasta -o aligned.sam`
**Explanation:** Aligns reads to reference sequence.

### With custom modules
**Args:** `ma align -i reads.fastq -r reference.fasta -o aligned.sam -m seed:kmer,ext:smith-waterman`
**Explanation:** Uses k-mer seeding with Smith-Waterman extension.

### Paired-end alignment
**Args:** `ma align -i read1.fastq -j read2.fastq -r reference.fasta -o aligned.sam`
**Explanation:** Aligns paired-end reads.

### BAM output
**Args:** `ma align -i reads.fastq -r reference.fasta -o aligned.bam -f bam`
**Explanation:** Outputs alignments in BAM format.

### Verbose mode
**Args:** `ma align -i reads.fastq -r reference.fasta -o aligned.sam -v`
**Explanation:** Provides detailed logging during alignment.

### Performance mode
**Args:** `ma align -i reads.fastq -r reference.fasta -o aligned.sam -p high`
**Explanation:** Optimizes for high performance.