---
name: aviary
category: metagenomics
description: Aviary - Hybrid assembly and metagenomic pipeline for long and short reads
tags: [metagenomics, hybrid-assembly, binning, annotation, snakemake]
author: oxo-call-community
source_url: "https://github.com/rhysnewell/aviary"
---

## Concepts

- **Tool Overview**: Aviary is a Snakemake-based pipeline for metagenomic hybrid assembly, binning, and annotation, supporting both short-read and long-read data.

- **Hybrid Assembly**: Combines short-read (Illumina) and long-read (Nanopore/PacBio) data for improved metagenome assembly quality.

- **Multiple Assemblers**: Supports various assemblers including metaSPAdes, MEGAHIT, Flye, and hybrid approaches.

- **Automated Binning**: Includes automated binning with multiple tools and consensus binning approaches.

- **Functional Annotation**: Provides automated functional annotation of recovered genomes.

- **Strain Diversity**: Analyzes strain-level diversity within recovered genomes.

## Pitfalls

- **Snakemake Dependency**: Requires Snakemake workflow manager and conda/mamba for environment management.

- **Resource Requirements**: Hybrid assembly is computationally intensive. Ensure adequate CPU and memory.

- **Input Requirements**: Best results require both short and long reads. Short-read-only mode has reduced assembly quality.

- **Conda Environments**: Creates multiple conda environments during execution. Ensure sufficient disk space.

## Examples

### Basic hybrid assembly
**Args:** `aviary assemble --longreads nanopore.fastq.gz --shortreads illumina_R1.fastq.gz illumina_R2.fastq.gz --output results/`
**Explanation:** Runs hybrid metagenomic assembly using both long and short reads.

### Short-read only assembly
**Args:** `aviary assemble --shortreads R1.fastq.gz R2.fastq.gz --output results/`
**Explanation:** Performs short-read-only metagenomic assembly when long reads unavailable.

### Long-read only assembly
**Args:** `aviary assemble --longreads reads.fastq.gz --output results/`
**Explanation:** Performs long-read-only assembly for Nanopore or PacBio data.

### Full pipeline with binning and annotation
**Args:** `aviary process --longreads nanopore.fastq.gz --shortreads R1.fastq.gz R2.fastq.gz --output results/`
**Explanation:** Runs complete pipeline: assembly, binning, annotation, and strain analysis.

### Custom assembler selection
**Args:** `aviary assemble --longreads reads.fastq.gz --shortreads R1.fq.gz R2.fq.gz --assembler metaflye,metaspades --output results/`
**Explanation:** Uses specific assemblers (metaFlye and metaSPAdes) instead of defaults.

### Specify threads and memory
**Args:** `aviary assemble --longreads reads.fastq.gz --shortreads R1.fq.gz R2.fq.gz --threads 32 --memory 128 --output results/`
**Explanation:** Limits resource usage to 32 threads and 128GB memory.
