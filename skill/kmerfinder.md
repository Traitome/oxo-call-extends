---
name: kmerfinder
category: metagenomics
description: Prediction of bacterial species using a fast K-mer algorithm
tags: [kmerfinder, metagenomics, bacteria, species-identification, k-mer]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/kmerfinder"
---

## Concepts

- **Bacterial Species Identification**: Identifies bacterial species from sequencing reads
- **K-mer Matching**: Uses k-mer based algorithm for rapid species matching
- **Reference Database**: Compares against curated bacterial reference genomes
- **Pathogen Detection**: Designed for pathogen identification in clinical samples
- **Fast Analysis**: Provides rapid results for time-sensitive applications
- **Multi-species Detection**: Can identify multiple species in mixed samples

## Pitfalls

- **Database Coverage**: Limited by reference database completeness
- **Read Quality**: Low-quality reads affect identification accuracy
- **Novel Species**: May not detect novel or poorly characterized species
- **Mixed Infections**: Difficult to resolve in complex multi-species samples
- **Strain-level Resolution**: Limited ability to distinguish strains
- **Genome Similarity**: Closely related species may cause ambiguity

## Examples

### Identify species from reads
**Args:** `kmerfinder.py -i reads.fastq -db /path/to/db -o output`
**Explanation:** Identifies bacterial species from sequencing reads.

### Paired-end reads
**Args:** `kmerfinder.py -i reads_1.fastq reads_2.fastq -db db -o results`
**Explanation:** Processes paired-end reads for species identification.

### Specify organism type
**Args:** `kmerfinder.py -i reads.fastq -db db -organism bacteria -o output`
**Explanation:** Specifically searches against bacterial database.

### Set minimum coverage
**Args:** `kmerfinder.py -i reads.fastq -db db -o output -min_cov 0.5`
**Explanation:** Requires minimum 50% coverage for species identification.

### Detailed output
**Args:** `kmerfinder.py -i reads.fastq -db db -o output -verbose`
**Explanation:** Provides detailed output with all matches.

### Batch processing
**Args:** `kmerfinder.py --batch -d samples/ -db db -o results/`
**Explanation:** Processes multiple samples in batch mode.