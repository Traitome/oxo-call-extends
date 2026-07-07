---
name: ksnp
category: variant-calling
description: K-mer based SNP discovery and haplotype assembly
tags: [ksnp, variant-calling, SNP, k-mer, haplotype, genomics]
author: oxo-call-community
source_url: "https://github.com/zhouqiansolab/KSNP"
---

## Concepts

- **K-mer Based SNP Calling**: Uses k-mers for SNP discovery
- **Haplotype Assembly**: Assembles haplotypes from sequencing data
- **Reference-free**: Can work without reference genome
- **SNP Detection**: Identifies single nucleotide polymorphisms
- **Multiple Genomes**: Compares multiple genome sequences
- **Phylogenetic Analysis**: Supports phylogenetic tree construction

## Pitfalls

- **K-mer Size**: K-mer size affects SNP detection sensitivity
- **Genome Coverage**: Low coverage affects haplotype assembly
- **Repeated Regions**: Repetitive sequences cause ambiguous mapping
- **heterozygosity**: High heterozygosity complicates assembly
- **Computational Resources**: Large genomes require significant memory
- **Parameter Selection**: Parameters need optimization for different data

## Examples

### Call SNPs
**Args:** `kSNP3 -in input.list -outdir output -k 21`
**Explanation:** Calls SNPs from assembled genomes using 21-mers.

### Specify k-mer size
**Args:** `kSNP3 -in input.list -outdir output -k 31`
**Explanation:** Uses k-mer size of 31 for SNP calling.

### Create genome list
**Args:** `kSNP3 -in genomes.txt -outdir results -k 25`
**Explanation:** Calls SNPs from list of genome files.

### Generate phylogeny
**Args:** `kSNP3 -in input.list -outdir output -k 21 - phylogeny`
**Explanation:** Also constructs phylogenetic tree.

### Filter SNPs
**Args:** `kSNP3 -in input.list -outdir output -k 21 -filter`
**Explanation:** Filters low-quality SNP calls.

### Annotate SNPs
**Args:** `kSNP3 -in input.list -outdir output -k 21 -annotate annotations.gff`
**Explanation:** Annotates identified SNPs.