---
name: dehomopolymerate
category: utility
description: Tool for removing homopolymer runs from sequences.
tags: [dehomopolymerate, utility, sequence-processing, homopolymer]
author: oxo-call-community
source_url: "https://github.com/lskatz/dehomopolymerate"
---

## Concepts

- **Tool Overview**: dehomopolymerate is a tool for processing nucleotide sequences by removing or collapsing homopolymer runs. It helps reduce sequencing error artifacts, especially from long-read sequencing.
- **Core Function**: Identifies and removes or collapses homopolymer stretches (repeats of the same nucleotide) to improve downstream analysis accuracy.
- **Input/Output**: Input: FASTA/FASTQ sequence files. Output: Processed sequences with reduced homopolymer content.
- **Algorithm**: Uses sliding window approach to detect homopolymer runs and apply user-defined processing rules.
- **Key Features**: Supports multiple output modes (remove, collapse, mask), handles paired-end reads, preserves sequence quality, batch processing.
- **Installation**: `conda install -c bioconda dehomopolymerate`

## Pitfalls

- **Sequence Quality**: May affect biological signal if homopolymers are biologically relevant.
- **Threshold Setting**: Requires careful threshold selection for homopolymer length.
- **Read Pair Consistency**: May create inconsistencies between paired-end reads.
- **Reference Mapping**: Processed reads may map differently to reference.
- **Loss of Information**: Aggressive homopolymer removal may remove biologically important sequences.

## Examples

### Remove homopolymer stretches
**Args:** `dehomopolymerate --input reads.fq --output processed.fq`
**Explanation:** Removes homopolymer stretches from input sequences.

### Collapse homopolymers to fixed length
**Args:** `dehomopolymerate --input reads.fq --output processed.fq --collapse 3`
**Explanation:** Collapses homopolymers to maximum 3 consecutive bases.

### Mask homopolymers instead of removing
**Args:** `dehomopolymerate --input reads.fq --output processed.fq --mask`
**Explanation:** Masks homopolymer regions with N characters.