---
name: tgsgapcloser
category: assembly
description: TGS-GapCloser - Gap closing tool for third-generation sequencing (long-read) assemblies.
tags: [tgsgapcloser, gap-closer, long-read, assembly, nanopore, pacbio, polish]
author: oxo-call-community
source_url: "https://github.com/BGI-QingTao/TGSGapCloser"
---

## Concepts

- **Tool Overview**: TGS-GapCloser - A gap closing tool specifically designed for assemblies generated from third-generation sequencing (long-read) technologies.
- **Core Function**: Uses long reads to close gaps in genome assemblies, improving assembly completeness and continuity.
- **Input**: Draft genome assembly (FASTA), long-read data (FASTQ), reference genome (optional).
- **Output**: Improved genome assembly with closed gaps, gap closure report.
- **Installation**: `pip install tgsgapcloser` or `conda install -c bioconda tgsgapcloser`
- **Use Case**: Improving long-read assemblies, completing draft genomes, genome finishing.

## Pitfalls

- **Read Depth**: Requires sufficient long-read coverage for effective gap closing.
- **Assembly Quality**: Works best with assemblies that have good overall contiguity but contain gaps.

## Examples

### Close gaps in assembly
**Args:** `TGSGapCloser -i draft_assembly.fasta -o improved_assembly.fasta -l longreads.fastq.gz`
**Explanation:** Use long reads to close gaps in the draft assembly.

### With reference
**Args:** `TGSGapCloser -i contigs.fasta -o closed.fasta -l nanopore.fastq.gz -r reference.fasta`
**Explanation:** Use both long reads and reference for improved gap closure.
