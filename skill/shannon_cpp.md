---
name: shannon_cpp
category: assembly
description: shannon_cpp - De novo RNA-seq transcript assembly
tags: ["shannon_cpp", "assembly", "RNA-seq", "transcript"]
author: oxo-call-community
source_url: "https://github.com/bx3/shannon_cpp.git"
---

## Concepts

- **Tool Overview**: shannon_cpp (v0.5.0) is a command line tool for de novo RNA assembly.
- **Core Function**: Assembles transcripts from RNA-seq data.
- **Algorithm**: Uses de Bruijn graph approach for transcript assembly.
- **Input/Output**: Accepts FASTQ reads and produces assembled transcripts.
- **RNA Assembly**: Focuses on transcript reconstruction from sequencing data.
- **Applications**: RNA-seq analysis, transcriptomics, and gene expression studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Assemble transcripts
**Args:** `shannon_cpp -i reads.fastq -o transcripts.fasta`
**Explanation:** `-i` input reads; `-o` output transcripts.

### Paired-end
**Args:** `shannon_cpp -1 reads_1.fastq -2 reads_2.fastq -o transcripts.fasta`
**Explanation:** `-1/-2` paired-end reads.

### With reference
**Args:** `shannon_cpp -i reads.fastq -r reference.fasta -o transcripts.fasta`
**Explanation:** `-r` reference genome.

### Verbose logging
**Args:** `shannon_cpp -v -i reads.fastq -o transcripts.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shannon_cpp --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shannon_cpp --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shannon_cpp -t 8 -i reads.fastq -o transcripts.fasta`
**Explanation:** `-t 8` uses 8 threads.