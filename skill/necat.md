---
name: necat
category: assembly
description: NECAT is an error correction and de-novo assembly tool specifically designed for Nanopore long noisy reads.
tags: [necat, assembly, nanopore, long-reads, error-correction]
author: oxo-call-community
source_url: "https://github.com/xiaochuanle/NECAT"
---

## Concepts

- **Tool Overview**: NECAT is a de novo assembler optimized for Oxford Nanopore long-read sequencing data.
- **Core Function**: Performs error correction and assembly of long, noisy sequencing reads.
- **Algorithm**: Uses overlap-layout-consensus approach with specialized error correction for Nanopore data.
- **Input Format**: Accepts FASTQ files from Nanopore sequencing runs.
- **Output**: Produces assembled contigs in FASTA format with quality statistics.
- **Use Case**: Genome assembly from Nanopore data, metagenomic assembly, and long-read assembly projects.

## Pitfalls

- **Computational Cost**: Assembly of large genomes requires significant computational resources.
- **Memory Usage**: Can consume large amounts of memory for complex assemblies.
- **Input Quality**: Performance depends on input read quality and coverage.
- **Version Differences**: Options may vary between versions.
- **Parameter Tuning**: Requires careful parameter adjustment for optimal results.
- **Output Quality**: Assembly quality may vary based on input data characteristics.

## Examples

### Display help
**Args:** `necat --help`
**Explanation:** Shows available options and usage instructions.

### Basic assembly
**Args:** `necat assemble -c config.txt -o output_dir`
**Explanation:** Runs NECAT assembly with configuration file.

### Create configuration
**Args:** `necat config -t nanopore -i reads.fastq -o config.txt`
**Explanation:** Generates assembly configuration file.

### Error correction only
**Args:** `necat correct -c config.txt -o corrected_reads/`
**Explanation:** Performs error correction without assembly.

### Assembly with reference
**Args:** `necat assemble -c config.txt -r reference.fasta -o output_dir`
**Explanation:** Uses reference-guided assembly approach.

### Threads
**Args:** `necat assemble -c config.txt -t 16 -o output_dir`
**Explanation:** Uses 16 threads for parallel processing.