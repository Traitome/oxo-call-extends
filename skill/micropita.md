---
name: micropita
category: alignment
description: microPITA is a computational tool enabling sample selection in two-stage (tiered) studies.
tags: [micropita, alignment, statistics]
author: oxo-call-community
source_url: "http://huttenhower.sph.harvard.edu/micropita"
---

## Concepts

- **Tool Overview**: microPITA v1.1.0 enables sample selection in two-stage studies.
- **Core Function**: Optimizes sample selection for tiered study designs.
- **Two-stage Studies**: Supports two-stage (tiered) experimental designs.
- **Statistical Power**: Maximizes statistical power through optimal sampling.
- **Input/Output**: Accepts study data; outputs sample selection recommendations.
- **Experimental Design**: Aids in designing efficient experiments.

## Pitfalls

- **Study Design**: Specific to two-stage study designs.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Recommendations depend on input data quality.
- **Statistical Assumptions**: Based on specific statistical assumptions.

## Examples

### Select samples for study
**Args:** `micropita -i data.txt -o selection.txt`
**Explanation:** Selects optimal samples for two-stage study.

### With power analysis
**Args:** `micropita -i data.txt -o selection.txt -p`
**Explanation:** Includes power analysis in selection.

### Custom parameters
**Args:** `micropita -i data.txt -o selection.txt -a 0.05`
**Explanation:** Uses custom significance level.

### Batch processing
**Args:** `micropita -i data/ -o selections/`
**Explanation:** Processes multiple datasets in batch mode.

### Generate report
**Args:** `micropita -i data.txt -o selection.txt -r report.html`
**Explanation:** Generates study design report.