---
name: abpoa
category: alignment
description: abPOA: fast SIMD-based partial order alignment using adaptive band.
tags: [abpoa, alignment, msa, poa, consensus, simd]
author: oxo-call-community
source_url: "https://github.com/yangao07/abPOA"
---

## Concepts

- **Tool Overview**: An SIMD-based C library for fast partial order alignment using adaptive banded dynamic programming. Performs multiple sequence alignment (MSA) and consensus calling. Version 1.5.6.
- **Core Function**: Aligns multiple sequences using a partial order alignment (POA) graph, enabling representation of structural variants and generation of consensus sequences.
- **Input/Output**: Input is FASTA/FASTQ sequences (possibly gzipped); output is consensus sequence (FASTA), MSA (FASTA), or graph (GFA).
- **Installation**: Install via bioconda: `conda install -c bioconda abpoa`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **SIMD Acceleration**: Uses SIMD (SSE4.1, AVX, AVX2, AVX512) for 10-30x speedup over standard POA implementations.
- **Adaptive Banded DP**: Uses adaptive banded dynamic programming to reduce memory and time complexity.
- **Multi-Allelic Support**: Can generate multiple consensus sequences for diploid/polyploid or multi-allelic inputs using `-d` flag.
- **Incremental Alignment**: Can align new sequences to an existing graph using `-i` flag.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **SIMD Variant**: Different binaries (abpoa, abpoa.avx2, abpoa.avx, abpoa.sse4.1) for different CPU capabilities. Use the highest supported version.
- **Consensus Method**: Default uses heaviest bundling method. Use `-a1` for most frequent base method which may differ for heterogeneous data.
- **Graph Complexity**: Highly diverse sequences produce complex graphs. Use `-r3` or `-r4` to visualize graph structure.
- **Amino Acid Mode**: Requires `-c` flag and scoring matrix (`-t BLOSUM62.mtx`) for protein sequences.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options, output formats, and SIMD variant information.

### Generate consensus sequence from multiple sequences
**Args:** `sequences.fasta`
**Explanation:** Reads sequences from FASTA file and outputs a consensus sequence to stdout. Uses default heaviest bundling method.

### Generate consensus with most frequent base method
**Args:** `-a1 sequences.fasta > consensus.fa`
**Explanation:** Uses the most frequent base method for consensus calling. May produce different results for heterogeneous samples.

### Generate multiple consensus sequences (diploid)
**Args:** `-d2 heterozygous.fasta > 2consensus.fa`
**Explanation:** Generates two consensus sequences for diploid or heterozygous input. Useful for haplotype separation.

### Output multiple sequence alignment (MSA)
**Args:** `-r1 sequences.fasta > alignment.msa`
**Explanation:** Outputs the multiple sequence alignment in FASTA format with gaps represented as `-`. Does not include consensus.

### Output MSA with consensus
**Args:** `-r2 sequences.fasta > alignment_with_consensus.msa`
**Explanation:** Outputs MSA in FASTA format with the consensus sequence appended. Useful for visualizing alignment quality.

### Output graph in GFA format
**Args:** `-r3 sequences.fasta > graph.gfa`
**Explanation:** Outputs the partial order alignment graph in GFA format. Useful for downstream graph analysis.

### Align sequences to existing graph
**Args:** `-i existing.gfa new_sequences.fasta -r3 > updated.gfa`
**Explanation:** Incrementally aligns new sequences to an existing POA graph. Efficient for adding sequences to a growing alignment.

### Process amino acid sequences
**Args:** `-c -t BLOSUM62.mtx proteins.fasta > consensus_protein.fa`
**Explanation:** Aligns amino acid sequences using the BLOSUM62 scoring matrix. Required for protein sequence MSA.

### Generate graph visualization
**Args:** `-g graph.png sequences.fasta > consensus.fa`
**Explanation:** Creates a PNG visualization of the POA graph. Requires graphviz to be installed.
