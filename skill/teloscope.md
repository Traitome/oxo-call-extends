---
name: teloscope
category: analysis
description: Teloscope - Reference-free telomere discovery tool for long-read sequencing data.
tags: [teloscope, telomere, long-read, telomere-discovery, nanopore, pacbio]
author: oxo-call-community
source_url: "https://github.com/skovaka/teloscope"
---

## Concepts

- **Tool Overview**: Teloscope - A reference-free tool for discovering telomere sequences directly from long-read sequencing data.
- **Core Function**: Identifies telomere repeat motifs de novo from long-read sequencing without requiring prior reference genome.
- **Input**: Long-read sequencing data (Nanopore or PacBio) in FASTQ format.
- **Output**: Discovered telomere repeat motifs, read-level telomere annotations, and telomere length estimates.
- **Installation**: `pip install teloscope` or `conda install -c bioconda teloscope`
- **Use Case**: Discovering novel telomere sequences in non-model organisms, validating telomere assemblies.

## Pitfalls

- **Long Reads Required**: Designed for long-read data - short reads may not span complete telomere regions.
- **Coverage**: Requires sufficient coverage for reliable de novo motif discovery.
- **Novel Telomeres**: May not detect telomeres in organisms with unusual telomere mechanisms.

## Examples

### Discover telomere motifs
**Args:** `teloscope -i long_reads.fastq.gz -o telomere_discovery/`
**Explanation:** Discover telomere repeat motifs de novo from Nanopore or PacBio reads.

### With minimum read length
**Args:** `teloscope -i reads.fastq -o output/ --min-len 1000`
**Explanation:** Only use reads longer than 1000bp for telomere discovery.
