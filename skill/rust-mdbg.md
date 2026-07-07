---
name: rust-mdbg
category: assembly
description: An ultra-fast minimizer-space de Bruijn graph (mdBG) implementation for long-read assembly.
tags: ["rust-mdbg", "assembly", "de Bruijn graph", "long reads", "minimizer"]
author: oxo-call-community
source_url: "https://github.com/ekimb/rust-mdbg"
---

## Concepts

- **Tool Overview**: rust-mdbg (v1.0.1) is an ultra-fast minimizer-space de Bruijn graph (mdBG) assembler designed for long and accurate reads. It leverages minimizer sampling to reduce memory usage while maintaining assembly quality.
- **Core Function**: Constructs de Bruijn graphs from sequencing reads using minimizer-based k-mer sampling, enabling efficient assembly of large genomes with reduced memory footprint.
- **Algorithm**: Uses minimizer sampling to represent sequences in a compressed space, constructs the de Bruijn graph, and performs graph traversal to generate contigs.
- **Input Format**: FASTQ/FASTA files containing long reads (PacBio/ONT). Supports both single-end and paired-end reads.
- **Output Format**: FASTA files with assembled contigs, graph statistics, and optional assembly graphs in GFA format.
- **Use Case**: Genome assembly from long reads, metagenomic assembly, hybrid assembly combining short and long reads.

## Pitfalls

- **Read quality dependency**: Requires high-quality long reads for optimal results.
- **Memory requirements**: Still memory-intensive for very large genomes.
- **Parameter sensitivity**: k-mer size and minimizer settings significantly affect assembly quality.
- **Complex genomes**: Struggles with highly repetitive or polyploid genomes.
- **Assembly completeness**: May not fully resolve all genomic regions.
- **Output contiguity**: Contig N50 may vary significantly based on input data quality.

## Examples

### Basic assembly
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta`
**Explanation:** `-i` input reads; `-o` output FASTA with assembled contigs.

### Specify k-mer size
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta -k 21`
**Explanation:** `-k` k-mer size for de Bruijn graph construction.

### With minimizer window
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta -w 5`
**Explanation:** `-w` minimizer window size for sampling.

### Output graph
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta --graph graph.gfa`
**Explanation:** `--graph` outputs assembly graph in GFA format.

### Threaded assembly
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta -t 16`
**Explanation:** `-t` number of threads for parallel processing.

### Minimum contig length
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta -m 1000`
**Explanation:** `-m` minimum contig length to output (default: 500).

### Verbose mode
**Args:** `rust-mdbg -i reads.fastq -o assembly.fasta -v`
**Explanation:** `-v` verbose output showing assembly progress.
