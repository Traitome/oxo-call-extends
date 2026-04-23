---
name: abeona
category: assembly
description: A simple transcriptome assembler based on kallisto and Cortex graphs.
tags: [abeona, assembly, transcriptome, kallisto, cortex]
author: oxo-call-community
source_url: "https://github.com/winni2k/abeona"
---

## Concepts

- **Tool Overview**: A transcriptome assembler that combines kallisto quantification with Cortex graph-based assembly. Version 0.45.0.
- **Core Function**: Assembles transcriptomes using kallisto for quantification guidance and Cortex de Bruijn graphs for assembly.
- **Input/Output**: Input is RNA-seq reads (FASTQ); output is assembled transcripts (FASTA).
- **Installation**: Install via bioconda: `conda install -c bioconda abeona`
- **Platform Support**: Linux (x86_64) and platform-independent
- **Kallisto Integration**: Uses kallisto for rapid transcript quantification to guide assembly.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Kallisto Dependency**: Requires kallisto to be installed and in PATH.
- **Memory Usage**: Cortex graph construction can be memory-intensive for large transcriptomes.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic transcriptome assembly
**Args:** `--reads reads_1.fastq reads_2.fastq --output assembly_output/`
**Explanation:** Assembles transcripts from paired-end RNA-seq reads using kallisto-guided Cortex graph assembly.

### Assembly with custom k-mer size
**Args:** `--kmer 31 --reads reads.fastq --output results/`
**Explanation:** Uses 31-mers for the de Bruijn graph construction. K-mer size affects assembly contiguity and error rate.
