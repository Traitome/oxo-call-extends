---
name: staphscan
category: population-genomics
description: A tool for Staphylococcus aureus analysis and population genomics.
tags: [staphscan, staphylococcus, population-genomics, typing]
author: oxo-call-community
source_url: "https://staphscan.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: staphscan (v0.3.0) is a comprehensive tool for analyzing Staphylococcus aureus genomes, including MLST typing, SNP calling, and phylogenetic analysis.
- **Core Function**: Provides end-to-end analysis pipeline for S. aureus population genomics studies.
- **Workflow Components**: Quality control → SNP calling → MLST typing → phylogenetic tree construction.
- **Input/Output**: Input: FASTQ reads or VCF files; Output: Typing results, SNP matrices, and phylogenetic trees.
- **Population Analysis**: Supports core genome alignment and SNP-based phylogenetic reconstruction.
- **Installation**: `conda install -c bioconda staphscan` or download from GitHub.

## Pitfalls

- **Reference Genome**: Must use appropriate S. aureus reference genome for accurate SNP calling.
- **Read Quality**: Poor quality reads affect SNP calling accuracy.
- **Assembly Required**: Some analyses require prior genome assembly.
- **Memory Requirements**: Large datasets may require significant memory.
- **Computational Time**: Phylogenetic analysis of large populations can be time-consuming.
- **Database Updates**: Outdated MLST databases may miss new alleles.

## Examples

### Display help
**Args:** `staphscan --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `staphscan -i reads.fastq -o results/ -r reference.fasta`
**Explanation:** Run complete analysis pipeline on sequencing reads.

### SNP calling
**Args:** `staphscan snp -i reads.fastq -r reference.fasta -o snps.vcf`
**Explanation:** Call SNPs from sequencing reads.

### MLST typing
**Args:** `staphscan mlst -i genome.fasta -o mlst_results.txt`
**Explanation:** Perform MLST typing on genome assembly.

### Phylogenetic analysis
**Args:** `staphscan tree -i snps.vcf -o tree.nwk`
**Explanation:** Build phylogenetic tree from SNP matrix.

### Quality filtering
**Args:** `staphscan -i reads.fastq -o results/ -q 20`
**Explanation:** Apply quality filter with minimum Phred score.

### Verbose mode
**Args:** `staphscan -i reads.fastq -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Batch processing
**Args:** `staphscan batch -c samples.txt -o results/`
**Explanation:** Process multiple samples from batch file.
