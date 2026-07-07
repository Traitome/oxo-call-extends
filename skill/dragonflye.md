---
name: dragonflye
category: assembly
description: Dragonflye - Microbial genome assembly pipeline for Nanopore reads.
tags: [dragonflye, assembly, nanopore, microbial-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rpetit3/dragonflye"
---

## Concepts

- **Tool Overview**: Dragonflye is a complete microbial genome assembly pipeline optimized for Oxford Nanopore sequencing data.
- **Core Function**: Takes raw Nanopore reads and produces high-quality microbial genome assemblies.
- **Input/Output**: Input: FASTQ reads (raw or basecalled). Output: Assembled contigs, quality reports, annotations.
- **Algorithm**: Combines read filtering, error correction, assembly, polishing, and quality assessment.
- **Key Features**: End-to-end pipeline, hybrid assembly support, automatic QC, annotation integration, long-read optimization.
- **Installation**: `conda install -c bioconda dragonflye`

## Pitfalls

- **Input Quality**: Poor quality Nanopore reads can lead to fragmented assemblies.
- **Memory Requirements**: Assembly of large genomes requires significant RAM.
- **Basecalling**: Requires properly basecalled reads; raw signal data is not supported.
- **Contamination**: Host or adapter sequences should be removed before assembly.
- **Computation Time**: Assembly of complex genomes can be computationally intensive.
- **Repeat Regions**: Highly repetitive regions may cause misassembly.

## Examples

### Basic assembly
**Args:** `dragonflye --reads reads.fq --output assembly`
**Explanation:** Runs the complete assembly pipeline on Nanopore reads.

### With reference-guided assembly
**Args:** `dragonflye --reads reads.fq --output assembly --reference ref.fa`
**Explanation:** Uses a reference genome to guide assembly and improve contiguity.

### Hybrid assembly with Illumina reads
**Args:** `dragonflye --reads nanopore.fq --illumina illumina.fq --output assembly`
**Explanation:** Combines Nanopore long reads with Illumina short reads for hybrid assembly.

### Skip polishing steps
**Args:** `dragonflye --reads reads.fq --output assembly --skip-polish`
**Explanation:** Skips the polishing steps for faster assembly (lower quality output).

### With custom k-mer size
**Args:** `dragonflye --reads reads.fq --output assembly --kmer 100`
**Explanation:** Specifies a custom k-mer size for the assembler.

### Enable annotation
**Args:** `dragonflye --reads reads.fq --output assembly --annotate`
**Explanation:** Runs Prokka annotation on the assembled genome.