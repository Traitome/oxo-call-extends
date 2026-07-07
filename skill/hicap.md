---
name: hicap
category: bioinformatics
description: hicap performs in silico typing of the Haemophilus influenzae capsule locus.
tags: [hicap, bacterial-typing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/scwatts/hicap/blob/main/README.md"
---

## Concepts

- **Capsule Typing**: hicap types H. influenzae capsule loci.

- **In Silico Typing**: Performs computational serotyping.

- **H. influenzae**: Focused on Haemophilus influenzae.

- **Genomic Analysis**: Analyzes bacterial genome sequences.

- **Serotype Identification**: Identifies bacterial serotypes.

- **Pathogen Characterization**: Characterizes bacterial pathogens.

## Pitfalls

- **Assembly Quality**: Results depend on genome assembly quality.

- **Reference Database**: Requires up-to-date reference database.

- **Strain Variation**: May not cover all strains.

- **Partial Sequences**: Partial sequences may give incomplete results.

- **False Positives**: May produce false positive predictions.

## Examples

### Type H. influenzae capsule
**Args:** `hicap --input genome.fasta --output results/`
**Explanation:** Performs capsule typing on genome.

### With custom database
**Args:** `hicap --input genome.fasta --db custom_db/ --output results/`
**Explanation:** Uses custom reference database.

### Batch processing
**Args:** `for f in *.fasta; do hicap --input $f --output ${f%.fasta}_results/; done`
**Explanation:** Processes multiple genome files.

### Generate report
**Args:** `hicap --input genome.fasta --output results/ --report`
**Explanation:** Generates comprehensive typing report.

### Help command
**Args:** `hicap --help`
**Explanation:** Shows available options and usage information.