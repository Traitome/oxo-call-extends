---
name: gatb
category: assembly
description: GATB is a C++ library for efficient genome assembly and analysis using optimized de-Bruijn graphs with low memory footprint.
tags: [gatb, genome-assembly, de-bruijn-graph, library, cpp, ngs]
author: oxo-call-community
source_url: "https://gatb.inria.fr/"
---

## Concepts

- **Tool Overview**: GATB (Genome Assembly & Analysis Tool Box) is an open-source C++ library providing efficient algorithms for de-Bruijn graph-based genome assembly and analysis.
- **Core Function**: Implements optimized de-Bruijn graph data structures enabling complex genome assembly on desktop computers with limited resources.
- **Memory Efficiency**: Uses breakthrough memory optimization techniques allowing assembly of large genomes (including polyploid genomes) on standard hardware.
- **Library Design**: Provides a modular API for developers to build custom assembly tools without reimplementing core algorithms.
- **Key Components**: Includes minimizer-based indexing, Bloom filters for graph traversal, and parallelized graph algorithms.
- **Applications**: Whole genome assembly, metagenomics, variant calling, graph construction, k-mer counting.
- **License**: Released under A-GPL license for open source use.
- **Language**: C++ core with bindings/pipelines in Python and other languages.
- **Input**: Raw sequencing reads in FASTQ/FASTA format.
- **Output**: Assembled contigs, graphs in various formats, abundance information.

## Pitfalls

- **Library vs Application**: GATB is primarily a library, not a turn-key assembler. Users may need to write code using the API for custom workflows.
- **K-mer Selection**: K-mer size significantly affects assembly quality. Too small causes fragmentation, too large increases memory exponentially.
- **Error Correction**: Raw reads with high error rates can create bubbles in the de-Bruijn graph. Pre-error correction recommended.
- **Complex Genomes**: Polyploid and highly repetitive genomes require specialized parameter tuning.
- **Memory Configuration**:虽然设计为低内存，但某些操作仍可能需要大量RAM。监控峰值使用情况。
- **Dependencies**: Requires a C++ compiler (g++ 4.8+), CMake for building, and zlib for compression.
- **Threading**: Multi-threaded operations may cause issues on systems with limited cores or memory contention.

## Examples

### Install GATB from source
**Args:** `git clone https://github.com/GATB/gatb-core.git && cd gatb-core && mkdir build && cd build && cmake .. && make`
**Explanation:** Clones and builds the GATB core library from source code.

### Count k-mers
**Args:** `gatb-count -i reads.fastq -k 21 -o kmer_counts`
**Explanation:** Counts k-mer frequencies in input reads using GATB's efficient minimizer-based algorithm.

### Build de-Bruijn graph
**Args:** `gatb-graph -i reads.fastq -k 31 -o assembly_graph`
**Explanation:** Constructs de-Bruijn graph from reads for genome assembly visualization.

### Assemble genome
**Args:** `gatb-assemble -i reads.fastq -k 31 --abundance-min 2 -o contigs.fasta`
**Explanation:** Performs genome assembly from reads, outputting assembled contigs.

### Analyze graph coverage
**Args:** `gatb-info -g graph.before.gz -g2 graph.after.gz`
**Explanation:** Compares graph statistics before and after simplification to evaluate assembly quality.

### Use as C++ library
**Args:** `#include <gatb/gatb_core.hpp>` and link with -lgatb`
**Explanation:** Demonstrates embedding GATB algorithms in custom C++ applications.

### Python binding example
**Args:** `from gatb import Bank, Kmer; bank = Bank("reads.fastq"); kmers = Kmer(k=21).iteration(bank)`
**Explanation:** Uses Python API to iterate over k-mers from a sequence bank.
