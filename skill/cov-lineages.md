---
name: cov-lineages
category: variant-calling
description: Phylogenetic Assignment of Named Global Outbreak LINeages - SARS-CoV-2 lineage classification tool
tags: [cov-lineages, pangolin, sars-cov-2, lineage-classification, covid-19, variant-analysis, genomic-epidemiology]
author: oxo-call-community
source_url: "https://github.com/cov-lineages/pangolin"
---

## Concepts

- **Tool Overview**: Pangolin (Phylogenetic Assignment of Named Global Outbreak LINeages) is the standard tool for assigning SARS-CoV-2 sequences to Pango lineages, enabling genomic epidemiology and variant tracking.
- **Core Function**: Classifies SARS-CoV-2 sequences into Pango lineages based on mutations and phylogenetic placement.
- **Algorithm**: Uses UShER (ultra-fast phylogenetic placement) or pangoLEARN (machine learning) for lineage inference, with Scorpio for VOC-related lineage curation.
- **Input**: FASTA file containing SARS-CoV-2 consensus sequences.
- **Output**: CSV file with lineage assignments (lineage_report.csv), optionally with alignment output.
- **Application**: COVID-19 genomic surveillance, variant of concern (VOC) tracking, outbreak investigation, phylogenetic analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda pangolin`

## Pitfalls

- **Sequence Quality**: Sequences with high N content or low quality may fail assignment. Default max-ambig is 0.3 (30% Ns allowed).
- **Sequence Length**: Minimum recommended length is 25,000 bp. Shorter sequences may fail.
- **Analysis Mode**: UShER mode (accurate) is default but slower. For large datasets, use `--analysis-mode fast` with pangoLEARN.
- **Data Updates**: Lineage definitions change frequently. Run `pangolin --update-data` regularly to stay current.
- **Divergent Sequences**: Sequences too diverged from known SARS-CoV-2 may not be assignable.

## Examples

### Basic lineage assignment
**Args:** `pangolin sequences.fasta`
**Explanation:** Assigns SARS-CoV-2 sequences to Pango lineages using default UShER mode.

### Fast mode for large datasets
**Args:** `pangolin --analysis-mode fast sequences.fasta`
**Explanation:** Uses pangoLEARN machine learning model for faster processing of large batches.

### Custom output directory and filename
**Args:** `pangolin --outdir results/ --outfile lineage_report.csv sequences.fasta`
**Explanation:** Specifies custom output directory and filename for the lineage assignment results.

### Output multiple sequence alignment
**Args:** `pangolin --alignment --alignment-file aligned_sequences.fasta sequences.fasta`
**Explanation:** Generates a multiple sequence alignment (MSA) of input sequences with reference, useful for downstream phylogenetic analysis.

### Update lineage data
**Args:** `pangolin --update-data`
**Explanation:** Downloads the latest lineage definitions, UShER tree, and pangoLEARN model files.

### Set thread count for parallel processing
**Args:** `pangolin -t 8 sequences.fasta`
**Explanation:** Uses 8 threads for faster processing, especially useful for UShER mode.

### Custom data directory
**Args:** `pangolin --datadir /path/to/pangolin-data sequences.fasta`
**Explanation:** Uses a custom pangolin-data directory instead of the installed default.
