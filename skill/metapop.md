---
name: metapop
category: metagenomics
description: A pipeline for the macro- and micro-diversity analyses and visualization of metagenomic-derived populations
tags: [metapop, metagenomics, diversity]
author: oxo-call-community
source_url: "https://github.com/metaGmetapop/metapop"
---

## Concepts

- **Tool Overview**: MetaPop v1.0.2 is a pipeline for macro- and micro-diversity analyses and visualization of metagenomic-derived populations.
- **Core Function**: Analyzes microbial diversity at both macro (community-level) and micro (population-level) scales.
- **Diversity Analysis**: Provides comprehensive diversity metrics including alpha and beta diversity.
- **Population Structure**: Analyzes population structure within metagenomic samples.
- **Input/Output**: Accepts metagenomic sequencing data; outputs diversity metrics and visualizations.
- **Visualization**: Generates visual representations of diversity patterns and population structures.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Complete analysis can be time-consuming for complex datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input data quality.
- **Normalization**: Requires proper normalization of sequencing depth across samples.

## Examples

### Run diversity analysis
**Args:** `metapop -i reads.fastq -o results/`
**Explanation:** Performs comprehensive diversity analysis on metagenomic data.

### Macro-diversity analysis
**Args:** `metapop -i reads.fastq -o results/ --macro`
**Explanation:** Focuses on community-level diversity analysis.

### Micro-diversity analysis
**Args:** `metapop -i reads.fastq -o results/ --micro`
**Explanation:** Focuses on population-level diversity analysis.

### Generate visualization
**Args:** `metapop -i reads.fastq -o results/ -v`
**Explanation:** Generates visualizations of diversity patterns.

### Batch processing
**Args:** `metapop -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.