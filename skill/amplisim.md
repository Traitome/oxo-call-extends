---
name: amplisim
category: qc
description: Plain simple amplicon sequence simulator for in-silico genomic sequencing assays
tags: [amplisim, amplicon, simulation, in-silico, sequencing]
author: oxo-call-community
source_url: "https://github.com/rki-mf1/amplisim"
---

## Concepts

- **Tool Overview**: Amplisim is a plain simple amplicon sequence simulator for in-silico genomic sequencing assays. Version 0.2.1.
- **Core Function**: Simulates amplicon sequences from a reference genome using primer definitions, useful for testing and validating amplicon sequencing workflows.
- **Input/Output**: Inputs: Reference genome (FASTA), primer definitions (BED format); Outputs: Simulated amplicon sequences (FASTA).
- **Installation**: Available via Bioconda (`conda install -c bioconda amplisim`) or from source.
- **Key Features**: Configurable amplicon replicates, amplicon dropout simulation, random seed support, BED format primer input.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Primer file must be in BED format; reference must be FASTA format.
- **Primer Specificity**: Primers must correctly match reference genome coordinates.
- **Chromosome Matching**: Chromosome identifiers in BED file must match those in FASTA reference.
- **Dropout Rate**: Default dropout rate is 0; adjust with `-x` flag for realistic simulations.

## Examples

### Basic amplicon simulation
**Args:** `amplisim reference.fasta primers.bed > amplicons.fasta`
**Explanation:** Simulates amplicon sequences from reference using primers in BED format, outputs to stdout.

### Output to file
**Args:** `amplisim -o amplicons.fasta reference.fasta primers.bed`
**Explanation:** Simulates amplicons and saves directly to output FASTA file.

### Set amplicon coverage
**Args:** `amplisim -m 100 -n 10 reference.fasta primers.bed`
**Explanation:** Sets mean amplicon replicates to 100 with standard deviation of 10.

### Enable amplicon dropout
**Args:** `amplisim -x 0.1 reference.fasta primers.bed`
**Explanation:** Sets 10% likelihood for amplicon dropout (missing amplicons).

### Set random seed
**Args:** `amplisim -s 42 reference.fasta primers.bed`
**Explanation:** Sets random seed for reproducible simulation results.

### Show help
**Args:** `amplisim --help`
**Explanation:** Displays available options and usage information.

### Combine multiple options
**Args:** `amplisim -o output.fasta -m 50 -n 5 -x 0.05 -s 123 reference.fasta primers.bed`
**Explanation:** Full simulation with 50 mean replicates, SD 5, 5% dropout, seed 123.