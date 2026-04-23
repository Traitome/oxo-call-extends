---
name: nanopolish
category: variant-calling
description: Signal-level algorithms for MinION data.
tags: [nanopolish, variant-calling, nanopore, signal-level, methylation]
author: oxo-call-community
source_url: "https://github.com/jts/nanopolish"
---

## Concepts

- **Tool Overview**: Nanopolish v0.14.0 - signal-level algorithms for Nanopore data.
- **Core Function**: Performs variant calling, methylation detection, and event alignment using raw Nanopore signal data.
- **Input/Output**: Takes FAST5 + FASTQ/BAM; outputs variant calls, methylation calls, or eventalign data.
- **Installation**: `conda install -c bioconda nanopolish`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires both FAST5 signal files and basecalled FASTQ/BAM.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Index reads
**Args:** `index -d fast5_dir reads.fastq.gz`
**Explanation:** Indexes FAST5 files for subsequent Nanopolish commands.

### Call variants
**Args:** `callvariants -r reference.fasta -b aligned.bam -g variants.vcf -o calls.vcf`
**Explanation:** Calls variants from signal-level data.

### Methylation calling
**Args:** `call-methylation -r reference.fasta -b aligned.bam -o methylation.tsv`
**Explanation:** Detects methylated bases from signal data.
