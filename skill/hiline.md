---
name: hiline
category: bioinformatics
description: HiLine is a Hi-C alignment and classification pipeline.
tags: [hiline, Hi-C, alignment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/HiLine"
---

## Concepts

- **Hi-C Alignment**: HiLine aligns Hi-C sequencing reads.

- **Read Classification**: Classifies Hi-C read pairs.

- **Quality Control**: Performs quality control on Hi-C data.

- **Duplicate Removal**: Removes duplicate reads.

- **Contact Mapping**: Maps chromatin contacts.

- **Fragment Filtering**: Filters valid Hi-C fragments.

## Pitfalls

- **Data Quality**: Results depend on sequencing data quality.

- **Reference Genome**: Requires appropriate reference genome.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Run HiLine
**Args:** `hiline --input reads.fastq --output results/ --genome hg38`
**Explanation:** Runs Hi-C alignment and classification.

### With paired-end reads
**Args:** `hiline --input1 reads_1.fastq --input2 reads_2.fastq --output results/`
**Explanation:** Processes paired-end Hi-C data.

### Batch processing
**Args:** `for f in *.fastq; do hiline --input $f --output ${f%.fastq}_results/; done`
**Explanation:** Processes multiple Hi-C datasets.

### Generate report
**Args:** `hiline --input reads.fastq --output results/ --report`
**Explanation:** Generates comprehensive QC report.

### Help command
**Args:** `hiline --help`
**Explanation:** Shows available options and usage information.