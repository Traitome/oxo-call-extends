---
name: mitofinder
category: assembly
description: Mitofinder is a pipeline to assemble mitochondrial genomes and annotate mitochondrial genes from trimmed read sequencing data.
tags: [mitofinder, assembly, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/RemiAllio/MitoFinder"
---

## Concepts

- **Tool Overview**: MitoFinder v1.4.1 assembles and annotates mitochondrial genomes.
- **Core Function**: Pipeline for mitochondrial genome assembly and annotation.
- **Assembly Pipeline**: Integrates assembly and annotation steps.
- **Gene Annotation**: Automatically annotates mitochondrial genes.
- **Input/Output**: Accepts trimmed reads; outputs assembled and annotated mtDNA.
- **Mitochondrial Genomics**: Supports complete mitochondrial analysis workflows.

## Pitfalls

- **Mitochondrial Specific**: Designed for mitochondrial analysis.
- **Computational Resources**: Pipeline may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Results depend on input data quality.
- **Reference Databases**: Requires appropriate annotation databases.

## Examples

### Run MitoFinder pipeline
**Args:** `mitofinder -j config.json -o results/`
**Explanation:** Runs complete mitochondrial assembly and annotation.

### With reference
**Args:** `mitofinder -j config.json -r ref_mito.fasta -o results/`
**Explanation:** Uses reference mitochondrial genome.

### Annotation only
**Args:** `mitofinder -j config.json -a -o results/`
**Explanation:** Performs annotation only.

### Batch processing
**Args:** `mitofinder -j config/ -o results/`
**Explanation:** Processes multiple configuration files.

### Generate report
**Args:** `mitofinder -j config.json -o results/ -r report.html`
**Explanation:** Generates HTML analysis report.