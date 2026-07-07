---
name: seroba
category: typing
description: seroba - k-mer based serotype identification from NGS reads
tags: ["seroba", "typing", "k-mer", "serotyping"]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/seroba"
---

## Concepts

- **Tool Overview**: seroba (v1.0.2) is a k-mer based pipeline for serotype identification from Illumina NGS reads.
- **Core Function**: Identifies bacterial serotypes using k-mer matching against reference databases.
- **Algorithm**: Uses k-mer counting and matching for serotype prediction.
- **Input/Output**: Accepts FASTQ reads and produces serotype predictions.
- **Serotyping**: Focuses on bacterial serotype determination.
- **Applications**: Clinical microbiology, pathogen identification, and epidemiology.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Database Requirements**: Requires up-to-date reference database.
- **Input Quality**: Results depend on sequencing data quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Run serotyping
**Args:** `seroba runSerotyping -i reads.fastq -o results/ -d database/`
**Explanation:** `-i` input reads; `-o` output directory; `-d` database.

### Paired-end
**Args:** `seroba runSerotyping -1 reads_1.fastq -2 reads_2.fastq -o results/ -d database/`
**Explanation:** `-1/-2` paired-end reads.

### Build database
**Args:** `seroba createDB -f references.fasta -o database/`
**Explanation:** Creates custom database.

### Verbose logging
**Args:** `seroba -v runSerotyping -i reads.fastq -o results/ -d database/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seroba --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seroba --version`
**Explanation:** Shows current version.

### List databases
**Args:** `seroba listDB`
**Explanation:** Lists available databases.