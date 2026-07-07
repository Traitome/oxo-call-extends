---
name: isoncorrect
category: expression
description: De novo error-correction of long-read transcriptome reads.
tags: [isoncorrect, expression, long reads, error correction, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/ksahlin/isONcorrect"
---

## Concepts

- **De Novo Error Correction**: Corrects sequencing errors in long reads without reference genome.
- **Clustering-Based Correction**: Uses read clustering to identify consensus sequences.
- **Error Detection**: Identifies potential errors by comparing similar reads within clusters.
- **Consensus Generation**: Generates error-free consensus sequences from multiple reads.
- **Nanopore Optimization**: Optimized for Oxford Nanopore sequencing error profiles.
- **Isoform-Aware**: Maintains isoform diversity during error correction.

## Pitfalls

- **Homopolymer Errors**: Difficult to correct homopolymer errors common in long reads.
- **Low Coverage**: Insufficient coverage reduces correction accuracy.
- **Computational Resources**: Requires significant computational resources for large datasets.
- **Memory Requirements**: Memory usage increases with dataset size.
- **Complex Transcriptomes**: Highly complex transcriptomes may reduce correction efficiency.
- **Parameter Tuning**: Optimal parameters depend on specific dataset characteristics.

## Examples

### Basic error correction
**Args:** `isoncorrect --fastq reads.fastq --outfolder corrected/`
**Explanation:** Performs de novo error correction on long-read transcriptome data.

### With clustering
**Args:** `isoncorrect --fastq reads.fastq --cluster --outfolder corrected/`
**Explanation:** Uses clustering for improved error correction accuracy.

### Specify coverage threshold
**Args:** `isoncorrect --fastq reads.fastq --coverage 5 --outfolder corrected/`
**Explanation:** Requires minimum coverage of 5 reads for correction.

### Generate statistics
**Args:** `isoncorrect --fastq reads.fastq --outfolder corrected/ --stats`
**Explanation:** Generates correction statistics and quality metrics.

### Batch processing
**Args:** `isoncorrect --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple samples listed in a batch file.

### Conservative correction
**Args:** `isoncorrect --fastq reads.fastq --conservative --outfolder corrected/`
**Explanation:** Uses conservative correction mode to minimize false corrections.