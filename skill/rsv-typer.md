---
name: rsv-typer
category: variant_calling
description: Genotyping RSV samples from nanopore sequencing data.
tags: ["rsv-typer", "genotyping", "nanopore", "RSV", "virus"]
author: oxo-call-community
source_url: "https://github.com/DiltheyLab/RSVTyper"
---

## Concepts

- **Tool Overview**: rsv-typer (v0.5.0) is a bioinformatics tool for genotyping Respiratory Syncytial Virus (RSV) from Oxford Nanopore sequencing data. It performs reference-based mapping and variant calling to determine RSV subtypes and genotypes.
- **Core Function**: Takes nanopore sequencing reads and performs alignment to an RSV reference genome, identifies genetic variants, and classifies the sample into RSV A or B subtype with specific genotype assignments.
- **Algorithm**: Uses minimap2 for fast alignment, identifies SNVs and indels, and compares against a curated database of RSV genotypes for classification.
- **Input Format**: FASTQ or FASTA files containing nanopore sequencing reads; can also accept pre-aligned BAM files.
- **Output Format**: VCF file with called variants, JSON report with subtype/genotype classification, and visualization of genome coverage.
- **Use Case**: Clinical diagnostics for RSV infections, surveillance of RSV outbreaks, phylogenetic analysis of RSV strains.

## Pitfalls

- **Requires high-quality reads**: Poor quality nanopore data may lead to incorrect genotype calls.
- **Reference bias**: Uses a single reference genome; divergent strains may be misclassified.
- **Coverage requirements**: Minimum 10x coverage recommended for reliable genotyping.
- **Mixed infections**: Cannot reliably detect mixed RSV subtypes in a single sample.
- **Indel handling**: May miss complex indels or structural variations.
- **Nanopore-specific**: Optimized for nanopore data; Illumina data may require preprocessing.

## Examples

### Basic genotyping
**Args:** `rsv-typer -i reads.fastq -o output_dir`
**Explanation:** `-i` input FASTQ file; `-o` output directory. Performs alignment, variant calling, and genotyping.

### Using pre-aligned BAM
**Args:** `rsv-typer -b aligned.bam -o output_dir`
**Explanation:** `-b` input BAM file with pre-aligned reads. Skips alignment step for faster processing.

### Specify custom reference
**Args:** `rsv-typer -i reads.fastq -r custom_reference.fasta -o output_dir`
**Explanation:** `-r` custom reference genome for alignment and variant calling.

### Generate visualization
**Args:** `rsv-typer -i reads.fastq -o output_dir --plot`
**Explanation:** `--plot` generates coverage plots and genome visualization in the output directory.

### Verbose mode
**Args:** `rsv-typer -i reads.fastq -o output_dir -v`
**Explanation:** `-v` enables verbose output showing detailed processing steps and statistics.

### Minimum coverage filter
**Args:** `rsv-typer -i reads.fastq -o output_dir --min-cov 20`
**Explanation:** `--min-cov` sets minimum coverage threshold (default: 10x) for variant calling.
