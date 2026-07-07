---
name: last
category: alignment
description: Finds and aligns related regions of sequences - good for rearrangements and DNA-protein alignments
tags: [last, alignment, sequence-alignment, genomics, comparative-genomics]
author: oxo-call-community
source_url: "https://gitlab.com/mcfrith/last"
---

## Concepts

- **Rearrangement Detection**: Excellent for finding genome rearrangements
- **DNA-Protein Alignment**: Aligns DNA sequences to proteins
- **Sensitive DNA Search**: Sensitive DNA-DNA similarity search
- **AT-rich DNA**: Handles AT-rich genomes well
- **Large-scale Alignment**: Scales to whole genome comparisons
- **Moderate Data Size**: Designed for moderately large datasets

## Pitfalls

- **Database Size**: Very large databases increase memory usage
- **Parameter Tuning**: Default parameters may not suit all needs
- **Computational Time**: Large alignments take significant time
- **Score Estimation**: E-value estimation can be complex
- **Memory Usage**: Index construction requires substantial memory
- **Format Compatibility**: Output formats differ from BLAST

## Examples

### Index database
**Args:** `lastdb -uNEAR mydb reference.fasta`
**Explanation:** Builds LAST database with NEAR seeding scheme.

### Align reads
**Args:** `lastal -Q1 mydb reads.fastq > alignments.maf`
**Explanation:** Maps FASTQ reads against indexed database.

### DNA vs protein
**Args:** `lastal -fMaf -d mydb dna.fasta > alignments.maf`
**Explanation:** Aligns DNA to protein database.

### Find rearrangements
**Args:** `lastal -Q1 mydb query.fasta | last-map9.py > results.maf`
**Explanation:** Identifies rearranged regions.

### Set scoring matrix
**Args:** `lastal -m 1 mydb query.fasta > alignments.maf`
**Explanation:** Uses scoring matrix for DNA.

### Convert formats
**Args:** `maf-convert.py fasta alignments.maf > alignments.fasta`
**Explanation:** Converts MAF to FASTA format.