---
name: gangstr
category: metagenomics
description: GangSTR is a tool for genome-wide profiling tandem repeats from short reads.
tags: [gangstr, tandem repeats, short reads, genomics]
author: oxo-call-community
source_url: "https://github.com/gymreklab/GangSTR"
---

## Concepts
- **Tandem Repeat Profiling**: Genome-wide profiling of tandem repeats.
- **Short-read Analysis**: Analyzes tandem repeats from short-read sequencing.
- **Expansion Detection**: Detects repeat expansions and contractions.
- **Statistical Modeling**: Uses statistical models for repeat length estimation.
- **Genome-wide**: Profiles repeats across the entire genome.

## Pitfalls
- **Read Depth**: Requires sufficient sequencing depth.
- **Repeat Complexity**: May struggle with highly complex repeats.
- **Allele dropout**: May miss alleles with very long repeats.
- **Short Reads**: Limited by short-read technology.
- **Reference Bias**: May have reference genome bias.

## Examples
### Run GangSTR
**Args:** `gangstr --bam sample.bam --ref reference.fasta --regions repeats.bed --out results`
**Explanation:** Profiles tandem repeats from BAM file.

### With external repeat file
**Args:** `gangstr --bam sample.bam --ref reference.fasta --tre-file repeats.tre --out results`
**Explanation:** Uses external tandem repeat file.

### Specify read length
**Args:** `gangstr --bam sample.bam --ref reference.fasta --regions repeats.bed --readlen 150 --out results`
**Explanation:** Specifies read length for analysis.

### Enable ML genotyping
**Args:** `gangstr --bam sample.bam --ref reference.fasta --regions repeats.bed --ml --out results`
**Explanation:** Enables maximum likelihood genotyping.

### Generate plots
**Args:** `gangstr --bam sample.bam --ref reference.fasta --regions repeats.bed --plot --out results`
**Explanation:** Generates visualization plots.