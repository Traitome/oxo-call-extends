---
name: carpedeam
category: assembly
description: Metagenomic assembler for heavily damaged ancient DNA datasets
tags: [carpedeam, ancient-dna, metagenomics, assembly, damage]
author: oxo-call-community
source_url: "https://github.com/LouisPwr/CarpeDeam"
---

## Concepts

- **Tool Overview**: CarpeDeam assembles metagenomes from heavily damaged ancient DNA.
- **Core Function**: Handles ancient DNA damage patterns during assembly.
- **Algorithm**: Accounts for deamination and fragmentation patterns in ancient DNA.
- **Input**: Ancient DNA FASTQ files.
- **Output**: Assembled contigs accounting for damage patterns.
- **Application**: Ancient metagenomics and paleogenomics.
- **Installation**: Install via bioconda: `conda install -c bioconda carpedeam`

## Pitfalls

- **Ancient DNA**: Specifically designed for damaged ancient DNA data.
- **Damage Patterns**: Assumes typical ancient DNA damage profile.
- **Coverage**: Low coverage typical of ancient DNA may limit assembly.

## Examples

### Assemble ancient DNA
**Args:** `carpedeam -i ancient_reads.fq -o assembly.fa`
**Explanation:** Assembles ancient DNA reads accounting for damage patterns.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
