---
name: tcdemux
category: utility
description: tcdemux - Demultiplexes target capture sequencing files and prepares reads for analysis pipelines.
tags: [tcdemux, demultiplexing, target-capture, sequencing, preprocessing]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/tcdemux"
---

## Concepts

- **Tool Overview**: tcdemux (v0.1.1) - A demultiplexing tool for target capture sequencing data, part of a target capture analysis pipeline.
- **Core Function**: Separates multiplexed sequencing reads by sample/barcode and prepares them for downstream target capture analysis.
- **Input**: Multiplexed FASTQ files with associated sample sheets or barcode information.
- **Output**: Demultiplexed FASTQ files organized by sample, ready for target capture analysis.
- **Installation**: `conda install -c bioconda tcdemux`
- **Dependencies**: Requires bbmap, cutadapt, pandas, snakemake for pipeline execution.

## Pitfalls

- **Barcode Handling**: Requires accurate barcode/sample sheet information - errors lead to misassignment.
- **Paired-end Data**: Processes paired-end sequencing - ensure both reads are present.
- **Pipeline Dependency**: Part of a larger Snakemake workflow - may require other pipeline components.

## Examples

### Demultiplex paired-end reads
**Args:** `tcdemux -i sample_sheet.csv -o demux_output/ reads_R1.fastq.gz reads_R2.fastq.gz`
**Explanation:** Basic demultiplexing of paired-end reads using sample sheet CSV.

### With cutadapt trimming
**Args:** `tcdemux -i sample_sheet.csv -o output/ --trim-adapters R1.fastq.gz R2.fastq.gz`
**Explanation:** Demultiplex and trim adapters in one step.
