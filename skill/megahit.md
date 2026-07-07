---
name: megahit
category: assembly
description: Ultra-fast metagenomics assembler using succinct de Bruijn graph.
tags: [megahit, metagenomics, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/voutcn/megahit"
---

## Concepts

- **Tool Overview**: MEGAHIT assembles metagenomic sequences efficiently.
- **Core Function**: Builds succinct de Bruijn graphs for assembly.
- **Succinct Data Structure**: Uses compact representation for efficiency.
- **Multi-k-mer**: Supports multiple k-mer sizes for better assembly.
- **Parallel Processing**: Optimized for multi-core systems.
- **Installation**: `conda install -c bioconda megahit`

## Pitfalls

- **Memory Requirements**: High memory for large datasets.
- **k-mer Selection**: k-mer choice affects assembly quality.
- **Computation Time**: Can be slow for complex metagenomes.
- **Contig Quality**: May produce fragmented assemblies.
- **Parameter Tuning**: Requires careful optimization.
- **Input Quality**: Low-quality reads affect assembly.

## Examples

### Assemble paired-end reads
**Args:** `megahit -1 R1.fq.gz -2 R2.fq.gz -o output_dir`
**Explanation:** Assembles metagenomic paired-end reads.

### Single-end reads
**Args:** `megahit -r reads.fq.gz -o output_dir`
**Explanation:** Assembles single-end sequencing reads.

### Multiple k-mer sizes
**Args:** `megahit -1 R1.fq.gz -2 R2.fq.gz --k-list 21,33,55 -o output_dir`
**Explanation:** Uses multiple k-mer sizes.

### Threaded assembly
**Args:** `megahit -1 R1.fq.gz -2 R2.fq.gz -t 16 -o output_dir`
**Explanation:** Uses 16 threads for parallel processing.

### Help documentation
**Args:** `megahit --help`
**Explanation:** Displays available options.
