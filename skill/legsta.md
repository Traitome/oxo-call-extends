---
name: legsta
category: typing
description: In silico Legionella pneumophila Sequence Based Typing
tags: [legsta, typing, Legionella, bacteria, sequence-typing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/tseemann/legsta"
---

## Concepts

- **Sequence Typing**: Performs in silico sequence-based typing
- **Legionella**: Specifically designed for Legionella pneumophila
- **MLST**: Multi-locus sequence typing support
- **Strain Identification**: Identifies bacterial strains from sequence data
- **Fast Analysis**: Rapid typing from genome sequences
- **Database Comparison**: Compares against known typing databases

## Pitfalls

- **Genome Completeness**: Requires complete or near-complete genomes
- **Sequence Quality**: Poor quality sequences affect typing accuracy
- **Database Updates**: Typing database needs regular updates
- **New Strains**: Novel strains may not be in database
- **Assembly Quality**: Poor assemblies affect typing results
- **MLST Scheme**: Depends on correct MLST scheme selection

## Examples

### Type genome
**Args:** `legsta genome.fasta`
**Explanation:** Performs sequence-based typing on genome.

### Output JSON
**Args:** `legsta genome.fasta --json`
**Explanation:** Outputs typing results in JSON format.

### Specify database
**Args:** `legsta genome.fasta --db custom_db.fasta`
**Explanation:** Uses custom typing database.

### Batch processing
**Args:** `legsta *.fasta`
**Explanation:** Types multiple genome files.

### Verbose output
**Args:** `legsta genome.fasta --verbose`
**Explanation:** Shows detailed typing information.

### Version check
**Args:** `legsta --version`
**Explanation:** Shows current version.