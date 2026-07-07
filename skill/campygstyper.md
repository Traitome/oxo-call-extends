---
name: campygstyper
category: typing
description: Genotyping tool for Campylobacter jejuni and Campylobacter coli
tags: [campygstyper, campylobacter, genotyping, mlst, typing]
author: oxo-call-community
source_url: "https://github.com/LanLab/campygstyper"
---

## Concepts

- **Tool Overview**: campygstyper performs genotyping of Campylobacter jejuni and Campylobacter coli isolates.
- **Core Function**: Assigns sequence types and identifies genomic markers for Campylobacter typing.
- **Algorithm**: Uses MLST and genomic marker detection for strain characterization.
- **Input**: Assembled Campylobacter genome in FASTA format.
- **Output**: Genotype information including sequence type and marker presence.
- **Application**: Campylobacter outbreak investigation and epidemiology.
- **Installation**: Install via bioconda: `conda install -c bioconda campygstyper`

## Pitfalls

- **Species Specific**: Designed for C. jejuni and C. coli only.
- **Assembly Required**: Requires assembled genome, not raw reads.
- **Database**: Uses built-in MLST and marker databases.
- **Quality**: Assembly quality affects genotyping accuracy.

## Examples

### Genotype Campylobacter isolate
**Args:** `campygstyper -i genome.fa -o genotype_results.tsv`
**Explanation:** Performs genotyping of Campylobacter isolate.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.