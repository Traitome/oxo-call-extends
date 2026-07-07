---
name: clair3-trio
category: variant-calling
description: Deep learning-based variant caller for family trios from nanopore long-reads
tags: [clair3-trio, variant-calling, long-reads, trio, deep-learning, mendelian-inheritance]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/Clair3-Trio"
---

## Concepts

- **Tool Overview**: Clair3-Trio is a specialized variant caller for family trios using nanopore long-read sequencing data, employing a Trio-to-Trio deep neural network model.
- **Core Function**: Calls variants from trio sequencing data (father, mother, child) while leveraging Mendelian inheritance priors for improved accuracy.
- **Algorithm**: Uses MCVLoss (Mendelian Constraint Violation Loss) to explicitly encode inheritance priors, reducing Mendelian violations.
- **Input**: Aligned BAM files for trio members and reference genome (FASTA).
- **Output**: VCF file with variant calls for all trio members.
- **Application**: Family-based variant calling, rare disease research, and population genetics.
- **Installation**: Install via bioconda: `conda install -c bioconda clair3-trio`

## Pitfalls

- **Trio Data Requirement**: Requires complete trio data (father, mother, child).
- **Model Compatibility**: Designed specifically for ONT long-read data.
- **Reference Genome**: Must use the same reference genome for all trio members.
- **Computational Resources**: Requires significant memory and GPU resources.
- **Alignment Quality**: Depends on accurate alignment of all trio samples.

## Examples

### Call variants from trio data
**Args:** `run_clair3_trio.sh -b father.bam,mother.bam,child.bam -r reference.fasta -o output_dir`
**Explanation:** Calls variants from trio ONT sequencing data.

### With GPU acceleration
**Args:** `run_clair3_trio.sh -b father.bam,mother.bam,child.bam -r reference.fasta -o output_dir --gpu`
**Explanation:** Uses GPU for faster trio variant calling.

### Targeted sequencing
**Args:** `run_clair3_trio.sh -b father.bam,mother.bam,child.bam -r reference.fasta -o output_dir --bed targets.bed`
**Explanation:** Calls variants only in specified genomic regions.

### Display help
**Args:** `run_clair3_trio.sh --help`
**Explanation:** Shows all available options and usage information.