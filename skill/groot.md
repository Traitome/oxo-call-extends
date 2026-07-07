---
name: groot
category: bioinformatics
description: Groot is a tool for resistome profiling of metagenomic samples, identifying antibiotic resistance genes and their abundances.
tags: [groot, resistome, metagenomics, bioinformatics]
author: oxo-call-community
source_url: "https://groot-documentation.readthedocs.io"
---

## Concepts

- **Resistome Profiling**: Groot identifies and quantifies antibiotic resistance genes in metagenomic data.

- **Database Search**: Searches against comprehensive resistance gene databases.

- **Abundance Estimation**: Estimates relative abundances of resistance genes.

- **Classification**: Classifies resistance genes by type and mechanism.

- **Annotation**: Provides functional annotations for detected resistance genes.

- **Visualization**: Generates visualizations of resistome profiles.

## Pitfalls

- **Database Coverage**: Results depend on database comprehensiveness.

- **Read Quality**: Low-quality reads may produce false positives.

- **Gene Variants**: Novel resistance gene variants may be missed.

- **Abundance Bias**: Relative abundances may not reflect absolute concentrations.

- **Parameter Tuning**: Adjust parameters based on sequencing depth and read quality.

## Examples

### Build database index
**Args:** `groot index -d database.fasta -o index/`
**Explanation:** Builds an index for the resistance gene database.

### Profile resistome
**Args:** `groot profile -i reads.fastq -d index/ -o profile.txt`
**Explanation:** Profiles resistome from metagenomic reads.

### Annotate results
**Args:** `groot annotate -i profile.txt -o annotated.txt`
**Explanation:** Adds functional annotations to resistance gene profiles.

### Compare profiles
**Args:** `groot compare -i sample1.txt sample2.txt -o comparison.txt`
**Explanation:** Compares resistome profiles between samples.

### Generate visualization
**Args:** `groot plot -i profile.txt -o plot.png`
**Explanation:** Creates a visualization of the resistome profile.

### Batch processing
**Args:** `groot batch -d samples/ -o results/`
**Explanation:** Processes multiple metagenomic samples.

### Filter results
**Args:** `groot filter -i profile.txt -t 0.01 -o filtered.txt`
**Explanation:** Filters out low-abundance resistance genes.