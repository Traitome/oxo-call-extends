---
name: lissero
category: typing
description: LisSerO - In silico serotyping of Listeria monocytogenes
tags: [lissero, typing, Listeria, serotyping, bacteria, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/lissero"
---

## Concepts

- **Serotyping**: In silico serotyping of bacterial strains
- **Listeria monocytogenes**: Analysis of Listeria monocytogenes
- **Genomic Analysis**: Genomic-based serotype prediction
- **MLST Typing**: Multi-locus sequence typing
- **Pathogen Identification**: Identification of pathogenic strains
- **Food Safety**: Food safety and pathogen monitoring

## Pitfalls

- **Genome Quality**: Poor quality assemblies affect typing
- **Reference Database**: Requires up-to-date reference database
- **Strain Variability**: Highly variable strains may cause issues
- **Parameter Tuning**: Requires careful parameter optimization
- **Database Updates**: Database must be regularly updated
- **Interpretation**: Results require careful interpretation

## Examples

### Serotype Listeria
**Args:** `lissero -i genome.fasta -o serotype.txt`
**Explanation:** Determines serotype of Listeria monocytogenes.

### Multi-fasta input
**Args:** `lissero -i genomes/ -o serotypes.txt`
**Explanation:** Processes multiple genome files.

### Verbose output
**Args:** `lissero -i genome.fasta -o serotype.txt -v`
**Explanation:** Provides detailed output.

### Database update
**Args:** `lissero --update-db`
**Explanation:** Updates reference database.

### MLST typing
**Args:** `lissero -i genome.fasta -o mlst.txt --mlst`
**Explanation:** Performs MLST typing.

### Quality filtering
**Args:** `lissero -i genome.fasta -o serotype.txt -q 30`
**Explanation:** Filters by quality score.