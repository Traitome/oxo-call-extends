---
name: kmcp
category: metagenomics
description: Accurate metagenomic profiling of both prokaryotic and viral populations by pseudo-mapping
tags: [kmcp, metagenomics, profiling, prokaryotes, viruses, pseudo-mapping]
author: oxo-call-community
source_url: "https://github.com/shenwei356/kmcp"
---

## Concepts

- **Metagenomic Profiling**: Profiles both prokaryotic and viral populations from metagenomic samples
- **Pseudo-mapping**: Uses k-mer based pseudo-alignment for rapid profiling
- **Database Indexing**: Builds efficient index from reference genomes
- **Abundance Estimation**: Estimates relative abundance of organisms
- **Cross-species Mapping**: Handles reads that map to multiple genomes
- **Batch Processing**: Supports processing multiple samples efficiently

## Pitfalls

- **Database Size**: Large databases increase memory and indexing time
- **Read Length**: Different k-mer sizes work better with different read lengths
- **Database Quality**: Incomplete databases miss organisms
- **Cross-mapping**: Reads mapping to multiple species cause ambiguity
- **Parameter Selection**: Threshold settings affect sensitivity
- **Computational Resources**: Large datasets require significant memory

## Examples

### Index genomes for profiling
**Args:** `kmcp index -I genomes.fasta -O index_dir`
**Explanation:** Indexes genome sequences for KMCP search.

### Search metagenomic reads
**Args:** `kmcp search -d index_dir -1 reads_R1.fq.gz -2 reads_R2.fq.gz -o results.tsv`
**Explanation:** Searches paired-end reads against indexed genomes.

### Single-end reads
**Args:** `kmcp search -d index_dir -r reads.fastq.gz -o results.tsv`
**Explanation:** Searches single-end reads against indexed genomes.

### Estimate abundance
**Args:** `kmcp profile -d index_dir -s results.tsv -o abundance.tsv`
**Explanation:** Estimates organism abundance from search results.

### Filter low-quality matches
**Args:** `kmcp search -d index_dir -1 reads_R1.fq.gz -2 reads_R2.fq.gz -o results.tsv --min-cov 0.5`
**Explanation:** Filters matches with coverage below 50%.

### Batch processing
**Args:** `kmcp batch -d samples/ -D index_dir -o results/`
**Explanation:** Processes multiple samples in batch mode.