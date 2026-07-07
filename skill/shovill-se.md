---
name: shovill-se
category: assembly
description: shovill-se - Microbial assembly pipeline supporting single-end reads
tags: ["shovill-se", "assembly", "microbial", "single-end"]
author: oxo-call-community
source_url: "https://github.com/rpetit3/shovill"
---

## Concepts

- **Tool Overview**: shovill-se (v1.1.0se) is a fork of Shovill supporting single-end reads.
- **Core Function**: Assembles microbial genomes from single-end Illumina sequencing data.
- **Algorithm**: Uses SPAdes or SKESA assembler optimized for single-end reads.
- **Input/Output**: Accepts single-end FASTQ reads and produces assembled contigs.
- **Single-end Support**: Specialized for single-end sequencing data.
- **Applications**: Microbial genome assembly with single-end data.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Read Quality**: Single-end reads require higher quality than paired-end.
- **Assembly Quality**: May produce lower quality assemblies than paired-end.
- **Parameter Tuning**: Requires careful adjustment for different organisms.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation compared to original Shovill.

## Examples

### Assemble with single-end reads
**Args:** `shovill-se --SE reads.fastq --outdir output/`
**Explanation:** Basic single-end assembly.

### With reference
**Args:** `shovill-se --SE reads.fastq --ref reference.fasta --outdir output/`
**Explanation:** `--ref` uses reference-guided assembly.

### With SPAdes
**Args:** `shovill-se --SE reads.fastq --assembler spades --outdir output/`
**Explanation:** `--assembler spades` uses SPAdes assembler.

### Help command
**Args:** `shovill-se --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shovill-se --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shovill-se --SE reads.fastq --threads 8 --outdir output/`
**Explanation:** `--threads 8` uses 8 threads.

### With trimming
**Args:** `shovill-se --SE reads.fastq --trim --outdir output/`
**Explanation:** `--trim` enables read trimming.
