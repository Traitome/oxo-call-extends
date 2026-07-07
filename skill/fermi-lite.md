---
name: fermi-lite
category: assembly
description: "Fermi-lite is a standalone C library as well as a command-line tool for assembling Illumina short reads in regions from 100bp to 10 million bp in size."
tags: [fermi-lite, assembly, Illumina, de-bruijn-graph, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lh3/fermi-lite"
---

## Concepts

- **Tool Overview**: fermi-lite is a C library and command-line tool for assembling Illumina short reads in regions from 100bp to 10 million bp.
- **Core Function**: Assembles short reads into contigs using de Bruijn graph approach.
- **Input/Output**: Input: Illumina reads. Output: Assembled contigs, sequences.
- **Algorithm**: Uses de Bruijn graph assembly for short read assembly.
- **Key Features**: Fast assembly, de Bruijn graph, multi-size support, C library, memory efficient.
- **Installation**: `conda install -c bioconda fermi-lite`

## Pitfalls

- **Read Quality**: Requires high-quality Illumina reads.
- **Repeat Complexity**: Complex repeats may affect assembly.
- **Memory Usage**: Large assemblies may require significant memory.
- **Region Size**: Optimal for medium-sized regions.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic assembly
**Args:** `fermi-lite assemble -i reads.fastq -o contigs.fasta`
**Explanation:** Assembles reads into contigs.

### Specify region size
**Args:** `fermi-lite assemble -i reads.fastq -o contigs.fasta -s 1000000`
**Explanation:** Assembles with 1Mb region size.

### With mate pairs
**Args:** `fermi-lite assemble -i reads_1.fastq -2 reads_2.fastq -o contigs.fasta`
**Explanation:** Uses mate pairs for assembly.

### K-mer size
**Args:** `fermi-lite assemble -i reads.fastq -o contigs.fasta -k 31`
**Explanation:** Uses 31-mers for assembly.

### Output statistics
**Args:** `fermi-lite assemble -i reads.fastq -o contigs.fasta -s stats.txt`
**Explanation:** Generates assembly statistics.