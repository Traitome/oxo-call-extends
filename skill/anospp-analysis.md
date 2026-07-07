---
name: anospp-analysis
category: utility
description: Python package for ANOSPP data analysis - multiplexed amplicon sequencing assay for Anopheles mosquito species identification and Plasmodium detection
tags: [anospp-analysis, mosquito, malaria, Plasmodium, amplicon-sequencing, species-identification]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/anospp-analysis"
---

## Concepts

- **Tool Overview**: anospp-analysis (v0.4.0) - Python package for analyzing ANOSPP sequencing data, designed for Anopheles mosquito species identification and Plasmodium detection.
- **Core Function**: A suite of analysis tools for processing multiplexed amplicon sequencing data from the ANOSPP assay, including demultiplexing, QC, species identification, and result aggregation.
- **Key Components**:
  - `anospp-prep`: Demultiplexes amplicons from DADA2 output and generates haplotypes table
  - `anospp-qc`: Produces QC plots from haplotypes table and DADA2 stats
  - `anospp-plasm`: BLASTs Plasmodium sequences against reference dataset for species determination and infection status inference
  - `anospp-nn`: Compares k-mer profiles against reference for probabilistic mosquito species calls
  - `anospp-vae`: Provides fine-scale species prediction for An. gambiae complex using VAE projection
  - `anospp-agg`: Combines all results into a single consolidated table
- **Input/Output**: Works with DADA2 output files (sequences, stats), primer sequences, samples manifest; outputs haplotypes tables, QC plots, species calls, aggregated results
- **Installation**: `conda install -c bioconda anospp-analysis`

## Pitfalls

- **DADA2 Dependence**: Requires pre-processed DADA2 output files as input
- **Reference Databases**: Needs appropriate reference datasets for mosquito and Plasmodium species identification
- **Version Differences**: Options may vary between versions
- **TensorFlow/Keras Requirements**: Requires specific versions of TensorFlow (2.15.0) and Keras (2.15.0)

## Examples

### Prepare haplotypes table
**Args:** `anospp-prep --dada2-seqs dada2/seqtab.fasta --dada2-stats dada2/stats.tsv --primers primers.fasta --output haplotypes.tsv`
**Explanation:** Takes DADA2 output and primer sequences, demultiplexes amplicons, and generates haplotypes table.

### Generate QC plots
**Args:** `anospp-qc --haplotypes haplotypes.tsv --stats dada2/stats.tsv --manifest samples.tsv --output qc_plots/`
**Explanation:** Produces quality control plots for the sequencing data and haplotypes.

### Plasmodium species detection
**Args:** `anospp-plasm --haplotypes haplotypes.tsv --ref-db plasmodium_ref.fasta --output plasmodium_results.tsv`
**Explanation:** BLASTs Plasmodium sequences against reference to determine species and infer infection status.

### Mosquito species identification with neural network
**Args:** `anospp-nn --haplotypes haplotypes.tsv --ref-db mosquito_ref.fasta --output species_calls.tsv`
**Explanation:** Uses k-mer profiles and neural network for probabilistic mosquito species identification.

### Aggregate all results
**Args:** `anospp-agg --haplotypes haplotypes.tsv --plasm plasmodium_results.tsv --nn species_calls.tsv --output final_results.tsv`
**Explanation:** Combines results from all analysis steps into a single consolidated table.