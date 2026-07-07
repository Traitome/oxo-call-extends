---
name: hla-la
category: immunology
description: HLA typing from short and long reads using population reference graphs.
tags: [hla-la, HLA, typing, NGS, short reads, long reads]
author: oxo-call-community
source_url: "https://github.com/DiltheyLab/HLA-LA"
---

## Concepts

- **Population Reference Graph (PRG)**: HLA-LA uses a population reference graph approach to accurately type HLA alleles from sequencing data.
- **Multi-read Support**: Supports both short-read (Illumina) and long-read (PacBio/ONT) sequencing data.
- **High Resolution Typing**: Capable of high-resolution HLA typing (4-digit and beyond).
- **Graph Preparation**: Requires preprocessing step to prepare the PRG graph from reference sequences.
- **Memory Intensive**: The graph preparation and typing processes can require significant memory resources (30GB+ RAM).

## Pitfalls

- **Memory Requirements**: Running HLA-LA can require 300-400 GB RAM for large datasets; ensure sufficient resources are available.
- **Database Preparation**: The PRG graph database must be downloaded and indexed before use, requiring ~30GB memory for indexing.
- **BAM File Requirements**: Requires genome-aligned BAM files (e.g., aligned to GRCh38), not HLA-reference-aligned BAMs.
- **Long Processing Time**: Typing large datasets can be time-consuming, even with multiple threads.
- **Swap Memory Usage**: On systems with limited RAM, excessive swap usage can significantly slow down analysis.

## Examples

### Prepare PRG graph database
**Args:** `HLA-LA --action prepareGraph --PRG_graph_dir /path/to/graphs/PRG_MHC_GRCh38_withIMGT`
**Explanation:** Prepares the population reference graph database for HLA typing.

### Run HLA typing on BAM file
**Args:** `HLA-LA.pl --BAM ./sample.bam --graph PRG_MHC_GRCh38_withIMGT --sampleID patient1 --maxThreads 8 --workingDir ./output`
**Explanation:** Performs HLA typing on a BAM file using 8 threads and saves results to the output directory.

### Download and setup database
**Args:** `cd ~/miniconda3/opt/hla-la/ && mkdir -p graphs && wget http://www.well.ox.ac.uk/downloads/PRG_MHC_GRCh38_withIMGT.tar.gz && tar -xvzf PRG_MHC_GRCh38_withIMGT.tar.gz`
**Explanation:** Downloads and extracts the PRG MHC reference database.

### HLA typing with long reads
**Args:** `HLA-LA.pl --BAM ./long_reads.bam --graph PRG_MHC_GRCh38_withIMGT --sampleID patient2 --maxThreads 16 --workingDir ./lr_output`
**Explanation:** Performs HLA typing using long-read sequencing data with increased thread count.

### Run in batch mode
**Args:** `for bam in *.bam; do HLA-LA.pl --BAM $bam --graph PRG_MHC_GRCh38_withIMGT --sampleID ${bam%.bam} --maxThreads 4 --workingDir ./batch_output/${bam%.bam}; done`
**Explanation:** Processes multiple BAM files in batch mode, creating separate output directories for each sample.