---
name: formulaic-contrasts
category: utility
description: Build contrasts for models defined with formulaic.
tags: [formulaic-contrasts, statistics, regression, contrasts]
author: oxo-call-community
source_url: "https://github.com/scverse/formulaic-contrasts"
---

## Concepts
- **Contrast Matrices**: Constructs contrast matrices for statistical models.
- **Formulaic Integration**: Works seamlessly with formulaic package.
- **Hypothesis Testing**: Enables custom hypothesis testing in regression models.
- **Multiple Comparisons**: Handles multiple comparison corrections.
- **Flexible Specification**: Supports various contrast types (treatment, sum, helmert).

## Pitfalls
- **Model Compatibility**: Requires formulaic model specification.
- **Statistical Assumptions**: Contrasts depend on underlying model assumptions.
- **Multiple Testing**: May require adjustment for multiple comparisons.
- **Interpretation**: Contrast results require careful interpretation.
- **Syntax Complexity**: Advanced contrasts may have complex syntax.

## Examples
### Basic contrast
**Args:** `formulaic-contrasts --model model.pkl --contrast "group1 - group2"`
**Explanation:** Computes contrast between group1 and group2.

### Multiple contrasts
**Args:** `formulaic-contrasts --model model.pkl --contrasts contrasts.txt`
**Explanation:** Computes multiple contrasts from a file.

### Sum contrasts
**Args:** `formulaic-contrasts --model model.pkl --type sum --contrast "group1 + group2 + group3"`
**Explanation:** Uses sum contrasts for the comparison.

### Treatment contrasts
**Args:** `formulaic-contrasts --model model.pkl --type treatment --reference group0`
**Explanation:** Uses treatment contrasts with group0 as reference.

### Post-hoc tests
**Args:** `formulaic-contrasts --model model.pkl --posthoc tukey`
**Explanation:** Performs Tukey post-hoc test.