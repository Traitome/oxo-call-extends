---
name: shannon
category: expression
description: shannon - RNA-Seq transcript assembly
tags: ["shannon", "expression", "RNA-seq", "assembly"]
author: oxo-call-community
source_url: "http://sreeramkannan.github.io/Shannon/"
---

## Concepts

- **Tool Overview**: shannon (v0.0.2) assembles transcripts from RNA-Seq data.
- **Core Function**: Reconstructs transcript sequences from RNA-seq reads.
- **Algorithm**: Uses graph-based approach for transcript assembly.
- **Input/Output**: Accepts BAM/FASTQ files and produces assembled transcripts.
- **Transcript Assembly**: Focuses on reconstructing full-length transcripts.
- **Applications**: RNA-seq analysis, gene expression quantification, and transcriptomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Assemble transcripts
**Args:** `shannon -i input.bam -g annotation.gtf -o output.fasta`
**Explanation:** `-i` input BAM; `-g` annotation; `-o` output transcripts.

### From FASTQ
**Args:** `shannon -i reads.fastq -g annotation.gtf -o output.fasta`
**Explanation:** Input FASTQ reads.

### With reference
**Args:** `shannon -i input.bam -r reference.fasta -g annotation.gtf -o output.fasta`
**Explanation:** `-r` reference genome.

### Verbose logging
**Args:** `shannon -v -i input.bam -g annotation.gtf -o output.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shannon --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shannon --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shannon -t 8 -i input.bam -g annotation.gtf -o output.fasta`
**Explanation:** `-t 8` uses 8 threads.