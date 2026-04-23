---
name: autometa
category: metagenomics
description: Autometa - Automated extraction of microbial genomes from shotgun metagenomes
tags: [metagenomics, binning, genome-recovery, taxonomic-classification]
author: oxo-call-community
source_url: "https://github.com/KwanLab/Autometa"
---

## Concepts

- **Tool Overview**: Autometa is an automated binning pipeline for extracting microbial genomes from shotgun metagenomes, particularly effective for host-associated and highly complex communities.

- **Taxonomic Partitioning**: Performs kingdom-level taxonomic partitioning before binning, separating sequences into bacterial, archaeal, eukaryotic, and viral groups.

- **Coverage-Based Binning**: Uses differential coverage and tetranucleotide frequency for unsupervised clustering and binning.

- **Recursive Binning**: Applies recursive binning to improve genome recovery from complex samples.

- **Quality Assessment**: Evaluates bin completeness and contamination using CheckM-like metrics.

## Pitfalls

- **Coverage Requirements**: Requires multiple samples for differential coverage-based binning. Single-sample mode has reduced effectiveness.

- **Complex Communities**: Very diverse communities may produce fragmented bins. Adjust parameters for complex samples.

- **Memory Usage**: Large metagenomes require significant memory for coverage calculation and clustering.

- **Taxonomic Assignment**: Relies on DIAMOND/Blast hits for taxonomic assignment. Novel organisms may be misclassified.

## Examples

### Basic binning pipeline
**Args:** `autometa --assembly contigs.fasta --out-dir results/ --cpus 16`
**Explanation:** Runs complete Autometa binning pipeline on metagenome assembly.

### Single-sample binning
**Args:** `autometa --assembly contigs.fasta --bam-file alignments.bam --out-dir results/`
**Explanation:** Performs binning using single sample coverage from BAM file.

### Multi-sample binning
**Args:** `autometa --assembly contigs.fasta --bam-list bam_files.txt --out-dir results/`
**Explanation:** Uses differential coverage from multiple BAM files for improved binning.

### Custom clustering parameters
**Args:** `autometa --assembly contigs.fasta --bam-list bam_files.txt --clustering-method hdbscan --out-dir results/`
**Explanation:** Uses HDBSCAN clustering algorithm instead of default for potentially better bin boundaries.

### Extract specific kingdom
**Args:** `autometa --assembly contigs.fasta --bam-list bam_files.txt --kingdom bacteria --out-dir bacteria_bins/`
**Explanation:** Extracts only bacterial sequences and bins, skipping other kingdoms.

### Adjust completeness threshold
**Args:** `autometa --assembly contigs.fasta --bam-list bam_files.txt --completeness 50 --contamination 10 --out-dir results/`
**Explanation:** Sets minimum bin completeness to 50% and maximum contamination to 10%.
