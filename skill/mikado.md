---
name: mikado
category: alignment
description: A Python3 annotation program to select the best gene model in each locus.
tags: [mikado, alignment, annotation]
author: oxo-call-community
source_url: "https://github.com/EI-CoreBioinformatics/mikado"
---

## Concepts

- **Tool Overview**: Mikado v2.3.4 selects the best gene models from RNA-Seq annotations.
- **Core Function**: Identifies and selects optimal gene models in each locus.
- **Gene Model Selection**: Selects best transcript models from multiple annotations.
- **Superlocus Analysis**: Groups overlapping features into superloci.
- **Input/Output**: Accepts GTF/GFF3 annotations; outputs refined gene models.
- **Alternative Splicing**: Identifies alternative splicing isoforms.

## Pitfalls

- **Computational Resources**: Processing large annotations may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal selection.
- **Data Quality**: Selection accuracy depends on input annotation quality.
- **Configuration Complexity**: Requires careful configuration for optimal results.
- **Format Requirements**: Requires GTF/GFF3 format input.

## Examples

### Run Mikado pipeline
**Args:** `mikado prepare --json config.json`
**Explanation:** Prepares annotations for analysis.

### Pick best gene models
**Args:** `mikado pick --json config.json`
**Explanation:** Selects optimal gene models.

### Validate results
**Args:** `mikado validate --json config.json`
**Explanation:** Validates selected gene models.

### Export results
**Args:** `mikado export --json config.json -o output.gtf`
**Explanation:** Exports results to GTF format.

### Batch processing
**Args:** `mikado batch -i gtf/ -o results/`
**Explanation:** Processes multiple annotation files.