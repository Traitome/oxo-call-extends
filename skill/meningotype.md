---
name: meningotype
category: utility
description: In silico serotyping and finetyping of Neisseria meningitidis.
tags: [meningotype, serotyping, neisseria]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/meningotype"
---

## Concepts

- **Tool Overview**: MeningoType serotypes Neisseria meningitidis isolates.
- **Core Function**: In silico serotyping using genome data.
- **PorA Finetyping**: Determines PorA type.
- **FetA Finetyping**: Determines FetA type.
- **MLST Integration**: Supports MLST analysis.
- **Installation**: `conda install -c bioconda meningotype`

## Pitfalls

- **Species Specific**: Only for Neisseria meningitidis.
- **Data Quality**: Requires high-quality genome sequences.
- **Database Updates**: Needs updated reference databases.
- **Ambiguous Results**: May produce unclear typing results.
- **Contamination**: May misclassify contaminated samples.
- **Assembly Quality**: Depends on good assembly quality.

## Examples

### Serotype genome
**Args:** `meningotype -i genome.fasta -o results.txt`
**Explanation:** Determines serotype from genome.

### PorA finetyping
**Args:** `meningotype -i genome.fasta --porA -o pora.txt`
**Explanation:** Determines PorA type only.

### FetA finetyping
**Args:** `meningotype -i genome.fasta --fetA -o feta.txt`
**Explanation:** Determines FetA type only.

### Verbose mode
**Args:** `meningotype -i genome.fasta -v -o results.txt`
**Explanation:** Shows detailed typing process.

### Help documentation
**Args:** `meningotype --help`
**Explanation:** Displays available options.
