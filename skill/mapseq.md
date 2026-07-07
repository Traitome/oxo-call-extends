---
name: mapseq
category: metagenomics
description: Open source metagenomic 16S/18S read classifier enabling comparative metagenomics.
tags: [mapseq, metagenomics, 16S, classifier]
author: oxo-call-community
source_url: "https://github.com/jfmrod/MAPseq"
---

## Concepts

- **Tool Overview**: mapseq v2.1.1 - An open source metagenomic 16S/18S read classifier for comparative metagenomics analysis.
- **Core Function**: Classifies 16S/18S rRNA sequences to identify microbial community composition.
- **Input/Output**: Input: FASTQ reads, reference database; Output: Taxonomic classification, abundance profiles.
- **Installation**: `conda install -c bioconda mapseq`
- **16S/18S Analysis**: Specifically designed for ribosomal RNA sequence classification.
- **Comparative Metagenomics**: Enables comparison of metagenomic datasets across samples.

## Pitfalls

- **Reference Database**: Outdated databases affect classification accuracy.
- **Read Quality**: Poor quality reads affect classification.
- **Database Size**: Large databases require significant memory.
- **Taxonomic Resolution**: Limited by database coverage.
- **Chimeric Reads**: Chimeric sequences may produce incorrect classifications.
- **Parameter Tuning**: Incorrect parameters affect classification sensitivity.

## Examples

### Classify reads
**Args:** `mapseq -i reads.fastq -d database/ -o classification.txt`
**Explanation:** Classifies 16S/18S reads using reference database.

### With abundance
**Args:** `mapseq -i reads.fastq -d database/ -o classification.txt --abundance`
**Explanation:** Calculates taxonomic abundance.

### Multiple samples
**Args:** `mapseq -i samples/ -d database/ -o results/`
**Explanation:** Processes multiple samples in batch.

### Verbose mode
**Args:** `mapseq -i reads.fastq -d database/ -o classification.txt -v`
**Explanation:** Provides detailed logging during classification.

### Custom confidence threshold
**Args:** `mapseq -i reads.fastq -d database/ -o classification.txt -c 0.9`
**Explanation:** Sets confidence threshold to 0.9.

### Generate report
**Args:** `mapseq -i reads.fastq -d database/ -o classification.txt --report`
**Explanation:** Generates comprehensive classification report.