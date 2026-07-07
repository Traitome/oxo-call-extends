---
name: hicup
category: bioinformatics
description: HiCUP maps and performs quality control on Hi-C sequencing data.
tags: [hicup, Hi-C, alignment, bioinformatics]
author: oxo-call-community
source_url: "http://www.bioinformatics.babraham.ac.uk/projects/hicup/"
---

## Concepts

- **Hi-C Mapping**: HiCUP maps Hi-C sequencing reads.

- **Quality Control**: Performs quality control on Hi-C data.

- **Read Processing**: Processes Hi-C sequencing reads.

- **Duplicate Removal**: Removes duplicate reads.

- **Fragment Filtering**: Filters valid Hi-C fragments.

- **Contact Mapping**: Maps chromatin contacts.

## Pitfalls

- **Data Quality**: Results depend on sequencing data quality.

- **Reference Genome**: Requires appropriate reference genome.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Run HiCUP
**Args:** `hicup --input reads.fastq --output results/ --genome hg38`
**Explanation:** Runs Hi-C mapping and QC.

### With paired-end reads
**Args:** `hicup --input1 reads_1.fastq --input2 reads_2.fastq --output results/`
**Explanation:** Processes paired-end Hi-C data.

### Batch processing
**Args:** `for f in *.fastq; do hicup --input $f --output ${f%.fastq}_results/; done`
**Explanation:** Processes multiple Hi-C datasets.

### Generate report
**Args:** `hicup --input reads.fastq --output results/ --report`
**Explanation:** Generates comprehensive QC report.

### Help command
**Args:** `hicup --help`
**Explanation:** Shows available options and usage information.