---
name: emirge
category: utility
description: "EMIRGE reconstructs full length sequences from short sequencing reads"
tags: [emirge, utility, sequence-reconstruction, short-reads, metagenomics]
author: oxo-call-community
source_url: "https://github.com/csmiller/EMIRGE"
---

## Concepts

- **Tool Overview**: EMIRGE (Expectation-Maximization Iterative Reconstruction of Genes from the Environment) is a tool for reconstructing full-length 16S rRNA genes from short sequencing reads in metagenomic datasets.
- **Core Function**: Uses an expectation-maximization algorithm to iteratively reconstruct full-length sequences from fragmented short reads, primarily for ribosomal RNA analysis.
- **Input/Output**: Input: Short reads (FASTQ), reference database. Output: Reconstructed full-length sequences (FASTA), abundance estimates.
- **Algorithm**: Iteratively maps reads to reference sequences, performs multiple sequence alignment, and reconstructs consensus sequences using EM algorithm.
- **Key Features**: Full-length sequence reconstruction, abundance estimation, reference-based assembly, metagenomic analysis, taxonomic classification.
- **Installation**: `conda install -c bioconda emirge`

## Pitfalls

- **Reference Database**: Requires appropriate reference database for reconstruction.
- **Read Length**: Performance depends on read length and quality.
- **Computation Time**: May be slow for large datasets.
- **Memory Usage**: Requires significant memory for large reference databases.
- **Taxonomic Bias**: Reference database may introduce taxonomic bias.

## Examples

### Basic sequence reconstruction
**Args:** `emirge.py -1 reads_1.fastq -2 reads_2.fastq -o output/`
**Explanation:** Reconstructs full-length sequences from paired-end reads.

### With custom reference database
**Args:** `emirge.py -1 reads_1.fastq -2 reads_2.fastq -r ref_db.fasta -o output/`
**Explanation:** Uses custom reference database for reconstruction.

### Specify number of iterations
**Args:** `emirge.py -1 reads_1.fastq -2 reads_2.fastq -i 20 -o output/`
**Explanation:** Runs 20 iterations of EM algorithm.

### Output abundance estimates
**Args:** `emirge.py -1 reads_1.fastq -2 reads_2.fastq -a -o output/`
**Explanation:** Outputs abundance estimates for reconstructed sequences.

### Filter low-quality sequences
**Args:** `emirge.py -1 reads_1.fastq -2 reads_2.fastq -q 20 -o output/`
**Explanation:** Filters sequences with quality score below 20.