---
name: fjord
category: hpc
description: "FJORD is an amplicon sequencing pipeline for bacterial identification from Oxford Nanopore Technologies long-read data, mapping reads to GTDB reference databases."
tags: [fjord, hpc, nanopore, amplicon, sequencing, bacterial-identification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/adnsvrtsn/fjord"
---

## Concepts
- **Tool Overview**: FJORD (Flexible Joint Operational pipeline for Reference-based Diagnostics) is an amplicon sequencing pipeline for bacterial identification from Oxford Nanopore Technologies long-read data. It maps reads to a GTDB-formatted reference database, generates consensus sequences, clusters similar sequences with IUPAC-aware consolidation, and assigns taxonomy via BLAST.
- **Core Function**: Rapid bacterial identification from ONT amplicon sequencing data using reference-based mapping and consensus calling.
- **Input/Output**: Input: FASTQ files from ONT sequencing, GTDB reference database. Output: Consensus sequences, taxonomic assignments, visualization reports.
- **GTDB Integration**: Uses Genome Taxonomy Database (GTDB) formatted references for accurate taxonomic classification down to species level.
- **Consensus Calling**: Implements IUPAC-aware sequence consolidation to handle ambiguous base calls in heterogeneous populations.
- **Taxonomic Assignment**: Uses BLAST for initial taxonomic classification with configurable e-value and identity thresholds.
- **Installation**: `conda install -c bioconda fjord` or clone from GitHub and install dependencies.

## Pitfalls
- **Reference Database Requirements**: Must use GTDB-formatted database. Standard NCBI databases require conversion before use.
- **Long Read Quality**: Poor quality ONT reads may produce incorrect consensus sequences. Quality filtering recommended prior to analysis.
- **Barcode Demultiplexing**: If using barcoded libraries, ensure proper demultiplexing before running FJORD.
- **Memory Usage**: Large reference databases require significant memory. Consider splitting analysis by taxonomic groups for large datasets.
- **IUPAC Ambiguity Handling**: Mixed populations may produce ambiguous consensus calls that affect downstream taxonomic assignment.
- **BLAST Threshold Tuning**: Default parameters may not be optimal for all datasets. Adjust e-value and identity thresholds based on data quality.

## Examples
### Basic FJORD run with ONT reads
**Args:** `fjord --reads sample.fastq --db gtdb_r207/ --outdir results/`
**Explanation:** Runs FJORD on ONT amplicon reads against GTDB reference database, generating consensus sequences and taxonomic assignments.

### Run with quality filtering
**Args:** `fjord --reads sample.fastq --db gtdb_r207/ --outdir results/ --min-qscore 9`
**Explanation:** Filters reads by minimum quality score (Q9) before processing to improve consensus accuracy.

### Generate visualization report
**Args:** `fjord --reads sample.fastq --db gtdb_r207/ --outdir results/ --visualize`
**Explanation:** Generates interactive HTML visualization report showing taxonomic assignments and read mapping statistics.

### Cluster sequences with IUPAC consolidation
**Args:** `fjord --reads sample.fastq --db gtdb_r207/ --outdir results/ --cluster-iupac`
**Explanation:** Enables IUPAC-aware sequence clustering to handle mixed base calls in heterogeneous samples.

### Custom BLAST parameters
**Args:** `fjord --reads sample.fastq --db gtdb_r207/ --outdir results/ --blast-evalue 1e-50 --blast-identity 95`
**Explanation:** Sets custom BLAST e-value and identity thresholds for stricter taxonomic assignment.
