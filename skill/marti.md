---
name: marti
category: alignment
description: Metagenomic Analysis in Real Time
tags: [marti, alignment, metagenomics, real-time]
author: oxo-call-community
source_url: "https://github.com/richardmleggett/MARTi"
---

## Concepts

- **Tool Overview**: marti v0.9.29 - MARTi performs real-time analysis of metagenomic samples using nanopore sequencing data.
- **Core Function**: Analyzes metagenomic data in real-time as sequencing progresses.
- **Input/Output**: Input: Nanopore reads (FASTQ); Output: Taxonomic profiles, real-time updates.
- **Installation**: `conda install -c bioconda marti`
- **Real-time Analysis**: Processes sequencing data as it is generated.
- **Nanopore Optimization**: Specifically optimized for nanopore sequencing data.

## Pitfalls

- **Read Quality**: Poor quality reads affect classification.
- **Real-time Constraints**: Requires fast processing for real-time analysis.
- **Memory Usage**: Large datasets require significant memory.
- **Reference Database**: Outdated databases affect accuracy.
- **Computational Resources**: Requires sufficient computational resources.
- **Network Latency**: Real-time mode may be affected by network latency.

## Examples

### Real-time analysis
**Args:** `marti realtime -i reads.fastq -d database/ -o results/`
**Explanation:** Performs real-time metagenomic analysis.

### Offline mode
**Args:** `marti offline -i reads.fastq -d database/ -o results/`
**Explanation:** Processes data in offline mode.

### Paired-end reads
**Args:** `marti offline -1 reads_1.fastq -2 reads_2.fastq -d database/ -o results/`
**Explanation:** Processes paired-end reads.

### Verbose mode
**Args:** `marti offline -i reads.fastq -d database/ -o results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Generate visualization
**Args:** `marti offline -i reads.fastq -d database/ -o results/ --plot`
**Explanation:** Generates visualization of results.

### Custom confidence threshold
**Args:** `marti offline -i reads.fastq -d database/ -o results/ -c 0.9`
**Explanation:** Sets confidence threshold to 0.9.