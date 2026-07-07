---
name: cliquesnv
category: population-genomics
description: Scalable Reconstruction of Intra-Host Viral Populations from NGS Reads
tags: [cliquesnv, viral-populations, ngs, population-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vtsyvina/CliqueSNV"
---

## Concepts

- **Tool Overview**: CliqueSNV is a scalable tool for reconstructing intra-host viral populations from next-generation sequencing reads.
- **Core Function**: Identifies and reconstructs viral haplotypes present within a host from deep sequencing data.
- **Algorithm**: Uses graph-based approach to cluster reads into cliques representing distinct viral variants.
- **Input**: Deep sequencing reads (FASTQ) or aligned reads (BAM) from viral samples.
- **Output**: Reconstructed viral haplotypes with frequencies and consensus sequences.
- **Application**: Viral evolution studies, quasispecies analysis, and drug resistance monitoring.
- **Installation**: Install via bioconda: `conda install -c bioconda cliquesnv`

## Pitfalls

- **Deep Sequencing**: Requires high-depth sequencing for accurate haplotype reconstruction.
- **Viral Specific**: Designed specifically for viral populations.
- **Computational Resources**: May require significant resources for large datasets.
- **Memory Usage**: May require significant memory for complex populations.
- **Parameter Tuning**: May require adjustment of clustering parameters.

## Examples

### Reconstruct viral populations
**Args:** `cliquesnv -i reads.fastq -r reference.fasta -o haplotypes.fasta`
**Explanation:** Reconstructs viral haplotypes from sequencing reads.

### From aligned reads
**Args:** `cliquesnv -b alignments.bam -o haplotypes.fasta`
**Explanation:** Processes aligned BAM file to identify viral variants.

### With frequency threshold
**Args:** `cliquesnv -i reads.fastq -r reference.fasta -f 0.01 -o haplotypes.fasta`
**Explanation:** Filters haplotypes with frequency >= 1%.

### Display help
**Args:** `cliquesnv --help`
**Explanation:** Shows all available options and usage information.