---
name: crossfilt
category: alignment
description: Tools to filter reads causing alignment bias in cross-species genomic comparisons using GC content normalization
tags: [crossfilt, alignment, bias, GC-content, cross-species, read-filtering, genomics]
author: oxo-call-community
source_url: "https://github.com/kennethabarr/CrossFilt"
---

## Concepts

- **Tool Overview**: CrossFilt (v0.2.1+) - Tools to filter reads causing alignment bias in cross-species genomic comparisons.
- **Core Function**: Identifies and removes reads whose alignment is biased by GC content differences between query and reference genomes, improving accuracy in cross-species sequence comparisons.
- **Algorithm**: (1) Calculates GC content of query sequences. (2) Compares GC distribution to expected distribution. (3) Identifies reads with biased alignment likelihood. (4) Filters out problematic reads.
- **Input**: FASTQ/FASTA files, reference genome, optional BAM/SAM alignments.
- **Output**: Filtered FASTQ/FASTA files, bias reports.
- **Application**: Cross-species genomics, metagenomics, phylogenomics, ancient DNA analysis.
- **Installation**: `conda install -c bioconda crossfilt` or `pip install crossfilt`

## Pitfalls

- **Reference Required**: Needs reference genome for GC content comparison; results less meaningful without proper reference.
- **Paired-end Handling**: Ensure proper pairing of reads when filtering paired-end data.
- **Bias Threshold**: Adjust GC bias threshold based on divergence between species; highly divergent species may need stricter filtering.

## Examples

### Filter biased reads from FASTQ
**Args:** `crossfilt -i input.fastq -r reference.fasta -o filtered.fastq`
**Explanation:** Filter reads from input FASTQ that show alignment bias compared to reference genome.

### Filter with GC content normalization
**Args:** `crossfilt -i input.fastq -r reference.fasta --gc-norm -o filtered.fastq`
**Explanation:** Apply GC content normalization during filtering to account for systematic GC differences.

### Generate bias report
**Args:** `crossfilt -i input.fastq -r reference.fasta --report bias_report.txt -o filtered.fastq`
**Explanation:** Output detailed report of reads filtered and bias statistics.

### Paired-end filtering
**Args:** `crossfilt -i R1.fastq -i2 R2.fastq -r reference.fasta -o R1_filtered.fastq -o2 R2_filtered.fastq`
**Explanation:** Filter paired-end reads, maintaining read pairing in output files.

### Adjust bias threshold
**Args:** `crossfilt -i input.fastq -r reference.fasta --threshold 0.1 -o filtered.fastq`
**Explanation:** Set custom threshold for alignment bias (default typically 0.05); higher values are more stringent.
