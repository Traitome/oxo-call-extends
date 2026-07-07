---
name: cpgeneprofiler
category: annotation
description: R package for profiling carbapenemase (CP) genes from bacterial genome assemblies using BLAST
tags: [cpgeneprofiler, carbapenemase, antimicrobial-resistance, amr, bacteria, genome-assembly, blast, r-package]
author: oxo-call-community
source_url: "https://github.com/ramadatta/CPgeneProfiler"
---

## Concepts

- **Tool Overview**: CPgeneProfiler is an R package that profiles carbapenemase (CP) genes from bacterial genome assemblies. Uses NCBI BLAST+ and R framework to detect and visualize CP gene families.
- **Core Function**: Scans genome assemblies (FASTA) against a curated CP gene database and generates profile heatmaps showing presence/absence of carbapenemase genes.
- **Algorithm**: Performs BLASTN searches of genome contigs against known CP gene sequences, then visualizes results as heatmaps and analyzes gene cocarriage patterns.
- **Input**: FASTA files containing genome assemblies, CP gene database (FASTA format).
- **Output**: Profile heatmaps, gene presence/absence tables, assembly statistics (N50, N90, assembly size), CP gene contig length distributions.
- **Application**: Antimicrobial resistance surveillance, carbapenem-resistant Enterobacteriaceae (CRE) monitoring, hospital infection control, epidemiological studies.
- **Installation**: R package installation via devtools: `install.packages("devtools"); devtools::install_github("ramadatta/CPgeneProfiler")`

## Pitfalls

- **R Dependencies**: Requires multiple R packages: ggplot2, dplyr, tidyverse, UpSetR, scales, ape, reshape2, gridExtra, Biostrings.
- **BLAST+ Requirement**: Requires NCBI BLAST+ executables installed and accessible in PATH.
- **Database Download**: CP gene database must be downloaded separately before first use.
- **Database Families**: Current database includes: IMI, IMP, KPC, NDM, OXA, VIM gene families. Other CP genes may not be detected.
- **Assembly Quality**: Results depend on assembly quality; fragmented assemblies may miss CP genes.

## Examples

### Basic CP gene profiling
**Args:** `CPgeneProfiler("/path/to/fasta", "/path/to/db/")`
**Explanation:** Profiles carbapenemase genes from genome assemblies in the specified FASTA directory.

### With custom database path
**Args:** `CPgeneProfiler("/data/genomes", "/data/CPgeneDB/")`
**Explanation:** Specifies custom paths for genome assemblies and CP gene database.

### Install required R packages
**Args:** `install.packages(c("ggplot2","dplyr", "tidyverse", "UpSetR", "scales", "ape", "reshape2", "gridExtra"))`
**Explanation:** Installs all required R dependencies for CPgeneProfiler.

### Install Biostrings (Bioconductor)
**Args:** `if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager"); BiocManager::install("Biostrings")`
**Explanation:** Installs Bioconductor's Biostrings package for sequence handling.

### Download CP gene database
**Args:** `download.file("https://raw.githubusercontent.com/ramadatta/CPgene-profiler/master/ARG-annot_CPGene_DB.fasta", "CPgene_DB.fasta")`
**Explanation:** Downloads the curated carbapenemase gene database for use in profiling.
