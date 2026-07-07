---
name: lorikeet
category: typing
description: Lorikeet - Digital spoligotyping of MTB strains
tags: [lorikeet, typing, MTB, spoligotyping, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/AbeelLab/lorikeet"
---

## Concepts

- **Spoligotyping**: Spacer oligonucleotide typing of MTB
- **MTB Analysis**: Analysis of Mycobacterium tuberculosis
- **Digital Typing**: Computational typing of strains
- **Strain Identification**: Identification of bacterial strains
- **Genotyping**: Genetic characterization of strains
- **Public Health**: Public health surveillance applications

## Pitfalls

- **Read Quality**: Poor quality reads affect typing
- **Reference Database**: Quality of reference database is critical
- **Strain Diversity**: Highly diverse strains may affect accuracy
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive identifications

## Examples

### Run spoligotyping
**Args:** `lorikeet --input reads.fastq --output spoligotype.txt`
**Explanation:** Performs digital spoligotyping.

### Reference database
**Args:** `lorikeet --input reads.fastq --output spoligotype.txt --ref reference.fasta`
**Explanation:** Uses custom reference database.

### Threads
**Args:** `lorikeet --input reads.fastq --output spoligotype.txt --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `lorikeet --input reads.fastq --output spoligotype.txt --min-cov 10`
**Explanation:** Sets minimum coverage threshold.

### Output format
**Args:** `lorikeet --input reads.fastq --output spoligotype.json --format json`
**Explanation:** Outputs results in JSON format.

### Verbose output
**Args:** `lorikeet --input reads.fastq --output spoligotype.txt --verbose`
**Explanation:** Provides detailed output.