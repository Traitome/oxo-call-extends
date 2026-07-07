---
name: nextdenovo
category: assembly
description: NextDenovo is a string graph-based de novo assembler for long reads from PacBio (CLR, HiFi) and Oxford Nanopore.
tags: [nextdenovo, assembly, long-reads, pacbio, nanopore]
author: oxo-call-community
source_url: "https://github.com/Nextomics/NextDenovo"
---

## Concepts

- **Tool Overview**: NextDenovo is an efficient de novo assembler optimized for long-read sequencing data.
- **Core Function**: Assembles long reads into contiguous sequences using string graph approach.
- **Algorithm**: Uses string graph construction with overlap detection and error correction.
- **Input Format**: Accepts FASTQ files from PacBio CLR, HiFi, or Oxford Nanopore sequencing.
- **Output**: Produces assembled contigs in FASTA format.
- **Use Case**: Genome assembly, metagenomic assembly, and long-read sequencing projects.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Quality**: Results depend on input read quality.
- **Memory Usage**: Large genomes require significant memory.
- **Computational Cost**: Assembly can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Complex Genomes**: Highly repetitive genomes may cause assembly issues.

## Examples

### Display help
**Args:** `nextDenovo --help`
**Explanation:** Shows available options and usage instructions.

### Basic assembly
**Args:** `nextDenovo config.cfg`
**Explanation:** Runs assembly using configuration file.

### Generate config
**Args:** `nextDenovo -g 3.2g -i reads.fastq -o output/ --cfg > config.cfg`
**Explanation:** Generates configuration file for assembly.

### HiFi assembly
**Args:** `nextDenovo -g 3.2g -i hifi_reads.fastq -o hifi_assembly/`
**Explanation:** Assembles HiFi reads.

### Nanopore assembly
**Args:** `nextDenovo -g 3.2g -i nanopore_reads.fastq -o nanopore_assembly/`
**Explanation:** Assembles Nanopore reads.

### With correction
**Args:** `nextDenovo -g 3.2g -i reads.fastq -o output/ --correct`
**Explanation:** Runs assembly with error correction.

### Multiple threads
**Args:** `nextDenovo -g 3.2g -i reads.fastq -o output/ -t 32`
**Explanation:** Uses 32 threads for parallel processing.