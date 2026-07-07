---
name: shovill
category: assembly
description: shovill - Microbial assembly pipeline for Illumina paired-end reads
tags: ["shovill", "assembly", "microbial", "illumina"]
author: oxo-call-community
source_url: "https://github.com/tseemann/shovill"
---

## Concepts

- **Tool Overview**: shovill (v1.4.2) is a microbial genome assembly pipeline for Illumina reads.
- **Core Function**: Assembles bacterial and viral genomes from paired-end sequencing data.
- **Algorithm**: Uses SPAdes or SKESA assembler with preprocessing steps.
- **Input/Output**: Accepts FASTQ reads and produces assembled contigs.
- **Microbial Assembly**: Optimized for small microbial genomes.
- **Applications**: Bacterial genome sequencing, pathogen identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Read Quality**: Requires high-quality sequencing data.
- **Parameter Tuning**: Requires careful adjustment for different organisms.
- **Reference Bias**: May be biased towards reference sequences.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Assemble genome
**Args:** `shovill --R1 reads_1.fastq --R2 reads_2.fastq --outdir output/`
**Explanation:** Basic paired-end assembly.

### With reference
**Args:** `shovill --R1 reads_1.fastq --R2 reads_2.fastq --ref reference.fasta --outdir output/`
**Explanation:** `--ref` uses reference-guided assembly.

### With SPAdes
**Args:** `shovill --R1 reads_1.fastq --R2 reads_2.fastq --assembler spades --outdir output/`
**Explanation:** `--assembler spades` uses SPAdes assembler.

### Help command
**Args:** `shovill --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shovill --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shovill --R1 reads_1.fastq --R2 reads_2.fastq --threads 8 --outdir output/`
**Explanation:** `--threads 8` uses 8 threads.

### With trimming
**Args:** `shovill --R1 reads_1.fastq --R2 reads_2.fastq --trim --outdir output/`
**Explanation:** `--trim` enables read trimming.
