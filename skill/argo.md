---
name: argo
category: metagenomics
description: Argo - Species-resolved profiling of antibiotic resistance genes in complex metagenomes
tags: [argo, metagenomics, antibiotic-resistance, long-reads, metagenomics]
author: oxo-call-community
source_url: "https://github.com/xinehc/argo"
---

## Concepts

- **Tool Overview**: Argo is a tool for species-resolved profiling of antibiotic resistance genes (ARGs) in complex metagenomes using long-read overlapping. Version 0.2.1.
- **Core Function**: Combines ARG detection with species-level resolution using long-read sequencing data for improved profiling in complex microbial communities.
- **Long-Read Analysis**: Utilizes Oxford Nanopore or PacBio long reads for ARG detection, enabling spanning of repetitive regions and mobile genetic elements.
- **Species Assignment**: Provides species-level attribution for detected ARGs, distinguishing between chromosomal and plasmid-borne resistance genes.
- **Mobile Genetic Elements**: Identifies ARGs located on plasmids, transposons, and integrons for horizontal gene transfer analysis.
- **Input/Output**: Accepts FASTQ/FASTA long-read files and outputs ARG abundance profiles with species annotations.
- **Installation**: `conda install -c bioconda argo` or install from GitHub.

## Pitfalls

- **Long-Read Quality**: Low-quality reads reduce ARG detection accuracy. Quality control and filtering recommended.
- **Reference Database**: ARG detection depends on comprehensive resistance gene databases. Database updates improve detection.
- **Species Assignment Ambiguity**: Short contigs may have ambiguous species assignment. Consider coverage and marker gene information.
- **Computational Resources**: Long-read alignment requires significant memory and CPU time for large datasets.
- **Complex Communities**: Highly diverse metagenomes may have many undiscovered species affecting profiling.

## Examples

### Basic ARG profiling
**Args:** `argo profile --reads input.fastq --output arg_profile.tsv`
**Explanation:** Performs ARG profiling on long-read input and outputs abundance table with species information.

### Specify reference database
**Args:** `argo profile --reads reads.fastq --db card_database --output results.tsv`
**Explanation:** Uses custom CARD database for ARG detection instead of default database.

### Minimum read length filter
**Args:** `argo profile --reads reads.fastq --min_length 1000 --output filtered_results.tsv`
**Explanation:** Filters reads to minimum 1000bp before ARG profiling for improved accuracy.

### Species-resolved output
**Args:** `argo profile --reads input.fastq --species_resolved --output species_args.tsv`
**Explanation:** Outputs ARG abundance broken down by species, showing which species carry each resistance gene.

### Batch processing
**Args:** `argo batch --input_dir fastq_files/ --output_dir results/`
**Explanation:** Processes multiple FASTQ files in batch mode for high-throughput analysis.

### Generate visualization
**Args:** `argo visualize --input profile.tsv --output heatmap.pdf --format pdf`
**Explanation:** Creates visualization of ARG profiles across samples in PDF format.