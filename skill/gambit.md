---
name: gambit
category: metagenomics
description: Tool for rapid taxonomic identification of microbial pathogens.
tags: [gambit, taxonomic identification, pathogen, metagenomics]
author: oxo-call-community
source_url: "https://github.com/jlumpe/gambit"
---

## Concepts
- **Genomic Distance**: Uses efficient genomic distance metric.
- **Large Database**: Curated database of ~50,000 reference genomes.
- **Fast Identification**: Identifies genomes within seconds.
- **NCBI RefSeq**: Based on NCBI RefSeq reference genomes.
- **Bacterial Pathogens**: Optimized for bacterial pathogen identification.

## Pitfalls
- **Database Size**: Large database requires significant storage.
- **Novel Organisms**: May miss novel or distantly related organisms.
- **Computational Resources**: Requires adequate computational resources.
- **Database Updates**: Needs regular database updates.
- **Query Complexity**: Complex queries may take longer.

## Examples
### Identify genome
**Args:** `gambit query -i genome.fasta -o results.csv`
**Explanation:** Identifies genome from query sequence.

### With taxonomy filter
**Args:** `gambit query -i genome.fasta --taxon genus -o results.csv`
**Explanation:** Filters results by genus.

### Create database
**Args:** `gambit create-database -i genomes/ -o gambit.db`
**Explanation:** Creates GAMBIT database from genomes.

### Check database
**Args:** `gambit check-database -d gambit.db`
**Explanation:** Checks database integrity.

### Export results
**Args:** `gambit export -i results.csv -f json -o results.json`
**Explanation:** Exports results to JSON format.