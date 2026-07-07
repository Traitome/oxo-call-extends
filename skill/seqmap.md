---
name: seqmap
category: alignment
description: seqmap - Map oligonucleotides to reference genome
tags: ["seqmap", "alignment", "short-reads", "oligonucleotide"]
author: oxo-call-community
source_url: "http://www-personal.umich.edu/~jianghui/seqmap"
---

## Concepts

- **Tool Overview**: seqmap (v1.0.13) maps large amounts of oligonucleotides to the genome.
- **Core Function**: Aligns short reads/oligonucleotides to reference sequences.
- **Algorithm**: Implements efficient short-read mapping algorithm.
- **Input/Output**: Accepts FASTQ/FASTA files and produces SAM/BAM alignments.
- **Short Read Mapping**: Focuses on mapping short oligonucleotide sequences.
- **Applications**: Small RNA sequencing, primer mapping, and targeted sequencing.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Map reads
**Args:** `seqmap -d reference.fasta -i reads.fastq -o alignments.sam`
**Explanation:** `-d` reference; `-i` input reads; `-o` output SAM.

### With mismatches
**Args:** `seqmap -d reference.fasta -i reads.fastq -m 2 -o alignments.sam`
**Explanation:** `-m 2` allows 2 mismatches.

### Threads
**Args:** `seqmap -d reference.fasta -i reads.fastq -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 threads.

### Verbose logging
**Args:** `seqmap -d reference.fasta -i reads.fastq -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqmap --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqmap --version`
**Explanation:** Shows current version.

### Output BAM
**Args:** `seqmap -d reference.fasta -i reads.fastq -b -o alignments.bam`
**Explanation:** `-b` outputs BAM format.