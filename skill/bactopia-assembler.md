---
name: bactopia-assembler
category: assembly
description: Bactopia Assembler - Assembly component of the Bactopia bioinformatics pipeline
tags: [bactopia-assembler, assembly, bacterial-genomics, pipeline, spades]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: Bactopia Assembler is the assembly component of the Bactopia pipeline, designed specifically for bacterial genome assembly. Version 1.0.5.
- **Core Function**: Performs de novo assembly of bacterial genomes from Illumina sequencing reads.
- **SPAdes Integration**: Uses SPAdes assembler as the core assembly engine with bacterial-specific optimizations.
- **Quality Trimming**: Integrates quality trimming and error correction before assembly.
- **Multiple Assemblers**: Supports different assembly strategies for optimal results.
- **Assembly Polishing**: Includes assembly polishing steps to improve consensus accuracy.
- **Input/Output**: Accepts FASTQ reads, outputs FASTA assembly contigs.
- **Installation**: `conda install -c bioconda bactopia-assembler`.

## Pitfalls

- **Memory Requirements**: Assembly is memory-intensive. Ensure sufficient RAM for large datasets.
- **Read Quality**: Poor quality reads can lead to fragmented assemblies. Perform quality filtering first.
- **Genome Complexity**: Highly repetitive genomes may result in misassemblies.
- **Contamination**: Contaminated reads can introduce foreign sequences into assemblies.
- **Version Compatibility**: Ensure compatibility with Bactopia pipeline version.

## Examples

### Basic assembly
**Args:** `bactopia-assembler --input R1.fastq.gz R2.fastq.gz --output assembly/`
**Explanation:** Assembles paired-end reads into bacterial genome contigs.

### With quality trimming
**Args:** `bactopia-assembler --input R1.fastq.gz R2.fastq.gz --trim --output assembly/`
**Explanation:** Performs quality trimming before assembly for improved results.

### Specify k-mers
**Args:** `bactopia-assembler --input R1.fastq.gz R2.fastq.gz --kmer-sizes 21,33,55 --output assembly/`
**Explanation:** Uses custom k-mer sizes for SPAdes assembly.

### Assembly polishing
**Args:** `bactopia-assembler --input R1.fastq.gz R2.fastq.gz --polish --output assembly/`
**Explanation:** Runs assembly polishing step to improve sequence accuracy.

### Single-end reads
**Args:** `bactopia-assembler --input reads.fastq.gz --single-end --output assembly/`
**Explanation:** Assembles single-end sequencing reads.

### With error correction
**Args:** `bactopia-assembler --input R1.fastq.gz R2.fastq.gz --error-correction --output assembly/`
**Explanation:** Enables SPAdes error correction for better assembly quality.

### Specify threads
**Args:** `bactopia-assembler --input R1.fastq.gz R2.fastq.gz --threads 16 --output assembly/`
**Explanation:** Uses specified number of threads for parallel processing.

### Display help
**Args:** `bactopia-assembler --help`
**Explanation:** Shows all available command-line options and usage information.