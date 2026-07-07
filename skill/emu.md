---
name: emu
category: metagenomics
description: "Emu is a relative abundance estimator for 16s genomic data."
tags: [emu, metagenomics, 16S, abundance-estimation, microbiome]
author: oxo-call-community
source_url: "https://github.com/treangenlab/emu"
---

## Concepts

- **Tool Overview**: Emu is a bioinformatics tool for estimating relative abundance of microbial taxa from 16S rRNA gene sequencing data.
- **Core Function**: Uses a reference database to classify 16S reads and estimate taxonomic composition of microbial communities.
- **Input/Output**: Input: 16S sequencing reads (FASTQ). Output: Taxonomic abundance table, classification reports.
- **Algorithm**: Uses k-mer based classification with probabilistic scoring for accurate taxonomic assignment.
- **Key Features**: High-speed classification, accurate abundance estimation, support for paired-end reads, comprehensive taxonomic ranks, visualization support.
- **Installation**: `conda install -c bioconda emu`

## Pitfalls

- **Reference Database**: Requires appropriate 16S reference database.
- **Read Length**: Performance depends on read length and quality.
- **Database Updates**: Reference database should be updated regularly.
- **Memory Usage**: Large databases require significant memory.
- **Taxonomic Resolution**: Resolution depends on reference database completeness.

## Examples

### Basic abundance estimation
**Args:** `emu abundance -i reads.fastq -o abundance.tsv`
**Explanation:** Estimates taxonomic abundance from 16S reads.

### With paired-end reads
**Args:** `emu abundance -1 reads_1.fastq -2 reads_2.fastq -o abundance.tsv`
**Explanation:** Processes paired-end 16S sequencing reads.

### Specify database
**Args:** `emu abundance -i reads.fastq -o abundance.tsv -d custom_db`
**Explanation:** Uses custom reference database for classification.

### Generate visualization
**Args:** `emu plot -i abundance.tsv -o plot.pdf`
**Explanation:** Generates visualization of taxonomic composition.

### Batch processing
**Args:** `emu abundance -i samples/ -o results/ --batch`
**Explanation:** Processes multiple samples in batch mode.