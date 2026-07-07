---
name: gambitcore
category: assembly
description: Tool for rapid taxonomic identification of microbial pathogens.
tags: [gambitcore, taxonomic identification, pathogen, bacteria]
author: oxo-call-community
source_url: "https://github.com/gambit-suite/gambitcore"
---

## Concepts
- **Taxonomic Identification**: Rapidly identifies microbial species.
- **K-mer Profiling**: Uses k-mer profiles for identification.
- **Assembly Quality**: Assesses assembly completeness.
- **Core Genome**: Compares against species-specific core genomes.
- **Fast Analysis**: Identifies pathogens within seconds.

## Pitfalls
- **Database Coverage**: Limited by reference database coverage.
- **Novel Species**: May struggle with novel or uncommon species.
- **Mixed Samples**: Complex for mixed culture samples.
- **Assembly Quality**: Results depend on assembly quality.
- **Memory Usage**: Requires significant memory for large queries.

## Examples
### Identify from assembly
**Args:** `gambitcore -i assembly.fasta -o results.txt`
**Explanation:** Identifies species from genome assembly.

### With custom database
**Args:** `gambitcore -i assembly.fasta -d custom.db -o results.txt`
**Explanation:** Uses custom reference database.

### Get assembly metrics
**Args:** `gambitcore -i assembly.fasta --metrics -o metrics.txt`
**Explanation:** Gets assembly quality metrics.

### Specify taxa
**Args:** `gambitcore -i assembly.fasta -t genus -o results.txt`
**Explanation:** Limits search to genus level.

### Verbose output
**Args:** `gambitcore -i assembly.fasta -v -o results.txt`
**Explanation:** Outputs verbose identification details.