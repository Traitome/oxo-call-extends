---
name: guacamole-bio
category: bioinformatics
description: GuaCAMOLE performs GC-aware species abundance estimation from metagenomic sequencing data.
tags: [guacamole-bio, metagenomics, abundance-estimation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/CIBIV/GuaCAMOLE"
---

## Concepts

- **GC-Aware Abundance**: GuaCAMOLE accounts for GC content bias in metagenomic abundance estimation.

- **Species Identification**: Identifies and quantifies species in metagenomic samples.

- **Coverage Estimation**: Estimates sequencing coverage for each species.

- **Reference Database**: Uses reference genome databases for species identification.

- **Statistical Modeling**: Applies statistical models for accurate abundance estimation.

- **Error Correction**: Corrects for sequencing biases and errors.

## Pitfalls

- **Reference Database Quality**: Results depend on reference database completeness.

- **GC Bias**: GC content variations can affect estimation accuracy.

- **Low Coverage**: Low sequencing coverage reduces detection sensitivity.

- **Species Complexity**: Highly complex communities may be challenging to resolve.

- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Run abundance estimation
**Args:** `guacamole-bio -i reads.fastq -r reference/ -o abundance.txt`
**Explanation:** Estimates species abundance from metagenomic reads.

### Include GC correction
**Args:** `guacamole-bio -i reads.fastq -r reference/ -g -o abundance.txt`
**Explanation:** Enables GC-aware abundance estimation.

### Custom k-mer size
**Args:** `guacamole-bio -i reads.fastq -r reference/ -k 31 -o abundance.txt`
**Explanation:** Sets custom k-mer size for analysis.

### Batch processing
**Args:** `for f in *.fastq; do guacamole-bio -i $f -r reference/ -o ${f%.fastq}_abundance.txt; done`
**Explanation:** Processes multiple metagenomic samples.

### Generate report
**Args:** `guacamole-bio -i reads.fastq -r reference/ -r -o report.pdf`
**Explanation:** Generates PDF report of results.

### Filter by abundance
**Args:** `guacamole-bio -i reads.fastq -r reference/ -t 0.01 -o abundance.txt`
**Explanation:** Filters results by minimum abundance threshold.

### Help command
**Args:** `guacamole-bio --help`
**Explanation:** Shows available options and usage information.