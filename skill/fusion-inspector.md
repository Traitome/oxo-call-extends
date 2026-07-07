---
name: fusion-inspector
category: expression
description: In silico Validation of Fusion Transcript Predictions.
tags: [fusion-inspector, gene fusion, validation, CTAT]
author: oxo-call-community
source_url: "https://github.com/FusionInspector/FusionInspector"
---

## Concepts
- **Fusion Validation**: Validates fusion transcript predictions in silico.
- **Evidence Recovery**: Recovers and re-scores evidence for fusion predictions.
- **CTAT Component**: Part of Trinity Cancer Transcriptome Analysis Toolkit.
- **Visualization**: Generates visualizations of fusion events.
- **Confidence Scoring**: Assigns confidence scores to fusion calls.

## Pitfalls
- **CTAT Integration**: Designed for use with CTAT pipeline.
- **Computational Requirements**: High computational requirements.
- **Memory Usage**: Requires significant memory for validation.
- **Time Consuming**: Validation can be time-consuming.
- **Interpretation**: Requires understanding of fusion biology.

## Examples
### Validate fusions
**Args:** `fusion-inspector --fusions fusions.txt --output results/`
**Explanation:** Validates fusion predictions and generates results.

### With RNA-seq data
**Args:** `fusion-inspector --fusions fusions.txt --reads reads.fastq --output results/`
**Explanation:** Uses RNA-seq data for validation.

### Generate visualization
**Args:** `fusion-inspector --fusions fusions.txt --viz --output viz/`
**Explanation:** Generates visualizations of fusion events.

### Detailed report
**Args:** `fusion-inspector --fusions fusions.txt --report --output report.html`
**Explanation:** Generates detailed HTML report.

### Batch validation
**Args:** `fusion-inspector --batch samples.txt --output results/`
**Explanation:** Validates fusions from multiple samples.