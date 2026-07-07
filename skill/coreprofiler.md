---
name: coreprofiler
category: utility
description: Robust and integrable cgMLST software for bacterial typing
tags: [coreprofiler, cgMLST, bacterial-typing, mlst, genomics]
author: oxo-call-community
source_url: "https://gitlab.com/ifb-elixirfr/abromics/coreprofiler"
---

## Concepts

- **Tool Overview**: CoreProfiler is a robust and integrable cgMLST (core genome Multi-Locus Sequence Typing) software for bacterial strain typing and identification.
- **Core Function**: Performs core genome MLST analysis to determine sequence types and phylogenetic relationships.
- **Algorithm**: Identifies core genes across isolates and compares allelic profiles for typing.
- **Input**: Bacterial genome assemblies (FASTA), reference gene databases.
- **Output**: Sequence types, allele profiles, and phylogenetic distance matrices.
- **Application**: Bacterial identification, outbreak investigation, epidemiological studies.
- **Installation**: Install via bioconda: `conda install -c bioconda coreprofiler`

## Pitfalls

- **Reference Database**: Requires up-to-date MLST databases for accurate typing.
- **Genome Quality**: Contaminated or incomplete assemblies may affect results.
- **Allele Calling**: Ambiguous bases can lead to uncertain allele assignments.
- **Database Compatibility**: Different MLST schemes may have incompatible formats.
- **Computational Resources**: Large datasets may require significant memory.

## Examples

### Run cgMLST analysis
**Args:** `coreprofiler -i genomes/ -d mlst_database/ -o results/`
**Explanation:** Performs cgMLST analysis on genome assemblies using MLST database.

### With quality filtering
**Args:** `coreprofiler -i genomes/ -d mlst_database/ -q 0.9 -o results/`
**Explanation:** Applies 90% quality threshold for allele calling.

### Generate phylogenetic tree
**Args:** `coreprofiler -i genomes/ -d mlst_database/ --tree -o results/`
**Explanation:** Generates phylogenetic tree from cgMLST profiles.

### Display help
**Args:** `coreprofiler --help`
**Explanation:** Shows all available options and usage information.