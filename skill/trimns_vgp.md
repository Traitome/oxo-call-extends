---
name: trimns_vgp
category: utility
description: TrimNS VGP - Tool for trimming Nanopore sequencing reads for VGP project.
tags: [trimns_vgp, nanopore, read-trimming, vgp, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/VGP/vgp-assembly"
---

## Concepts

- **Tool Overview**: TrimNS VGP - A tool for trimming Nanopore sequencing reads for the Vertebrate Genomes Project.
- **Core Function**: Trims adapter sequences and low-quality regions from Nanopore reads.
- **Input**: FASTQ files from Nanopore sequencing.
- **Output**: Trimmed reads, trimming statistics.
- **Installation**: Part of VGP assembly pipeline
- **Use Case**: Nanopore data processing, genome assembly preparation.

## Pitfalls

- **Specificity**: Optimized for VGP project standards.
- **Adapter Sequences**: Requires specific adapter sequences.

## Examples

### Trim Nanopore reads
**Args:** `trimns_vgp -i nanopore.fastq -o trimmed.fastq`
**Explanation:** Trim Nanopore reads for VGP assembly.

### With quality control
**Args:** `trimns_vgp -i raw.fastq -q -o clean.fastq`
**Explanation:** Trim reads with quality control.
