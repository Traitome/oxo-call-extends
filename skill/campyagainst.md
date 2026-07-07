---
name: campyagainst
category: taxonomy
description: Accurate assignment of ANI genomic species to Campylobacter genomes
tags: [campyagainst, campylobacter, ani, taxonomy, species-assignment]
author: oxo-call-community
source_url: "https://github.com/LanLab/campyagainst"
---

## Concepts

- **Tool Overview**: campyagainst assigns genomic species to Campylobacter genomes using ANI (Average Nucleotide Identity).
- **Core Function**: Determines species identity of Campylobacter isolates based on genomic similarity.
- **Algorithm**: Uses ANI calculations against reference Campylobacter genomes.
- **Input**: Assembled Campylobacter genome in FASTA format.
- **Output**: Species assignment with ANI scores.
- **Application**: Campylobacter species identification and typing.
- **Installation**: Install via bioconda: `conda install -c bioconda campyagainst`

## Pitfalls

- **Campylobacter Specific**: Designed only for Campylobacter genus.
- **Assembly Required**: Requires assembled genome, not raw reads.
- **ANI Threshold**: Species assignment depends on ANI cutoff values.
- **Reference Database**: Uses built-in Campylobacter reference genomes.

## Examples

### Assign species to genome
**Args:** `campyagainst -i genome.fa -o species_assignment.tsv`
**Explanation:** Assigns species to Campylobacter genome using ANI.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.