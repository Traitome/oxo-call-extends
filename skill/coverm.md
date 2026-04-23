---
name: coverm
category: metagenomics
description: Configurable, easy to use DNA read coverage and relative abundance calculator for metagenomics
tags: [coverm, metagenomics, coverage, abundance, relative-abundance]
author: oxo-call-community
source_url: "https://github.com/wwood/CoverM"
---

## Concepts

- **Tool Overview**: CoverM is a fast and configurable tool for calculating DNA read coverage and relative abundance, primarily designed for metagenomics applications.
- **Core Function**: Computes coverage of reads against reference genomes or contigs, and estimates relative abundance of organisms in metagenomic samples.
- **Input/Output**: Input: BAM/CRAM files or raw FASTQ reads with reference FASTA. Output: Coverage table (TSV) with per-genome or per-contig coverage.
- **Two Modes**: `genome` mode for coverage against reference genomes, `contig` mode for coverage of assembled contigs.
- **Coverage Methods**: Supports multiple coverage calculation methods: mean, median, trimmed mean, and relative abundance (RPKM/TPM).
- **Efficiency**: Handles large metagenomic datasets efficiently with multi-threading support.

## Pitfalls

- **BAM Sorting**: Input BAM files must be sorted by coordinate for some operations. Use `--bam-sort` if needed.
- **Minimap2 Required**: For mapping mode, minimap2 must be available in PATH.
- **Genome Naming**: Genome names are derived from FASTA headers. Ensure consistent naming across references.
- **Coverage Calculation**: Different methods (mean vs median) can give very different results. Choose based on your analysis needs.
- **Relative Abundance**: Relative abundance sums to 1.0 across all genomes. Unmapped reads are excluded.

## Examples

### Calculate genome coverage from BAM
**Args:** `genome --bam-files sample.bam --reference-genomes genomes/ -o coverage.tsv`
**Explanation:** Calculates coverage of reads against reference genomes from a pre-aligned BAM file.

### Calculate coverage with direct mapping
**Args:** `genome --coupled reads_R1.fq,reads_R2.fq --reference-genomes genomes/ -o coverage.tsv -t 8`
**Explanation:** Maps reads to reference genomes using minimap2 and calculates coverage, using 8 threads.

### Calculate contig coverage
**Args:** `contig --bam-files sample.bam -o contig_coverage.tsv`
**Explanation:** Calculates per-contig coverage from a BAM file aligned to assembled contigs.

### Calculate relative abundance (TPM)
**Args:** `genome --coupled reads_R1.fq,reads_R2.fq --reference-genomes genomes/ --relative-abundance -o abundance.tsv`
**Explanation:** Estimates relative abundance using TPM normalization, useful for comparing species proportions.

### Use trimmed mean coverage
**Args:** `genome --bam-files sample.bam --reference-genomes genomes/ --trim-max 95 --trim-min 5 -o coverage.tsv`
**Explanation:** Uses trimmed mean (removing top 5% and bottom 5% of coverage values) for more robust estimates.

### Calculate median coverage
**Args:** `genome --bam-files sample.bam --reference-genomes genomes/ --min-covered-fraction 0.5 -o coverage.tsv`
**Explanation:** Reports median coverage and requires at least 50% of genome to be covered for inclusion.

### Process multiple samples
**Args:** `genome --bam-files sample1.bam,sample2.bam,sample3.bam --reference-genomes genomes/ -o all_coverage.tsv`
**Explanation:** Calculates coverage for multiple samples against the same reference, outputs combined table.

### Filter low-coverage genomes
**Args:** `genome --bam-files sample.bam --reference-genomes genomes/ --min-covered-fraction 0.1 --min-mean-coverage 5 -o coverage.tsv`
**Explanation:** Only reports genomes with at least 10% covered and mean coverage >= 5x.
