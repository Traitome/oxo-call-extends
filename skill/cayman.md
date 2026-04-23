---
name: cayman
category: metagenomics
description: Profiling tool for CAZyme abundances in metagenomic datasets
tags: [cayman, cazyme, carbohydrate, metagenomics, profiling]
author: oxo-call-community
source_url: "https://github.com/zellerlab/cayman"
---

## Concepts

- **Tool Overview**: Cayman profiles CAZyme (carbohydrate-active enzyme) abundances in metagenomes.
- **Core Function**: Quantifies CAZyme families from metagenomic sequencing data.
- **Algorithm**: Maps reads to CAZyme database and quantifies family abundances.
- **Input**: FASTQ reads or assembled contigs.
- **Output**: CAZyme family abundance tables.
- **Application**: Gut microbiome carbohydrate metabolism studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cayman`

## Pitfalls

- **Database Required**: Requires CAZyme database for annotation.
- **Read Length**: Works best with reads >50bp.
- **Normalization**: Abundances may need normalization by sequencing depth.

## Examples

### Profile CAZymes from reads
**Args:** `cayman -i reads.fq -o cazyme_profile.tsv`
**Explanation:** Profiles CAZyme family abundances from metagenomic reads.

### Profile from contigs
**Args:** `cayman -i contigs.fa --contigs -o cazyme.tsv`
**Explanation:** Profiles CAZymes from assembled contigs.

### Display help
**Args:** `cayman --help`
**Explanation:** Shows all available options and usage information.
