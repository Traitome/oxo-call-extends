---
name: coverm
category: metagenomics
description: Configurable DNA read coverage and relative abundance calculator for metagenomics
tags: [coverm, metagenomics, coverage, abundance, relative-abundance, sequencing]
author: oxo-call-community
source_url: "https://github.com/wwood/CoverM"
---

## Concepts

- **Tool Overview**: CoverM is a fast and configurable tool for calculating DNA read coverage and relative abundance, primarily designed for metagenomics applications.
- **Core Function**: Computes coverage of reads against reference genomes or contigs, and estimates relative abundance of organisms in metagenomic samples.
- **Algorithm**: Uses read mapping and statistical methods to calculate coverage metrics and relative abundance.
- **Input**: BAM/CRAM files or raw FASTQ reads, reference FASTA files.
- **Output**: Coverage table (TSV) with per-genome or per-contig coverage statistics.
- **Application**: Metagenomics analysis, microbial community profiling, genome coverage assessment.
- **Installation**: Install via bioconda: `conda install -c bioconda coverm`

## Pitfalls

- **BAM Sorting**: Input BAM files must be sorted by coordinate for some operations.
- **Minimap2 Required**: For mapping mode, minimap2 must be available in PATH.
- **Genome Naming**: Genome names are derived from FASTA headers; ensure consistent naming.
- **Coverage Calculation**: Different methods (mean vs median) can give different results.
- **Relative Abundance**: Relative abundance sums to 1.0; unmapped reads are excluded.

## Examples

### Calculate genome coverage from BAM
**Args:** `coverm genome --bam-files sample.bam --reference-genomes genomes/ -o coverage.tsv`
**Explanation:** Calculates coverage against reference genomes from pre-aligned BAM.

### Calculate coverage with direct mapping
**Args:** `coverm genome --coupled reads_R1.fq,reads_R2.fq --reference-genomes genomes/ -o coverage.tsv -t 8`
**Explanation:** Maps reads to references using minimap2 with 8 threads.

### Calculate contig coverage
**Args:** `coverm contig --bam-files sample.bam -o contig_coverage.tsv`
**Explanation:** Calculates per-contig coverage from BAM aligned to assembled contigs.

### Calculate relative abundance (TPM)
**Args:** `coverm genome --coupled reads_R1.fq,reads_R2.fq --reference-genomes genomes/ --relative-abundance -o abundance.tsv`
**Explanation:** Estimates relative abundance using TPM normalization.

### Use trimmed mean coverage
**Args:** `coverm genome --bam-files sample.bam --reference-genomes genomes/ --trim-max 95 --trim-min 5 -o coverage.tsv`
**Explanation:** Uses trimmed mean for more robust estimates.

### Filter low-coverage genomes
**Args:** `coverm genome --bam-files sample.bam --reference-genomes genomes/ --min-covered-fraction 0.1 --min-mean-coverage 5 -o coverage.tsv`
**Explanation:** Reports genomes with at least 10% covered and mean coverage >= 5x.