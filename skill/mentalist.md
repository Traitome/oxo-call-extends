---
name: mentalist
category: utility
description: MLST (Multi-Locus Sequence Typing) pipeline for bacterial strain typing.
tags: [mentalist, mlst, bacterial-typing]
author: oxo-call-community
source_url: "https://github.com/WGS-TB/MentaLiST"
---

## Concepts

- **Tool Overview**: MentaLiST performs MLST typing on bacterial genomes.
- **Core Function**: Multi-locus sequence typing.
- **Allele Calling**: Identifies alleles at MLST loci.
- **ST Determination**: Determines sequence type.
- **Database Support**: Supports multiple MLST databases.
- **Installation**: `conda install -c bioconda mentalist`

## Pitfalls

- **Species Specific**: Database must match target species.
- **Data Quality**: Requires good quality sequencing data.
- **Database Updates**: Needs updated MLST databases.
- **Ambiguous Calls**: May produce uncertain allele calls.
- **Assembly Quality**: Depends on assembly completeness.
- **Computation Time**: Slow for large datasets.

## Examples

### Run MLST typing
**Args:** `mentalist --input reads.fastq --output results/`
**Explanation:** Performs MLST typing on reads.

### With assembly
**Args:** `mentalist --assembly genome.fasta --output results/`
**Explanation:** Uses assembled genome for typing.

### Specify species
**Args:** `mentalist --input reads.fastq --species tb --output results/`
**Explanation:** Specifies target species database.

### Verbose mode
**Args:** `mentalist --input reads.fastq -v --output results/`
**Explanation:** Shows detailed typing progress.

### Help documentation
**Args:** `mentalist --help`
**Explanation:** Displays available options.
