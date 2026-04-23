---
name: canu
category: assembly
description: Single-molecule sequencing assembler for high-noise long reads
tags: [canu, assembly, long-read, pacbio, ont]
author: oxo-call-community
source_url: "https://github.com/marbl/canu"
---

## Concepts

- **Tool Overview**: Canu is a fork of Celera Assembler designed for high-noise single-molecule sequencing (PacBio, ONT).
- **Core Function**: Assembles long reads with high error rates into contiguous sequences.
- **Workflow**: Correct reads → Trim reads → Assemble contigs.
- **Input**: FASTQ/FASTA files from PacBio or Oxford Nanopore.
- **Output**: Assembled contigs in FASTA format.
- **Features**: Automatic read correction and adapter trimming.
- **Installation**: Install via bioconda: `conda install -c bioconda canu`

## Pitfalls

- **Memory Usage**: Very memory-intensive; use grid mode for large genomes.
- **Runtime**: Large genomes can take days to assemble.
- **Read Correction**: Correction step is optional but recommended for high-error data.
- **Genome Size**: Must specify estimated genome size with genomeSize parameter.
- **Overlapping**: Overlap computation is the slowest step.

## Examples

### Assemble long reads
**Args:** `canu -p assembly -d output/ genomeSize=100m -pacbio-raw reads.fq`
**Explanation:** Assembles PacBio reads with 100Mbp estimated genome size.

### Assemble Nanopore reads
**Args:** `canu -p assembly -d output/ genomeSize=3g -nanopore-raw reads.fq`
**Explanation:** Assembles ONT reads with 3Gbp estimated genome size (human).

### Skip correction step
**Args:** `canu -p assembly -d output/ genomeSize=100m -pacbio-corrected reads.fq`
**Explanation:** Skips correction for pre-corrected PacBio reads.

### Use grid mode
**Args:** `canu -p assembly -d output/ genomeSize=3g -nanopore-raw reads.fq gridOptions='-q batch'`
**Explanation:** Submits canu jobs to grid scheduler for large genomes.

### Set coverage parameters
**Args:** `canu -p assembly -d output/ genomeSize=100m -pacbio-raw reads.fq corOutCoverage=100`
**Explanation:** Limits corrected read output to 100x coverage.

### Adjust overlap parameters
**Args:** `canu -p assembly -d output/ genomeSize=100m -pacbio-raw reads.fq ovlMemory=32`
**Explanation:** Uses more memory (32GB) for faster overlap computation.

### Trim only mode
**Args:** `canu -p assembly -d output/ genomeSize=100m -pacbio-raw reads.fq -trim`
**Explanation:** Runs only trimming step without assembly.
