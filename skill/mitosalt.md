---
name: mitosalt
category: utility
description: MitoSAlt is a pipeline to identify large deletions and duplications in human and mouse mitochondrial genomes from next generation whole genome/exome sequencing data. The pipeline is capable of analyzing any circular genome in principle, as long as a proper configuration file is provided.
tags: [mitosalt, utility, sequence, mitochondrial]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/mitosalt/"
---

## Concepts

- **Tool Overview**: MitoSAlt v1.1.1 identifies large deletions and duplications in mitochondrial genomes.
- **Core Function**: Detects structural variants in mtDNA from WGS/exome data.
- **Structural Variation**: Identifies deletions and duplications.
- **Circular Genome**: Designed for circular genome analysis.
- **Input/Output**: Accepts sequencing reads; outputs variant calls.
- **Human/Mouse**: Optimized for human and mouse mitochondrial genomes.

## Pitfalls

- **Mitochondrial Specific**: Designed for mtDNA analysis.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on input data quality.
- **Reference Dependence**: Requires appropriate reference sequences.

## Examples

### Run paired-end analysis
**Args:** `mitosalt.pl config.txt reads_1.fastq reads_2.fastq study_name`
**Explanation:** Runs pipeline with paired-end reads.

### Run single-end analysis
**Args:** `mitosalt_se.pl config.txt reads.fastq study_name`
**Explanation:** Runs pipeline with single-end reads.

### Download reference data
**Args:** `download-mitosalt-db.sh -h -m`
**Explanation:** Downloads human and mouse reference genomes.

### Custom reference
**Args:** `export MITOSALT_DATA=/path/to/genomedata && mitosalt.pl config.txt reads_1.fastq reads_2.fastq study_name`
**Explanation:** Uses custom reference data directory.

### Generate report
**Args:** `mitosalt.pl config.txt reads_1.fastq reads_2.fastq study_name -r report.html`
**Explanation:** Generates HTML analysis report.