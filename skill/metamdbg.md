---
name: metamdbg
category: assembly
description: "MetaMDBG: a lightweight assembler for long and accurate metagenomics reads."
tags: [metamdbg, assembly, metagenomics, long-reads]
author: oxo-call-community
source_url: "https://github.com/GaetanBenoitDev/metaMDBG"
---
## Concepts

- **Tool Overview**: MetaMDBG v1.3.1 is a lightweight and efficient assembler specifically designed for long and accurate metagenomic sequencing reads.
- **Core Function**: Assembles long-read metagenomic data into contiguous sequences (contigs) efficiently.
- **Long Read Support**: Optimized for long sequencing reads from technologies like PacBio and Oxford Nanopore.
- **Lightweight**: Designed to be memory-efficient and fast for metagenomic assembly.
- **Input/Output**: Accepts FASTQ-formatted long reads; outputs assembled contigs in FASTA format.
- **Accuracy**: Maintains high assembly accuracy even with complex metagenomic samples.

## Pitfalls

- **Read Quality**: Assembly quality depends on input read quality and accuracy.
- **Computational Resources**: Large datasets may require significant computational resources.
- **Parameter Tuning**: May require parameter adjustment for optimal results with different datasets.
- **Contig Quality**: May produce fragmented assemblies for highly complex communities.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Assembly of large datasets can be time-consuming.

## Examples

### Assemble long-read metagenome
**Args:** `metamdbg -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles long-read metagenomic data into contigs.

### With custom k-mer size
**Args:** `metamdbg -i reads.fastq -k 51 -o assembly.fasta`
**Explanation:** Uses k-mer size of 51 for assembly.

### Specify output directory
**Args:** `metamdbg -i reads.fastq -o results/`
**Explanation:** Outputs assembly and intermediate files to specified directory.

### Run with verbose logging
**Args:** `metamdbg -i reads.fastq -o assembly.fasta -v`
**Explanation:** Enables verbose logging for debugging and progress tracking.

### Use multiple threads
**Args:** `metamdbg -i reads.fastq -o assembly.fasta -t 16`
**Explanation:** Uses 16 threads for parallel processing.