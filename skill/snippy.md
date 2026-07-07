---
name: snippy
category: variant-analysis
description: Snippy - Rapid bacterial SNP calling and core genome alignment pipeline
tags: [snippy, variant-analysis, bacterial, snps, alignment, pipeline]
author: oxo-call-community
source_url: "https://github.com/tseemann/snippy"
---

## Concepts

- **Tool Overview**: snippy (v4.6.0) - A pipeline for rapid bacterial SNP calling
- **Core Function**: Calls SNPs from bacterial genomes and creates core genome alignments
- **Input/Output**: Accepts FASTQ reads and reference; outputs VCF and alignments
- **Algorithm**: Integrates alignment, variant calling, and core genome analysis
- **Installation**: `conda install -c bioconda snippy`
- **Key Features**: Rapid SNP calling, core genome alignment, bacterial analysis

## Pitfalls

- **Reference Quality**: Requires high-quality reference genome
- **Input Format**: Requires properly formatted FASTQ files
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for alignment
- **Bacterial Specific**: Designed for bacterial genomes, not eukaryotes
- **Coverage Requirements**: Requires sufficient read coverage

## Examples

### Display help
**Args:** `snippy --help`
**Explanation:** Shows available options and usage information.

### Basic SNP calling
**Args:** `snippy --cpus 8 --outdir results/ --ref reference.fasta --R1 reads_1.fastq --R2 reads_2.fastq`
**Explanation:** Call SNPs from paired-end reads.

### Single-end reads
**Args:** `snippy --outdir results/ --ref reference.fasta --R1 reads.fastq`
**Explanation:** Call SNPs from single-end reads.

### Core genome alignment
**Args:** `snippy-core results1/ results2/ results3/ -o core_alignment/`
**Explanation:** Create core genome alignment from multiple samples.

### With custom parameters
**Args:** `snippy --outdir results/ --ref reference.fasta --R1 reads.fastq --minfrac 0.9`
**Explanation:** Set minimum allele fraction threshold.

### Quick run
**Args:** `snippy --outdir results/ --ref reference.fasta --R1 reads.fastq --quick`
**Explanation:** Run quick SNP calling.

### Generate report
**Args:** `snippy --outdir results/ --ref reference.fasta --R1 reads.fastq --report`
**Explanation:** Generate analysis report.

### Multi-sample analysis
**Args:** `snippy-multi samples.txt --ref reference.fasta --outdir multi_results/`
**Explanation:** Analyze multiple samples in batch.