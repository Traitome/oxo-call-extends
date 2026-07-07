---
name: hifiasm
category: bioinformatics
description: hifiasm is a haplotype-resolved assembler for accurate PacBio HiFi reads.
tags: [hifiasm, genome-assembly, PacBio, HiFi, bioinformatics]
author: oxo-call-community
source_url: "https://hifiasm.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Haplotype-Resolved Assembly**: hifiasm assembles genomes with phased haplotypes.

- **PacBio HiFi**: Optimized for PacBio HiFi sequencing data.

- **De Novo Assembly**: Performs de novo genome assembly.

- **Phased Assembly**: Generates phased contigs.

- **Long Reads**: Handles long read sequencing data.

- **Hi-C Integration**: Supports Hi-C data for scaffolding.

## Pitfalls

- **Data Quality**: Results depend on HiFi read quality.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large genomes may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Assembly Validation**: Validate assembly quality after completion.

## Examples

### Assemble genome
**Args:** `hifiasm -o assembly.hifiasm reads.fastq`
**Explanation:** Assembles genome from HiFi reads.

### With Hi-C data
**Args:** `hifiasm -o assembly.hifiasm --h1 hic_1.fastq --h2 hic_2.fastq reads.fastq`
**Explanation:** Integrates Hi-C data for scaffolding.

### Batch processing
**Args:** `for f in *.fastq; do hifiasm -o ${f%.fastq}.hifiasm $f; done`
**Explanation:** Processes multiple HiFi datasets.

### Generate phased contigs
**Args:** `hifiasm -o assembly.hifiasm --primary reads.fastq`
**Explanation:** Generates primary assembly.

### Help command
**Args:** `hifiasm --help`
**Explanation:** Shows available options and usage information.