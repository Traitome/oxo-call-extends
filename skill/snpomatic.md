---
name: snpomatic
category: alignment
description: SNP-o-matic - Fast and stringent short-read mapping software
tags: [snpomatic, alignment, mapping, snps, short-reads]
author: oxo-call-community
source_url: "https://github.com/magnusmanske/snpomatic"
---

## Concepts

- **Tool Overview**: snpomatic (v1.0) - A fast short-read mapping tool
- **Core Function**: Maps short reads to reference with SNP detection
- **Input/Output**: Accepts FASTQ reads; outputs aligned reads with SNPs
- **Algorithm**: Uses stringent mapping criteria for accurate SNP detection
- **Installation**: `conda install -c bioconda snpomatic`
- **Key Features**: Fast mapping, stringent criteria, SNP detection

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **Reference Quality**: Quality of reference affects mapping accuracy
- **Stringency**: High stringency may reduce sensitivity
- **Memory Usage**: Large datasets require significant memory
- **Read Length**: Designed for specific read length ranges
- **Output Format**: Multiple output formats available

## Examples

### Display help
**Args:** `snpomatic --help`
**Explanation:** Shows available options and usage information.

### Basic mapping
**Args:** `snpomatic -r reference.fasta -i reads.fastq -o aligned.sam`
**Explanation:** Map reads to reference genome.

### Paired-end mapping
**Args:** `snpomatic -r reference.fasta -i reads_1.fastq reads_2.fastq -o aligned.sam`
**Explanation:** Map paired-end reads.

### With SNP output
**Args:** `snpomatic -r reference.fasta -i reads.fastq -o aligned.sam --snps snps.txt`
**Explanation:** Output detected SNPs.

### Set stringency
**Args:** `snpomatic -r reference.fasta -i reads.fastq -o aligned.sam --stringency high`
**Explanation:** Set mapping stringency level.

### With quality filter
**Args:** `snpomatic -r reference.fasta -i reads.fastq -o aligned.sam --min-quality 20`
**Explanation:** Filter by minimum read quality.

### Output BAM format
**Args:** `snpomatic -r reference.fasta -i reads.fastq -o aligned.bam --bam`
**Explanation:** Output alignment in BAM format.

### Generate statistics
**Args:** `snpomatic -r reference.fasta -i reads.fastq -o aligned.sam --stats`
**Explanation:** Output mapping statistics.