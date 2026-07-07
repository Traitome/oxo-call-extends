---
name: bwakit
category: alignment
description: Self-contained installation-free package for end-to-end read mapping with BWA
tags: [bwakit, bwa, alignment, mapping, precompiled]
author: oxo-call-community
source_url: "https://github.com/lh3/bwa/tree/master/bwakit"
---

## Concepts

- **Tool Overview**: BWA-kit is a self-consistent, installation-free package containing precompiled BWA binaries and helper scripts.
- **Core Function**: Provides end-to-end read mapping solution including index building, alignment, and post-processing.
- **Features**: Precompiled binaries, reference preparation scripts, and variant calling pipelines.
- **Application**: Complete pipeline for mapping NGS reads to reference genomes.
- **Installation**: Install via bioconda: `conda install -c bioconda bwakit`

## Pitfalls

- **Precompiled Binaries**: May have limited compatibility across different architectures.
- **Reference Preparation**: Requires proper reference genome preparation before alignment.
- **Memory Usage**: Large genomes require significant memory for indexing.
- **Output Format**: Default output may need conversion for downstream tools.

## Examples

### Prepare reference genome
**Args:** `run-bwamem-prep ref.fa`
**Explanation:** Prepares reference genome for BWA alignment (builds index).

### Map reads to reference
**Args:** `run-bwamem ref.fa read1.fq read2.fq > aligned.sam`
**Explanation:** Aligns paired-end reads using BWA-MEM algorithm.

### Complete pipeline with variant calling
**Args:** `run-bwamem ref.fa r1.fq r2.fq | samtools sort -o aligned.bam`
**Explanation:** Maps reads and sorts output using samtools.