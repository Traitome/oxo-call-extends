---
name: tigmint
category: assembly
description: Tigmint - Tool for correcting misassemblies using linked-read sequencing data.
tags: [tigmint, assembly-correction, linked-reads, scaffolding, genomics]
author: oxo-call-community
source_url: "https://github.com/bcgsc/tigmint"
---

## Concepts

- **Tool Overview**: Tigmint - A tool for identifying and correcting misassemblies using linked-read sequencing data from technologies like 10x Genomics.
- **Core Function**: Uses linked-read barcode information to detect and fix misassemblies in draft genomes.
- **Input**: Draft assembly (FASTA), linked-read alignments (BAM), barcode information.
- **Output**: Corrected assembly with improved contiguity and accuracy.
- **Installation**: `conda install -c bioconda tigmint`
- **Use Case**: Improving draft genome assemblies, scaffolding, assembly validation.

## Pitfalls

- **Linked-reads Required**: Requires linked-read sequencing data.
- **Barcode Quality**: Analysis depends on barcode completeness and accuracy.

## Examples

### Correct assembly
**Args:** `tigmint-make draft=assembly.fasta reads=linked_reads.bam`
**Explanation:** Correct misassemblies in draft assembly using linked-read data.

### With custom parameters
**Args:** `tigmint -a contigs.fasta -b alignments.bam -o corrected/ -k 21`
**Explanation:** Correct assembly with specified k-mer size.
