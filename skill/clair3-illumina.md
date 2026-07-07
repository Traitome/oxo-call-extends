---
name: clair3-illumina
category: variant-calling
description: Clair3 variant caller with Illumina short-read support
tags: [clair3-illumina, variant-calling, illumina, deep-learning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/Clair3"
---

## Concepts

- **Tool Overview**: clair3-illumina provides Clair3 variant calling with optimized libraries for Illumina short-read sequencing data.
- **Core Function**: Accurate variant calling from Illumina sequencing data using deep learning models.
- **Algorithm**: Uses neural networks to predict variants from aligned sequencing reads.
- **Input**: Aligned BAM file and reference genome (FASTA).
- **Output**: Variant calls in VCF format.
- **Application**: SNP and indel calling from Illumina sequencing data.
- **Installation**: Install via bioconda: `conda install -c bioconda clair3-illumina`

## Pitfalls

- **Model Compatibility**: Requires Illumina-specific models for optimal performance.
- **BAM Quality**: Requires properly aligned reads with good mapping quality.
- **Reference Genome**: Must match the reference used for alignment.
- **Computational Resources**: Requires GPU for fast inference (CPU supported but slower).
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Call variants from Illumina reads
**Args:** `run_clair3.sh -b reads.bam -r reference.fasta -o output_dir --platform illumina`
**Explanation:** Calls variants from Illumina aligned reads using Clair3.

### With GPU acceleration
**Args:** `run_clair3.sh -b reads.bam -r reference.fasta -o output_dir --platform illumina --gpu`
**Explanation:** Uses GPU for faster variant calling.

### Targeted sequencing
**Args:** `run_clair3.sh -b reads.bam -r reference.fasta -o output_dir --platform illumina --bed targets.bed`
**Explanation:** Calls variants only in specified genomic regions.

### Display help
**Args:** `run_clair3.sh --help`
**Explanation:** Shows all available options and usage information.