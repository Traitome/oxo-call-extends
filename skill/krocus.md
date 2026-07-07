---
name: krocus
category: typing
description: Multi-locus sequence typing from uncorrected long reads
tags: [krocus, typing, MLST, long-reads, k-mer, bacterial-typing]
author: oxo-call-community
source_url: "https://github.com/andrewjpage/krocus"
---

## Concepts

- **MLST Prediction**: Predicts multi-locus sequence type from reads
- **Long Read Support**: Designed for uncorrected long reads (PacBio/ONT)
- **K-mer Based**: Uses k-mer matching for sequence typing
- **Direct Analysis**: Analyzes reads without assembly
- **Species Identification**: Identifies bacterial species from reads
- **Fast Results**: Provides results in minutes from raw reads

## Pitfalls

- **Database Coverage**: Limited by MLST database completeness
- **Read Quality**: Poor quality reads reduce typing accuracy
- **Novel Alleles**: Novel alleles may not be typed correctly
- **Species Specificity**: MLST schemes are species-specific
- **Mixed Infections**: Mixed samples complicate typing
- **Minimum Coverage**: Requires sufficient coverage for reliable typing

## Examples

### Predict MLST from reads
**Args:** `krocus -i reads.fastq -d mlst_db -o mlst_results.txt`
**Explanation:** Predicts MLST directly from uncorrected long reads.

### Specify species
**Args:** `krocus -i reads.fastq -s "Staphylococcus aureus" -d mlst_db -o results.txt`
**Explanation:** Runs analysis for specific species MLST scheme.

### Batch processing
**Args:** `krocus batch -i samples/ -d mlst_db -o results/`
**Explanation:** Processes multiple read files for MLST.

### Export alleles
**Args:** `krocus -i reads.fastq -d mlst_db --export-alleles -o alleles.fasta`
**Explanation:** Exports identified allele sequences.

### Confidence threshold
**Args:** `krocus -i reads.fastq -d mlst_db --min-conf 0.8 -o results.txt`
**Explanation:** Uses confidence threshold for typing.

### Species identification
**Args:** `krocus -i reads.fastq --identify-species -o species.txt`
**Explanation:** Identifies bacterial species from reads first.