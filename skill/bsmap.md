---
name: bsmap
category: epigenomics
description: Short reads mapping software for bisulfite sequencing reads
tags: [bsmap, bisulfite, methylation, alignment, wgbs]
author: oxo-call-community
source_url: "https://code.google.com/archive/p/bsmap/"
---

## Concepts

- **Tool Overview**: BSMAP maps bisulfite-treated short reads to reference genomes for methylation analysis.
- **Core Function**: Aligns bisulfite-converted reads while accounting for C-to-T conversions.
- **Algorithm**: Uses wildcard matching for efficient bisulfite alignment.
- **Input**: Bisulfite FASTQ files and reference genome FASTA.
- **Output**: SAM alignment and methylation ratio files.
- **Installation**: Install via bioconda: `conda install -c bioconda bsmap`

## Pitfalls

- **Reference Indexing**: Must index reference before alignment.
- **Strand Specificity**: Specify correct library strand direction.
- **Memory Usage**: Large genomes require significant memory.
- **Output Format**: SAM output may need conversion for downstream tools.

## Examples

### Index reference genome
**Args:** `bsmap -a reads.fq -d genome.fa -o aligned.sam`
**Explanation:** Aligns bisulfite reads to reference genome outputting SAM format.

### Paired-end alignment
**Args:** `bsmap -a R1.fq -b R2.fq -d genome.fa -o paired.sam`
**Explanation:** Aligns paired-end bisulfite reads.

### Multi-threaded alignment
**Args:** `bsmap -a reads.fq -d genome.fa -p 8 -o aligned.sam`
**Explanation:** Uses 8 threads for faster bisulfite alignment.

### Calculate methylation ratios
**Args:** `methratio.py -r genome.fa -i aligned.sam -o methylation.tsv`
**Explanation:** Calculates methylation ratios from BSMAP alignments.

### Set maximum mismatches
**Args:** `bsmap -a reads.fq -d genome.fa -v 3 -o aligned.sam`
**Explanation:** Allows up to 3 mismatches in alignment.
