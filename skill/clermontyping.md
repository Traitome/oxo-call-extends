---
name: clermontyping
category: utility
description: Determine the Clermont E. coli phylotype using in silico quadriplex PCR
tags: [clermontyping, ecoli, phylotyping, bacteria, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/happykhan/ClermonTyping"
---

## Concepts

- **Tool Overview**: ClermonTyping determines the Clermont phylotype of E. coli strains by performing in silico quadriplex PCR analysis.
- **Core Function**: Identifies E. coli phylotypes (A, B1, B2, D, E, F) based on genetic markers.
- **Algorithm**: Uses in silico PCR to detect specific genetic markers for phylotype classification.
- **Input**: E. coli genome sequence (FASTA).
- **Output**: Phylotype classification with confidence scores.
- **Application**: E. coli strain characterization, epidemiology, and evolutionary studies.
- **Installation**: Install via bioconda: `conda install -c bioconda clermontyping`

## Pitfalls

- **E. coli Specific**: Designed specifically for E. coli; not suitable for other species.
- **Genome Quality**: Requires complete or draft genome sequence.
- **Marker Detection**: May fail if genetic markers are missing or mutated.
- **Database Updates**: Phylotype database may need updates for new strains.
- **False Negatives**: May miss phylotype if markers are not detected.

## Examples

### Determine phylotype
**Args:** `clermontyping -i ecoli_genome.fasta -o phylotype.txt`
**Explanation:** Determines Clermont phylotype of E. coli genome.

### With verbose output
**Args:** `clermontyping -i ecoli_genome.fasta -v -o phylotype.txt`
**Explanation:** Provides detailed output including marker detection status.

### Batch processing
**Args:** `clermontyping -d genomes/ -o results/`
**Explanation:** Processes multiple genomes in batch mode.

### Display help
**Args:** `clermontyping --help`
**Explanation:** Shows all available options and usage information.