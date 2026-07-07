---
name: smallgenomeutilities
category: virus-analysis
description: A collection of scripts useful for dealing with viral RNA NGS data
tags: [smallgenomeutilities, virus-analysis, rna-seq, viral-genomics, ngs]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/smallgenomeutilities"
---

## Concepts

- **Tool Overview**: smallgenomeutilities (v0.5.2) - A collection of utilities for viral RNA sequencing data analysis
- **Core Function**: Provides tools for processing and analyzing viral NGS data
- **Input/Output**: Accepts FASTA/FASTQ/BAM files; outputs processed sequences and reports
- **Algorithm**: Various bioinformatics algorithms for viral genome analysis
- **Installation**: `conda install -c bioconda smallgenomeutilities`
- **Key Features**: Collection of specialized tools, optimized for viral genomes

## Pitfalls

- **Virus Specific**: Designed specifically for viral genomes
- **Input Quality**: Requires high-quality sequencing data
- **Reference Dependence**: Many tools require reference genome
- **Assembly Quality**: Results depend on input assembly quality
- **Coverage Depth**: Low coverage affects variant calling accuracy
- **Mixed Infections**: May struggle with mixed viral populations

## Examples

### Display help
**Args:** `smallgenomeutilities --help`
**Explanation:** Shows available utilities and usage information.

### Trim adapters
**Args:** `sgu-trim -i reads.fastq -o trimmed.fastq -a adapters.fa`
**Explanation:** Trim adapter sequences from viral reads.

### Map reads to reference
**Args:** `sgu-map -i reads.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Map reads to viral reference genome.

### Call variants
**Args:** `sgu-variant -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads.

### Consensus sequence
**Args:** `sgu-consensus -i aligned.bam -r reference.fasta -o consensus.fasta`
**Explanation:** Generate consensus sequence from alignments.

### Coverage analysis
**Args:** `sgu-coverage -i aligned.bam -o coverage.txt`
**Explanation:** Calculate coverage depth across genome.

### Quality control
**Args:** `sgu-qc -i reads.fastq -o qc_report.html`
**Explanation:** Generate QC report for viral sequencing data.