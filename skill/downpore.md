---
name: downpore
category: assembly
description: "Suite of tools for use in genome assembly and consensus."
tags: [downpore, assembly, genome-assembly, consensus-sequence]
author: oxo-call-community
source_url: "https://github.com/jteutenberg/downpore"
---

## Concepts

- **Tool Overview**: Downpore is a suite of tools for genome assembly and consensus sequence generation from nanopore sequencing data.
- **Core Function**: Provides utilities for error correction, consensus calling, and assembly refinement.
- **Input/Output**: Input: Raw nanopore reads (FASTQ), draft assembly (FASTA). Output: Polished consensus sequences.
- **Algorithm**: Uses k-mer based error correction and multiple sequence alignment for consensus generation.
- **Key Features**: Long-read support, hybrid assembly capabilities, parallel processing, quality-aware polishing.
- **Installation**: `conda install -c bioconda downpore`

## Pitfalls

- **Read Quality**: Poor quality reads can reduce assembly accuracy.
- **Memory Usage**: Large datasets may require significant memory resources.
- **Parameter Tuning**: k-mer size selection affects error correction performance.
- **Contamination**: Foreign DNA sequences can contaminate assemblies.
- **Repeat Regions**: Highly repetitive sequences can cause assembly errors.

## Examples

### Basic consensus generation
**Args:** `--reads reads.fastq --draft draft.fasta --output consensus.fasta`
**Explanation:** Generates consensus sequence from raw reads and draft assembly.

### Error correction
**Args:** `--reads reads.fastq --output corrected.fastq --correct`
**Explanation:** Performs error correction on raw nanopore reads.

### Hybrid assembly
**Args:** `--long reads.fastq --short short_reads.fastq --output hybrid.fasta`
**Explanation:** Combines long and short reads for hybrid assembly.

### Parallel processing
**Args:** `--reads reads.fastq --draft draft.fasta --output consensus.fasta --threads 16`
**Explanation:** Uses 16 threads for parallel processing to speed up analysis.

### Quality filtering
**Args:** `--reads reads.fastq --draft draft.fasta --output consensus.fasta --min-quality 10`
**Explanation:** Filters out low-quality reads with Phred score below 10.