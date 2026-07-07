---
name: kleborate
category: annotation
description: "Kleborate: a tool for typing and screening pathogen genome assemblies."
tags: [kleborate, annotation, pathogen, typing, Klebsiella, screening]
author: oxo-call-community
source_url: "https://kleborate.readthedocs.io"
---
## Concepts

- **Pathogen Genotyping**: Types bacterial pathogen genomes for species, MLST, and virulence markers
- **Resistance Screening**: Screens for antimicrobial resistance genes and mutations
- **Klebsiella Analysis**: Specialized for Klebsiella pneumoniae complex species identification
- **Genome Assembly Quality**: Assesses quality of genome assemblies before analysis
- **Plasmid Detection**: Identifies plasmid-born resistance and virulence genes
- **Multi-locus Typing**: Performs MLST for molecular epidemiology

## Pitfalls

- **Assembly Quality**: Poor quality assemblies lead to missing or incorrect predictions
- **Database Updates**: Resistance gene databases require regular updates
- **Species Specificity**: Optimized for Klebsiella, may not work well for other species
- **Coverage Requirements**: Low coverage assemblies may miss genes
- **Gene Nomenclature**: Gene names may vary between databases
- **Interpretation Challenges**: Presence of resistance gene doesn't always mean phenotypic resistance

## Examples

### Screen genome assembly
**Args:** `kleborate -i assembly.fasta -o results.txt`
**Explanation:** Screens a genome assembly for species, MLST, and resistance markers.

### Full screening with all modules
**Args:** `kleborate -i assembly.fasta -o full_results.txt --all`
**Explanation:** Runs complete screening including species, MLST, resistance, and virulence.

### Process multiple assemblies
**Args:** `kleborate -d assemblies/ -o results.csv --batch`
**Explanation:** Processes multiple genome assemblies in batch mode.

### Specify output format
**Args:** `kleborate -i assembly.fasta -o results.tsv --tsv`
**Explanation:** Outputs results in tab-separated format.

### Filter by species
**Args:** `kleborate -i assembly.fasta -o results.txt --species Kp`
**Explanation:** Specifically screens for Klebsiella pneumoniae.

### Verbose output
**Args:** `kleborate -i assembly.fasta -o results.txt -v`
**Explanation:** Runs with verbose output for debugging.