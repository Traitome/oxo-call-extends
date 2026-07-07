---
name: fusion-filter
category: utility
description: FusionFilter provides a common fusion-finding, filtering, and annotation framework for the Trinity Cancer Transcriptome Analysis Toolkit (CTAT).
tags: [fusion-filter, gene fusion, CTAT, filtering]
author: oxo-call-community
source_url: "https://github.com/FusionFilter/FusionFilter"
---

## Concepts
- **Fusion Filtering**: Filters and validates fusion gene predictions.
- **Annotation Framework**: Provides annotation for fusion features.
- **False Positive Removal**: Removes likely false-positive fusion calls.
- **CTAT Integration**: Part of Trinity Cancer Transcriptome Analysis Toolkit.
- **Evidence Scoring**: Scores fusion evidence for confidence assessment.

## Pitfalls
- **CTAT Dependency**: Designed for use with CTAT pipeline.
- **Input Format**: Requires specific input format from fusion tools.
- **Database Requirements**: Needs annotation databases.
- **Complex Configuration**: Multiple configuration options.
- **Output Interpretation**: Results require careful interpretation.

## Examples
### Run fusion filtering
**Args:** `fusion-filter --input fusions.txt --output filtered.txt`
**Explanation:** Filters fusion calls and outputs high-confidence results.

### With annotation
**Args:** `fusion-filter --input fusions.txt --annotate --output annotated.txt`
**Explanation:** Adds functional annotations to fusion calls.

### Strict filtering
**Args:** `fusion-filter --input fusions.txt --strict --output strict.txt`
**Explanation:** Applies strict filtering criteria.

### Generate report
**Args:** `fusion-filter --input fusions.txt --report --output report.html`
**Explanation:** Generates HTML report of fusion analysis.

### Batch processing
**Args:** `fusion-filter --batch samples.txt --output results/`
**Explanation:** Processes multiple samples in batch.