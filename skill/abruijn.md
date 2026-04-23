---
name: abruijn
category: assembly
description: Long read assembly via A-Bruijn graph
tags: [abruijn, assembly, long-read, de-bruijn, pacbio, nanopore]
author: oxo-call-community
source_url: "https://github.com/fenderglass/ABruijn/"
---

## Concepts

- **Tool Overview**: Long read assembler using the A-Bruijn graph approach, designed for PacBio and Nanopore reads. Version 2.1b.
- **Core Function**: Assembles long reads into contigs using an A-Bruijn graph structure that handles higher error rates of long reads.
- **Input/Output**: Input is long reads (FASTA/FASTQ); output is assembled contigs (FASTA).
- **Installation**: Install via bioconda: `conda install -c bioconda abruijn`
- **Platform Support**: Linux (x86_64) and macOS (x86_64)
- **Long Read Optimized**: Designed specifically for error-prone long reads from PacBio and Oxford Nanopore.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Long Read Only**: Not designed for short read assembly. Use other assemblers for Illumina data.
- **Error Rate**: While tolerant of errors, extremely high error rates may degrade assembly quality.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic long read assembly
**Args:** `reads.fasta -o assembly_output/`
**Explanation:** Assembles long reads into contigs and writes output to the specified directory.

### Assembly with custom parameters
**Args:** `--min-ovlp 2000 reads.fasta -o results/`
**Explanation:** Sets minimum overlap to 2000bp for more stringent assembly. Higher values reduce misassemblies but may fragment the assembly.
