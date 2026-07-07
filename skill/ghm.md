---
name: ghm
category: statistical-analysis
description: ghm - MOD-score analysis for genetic linkage studies.
tags: [ghm, statistical-analysis, linkage, genetics]
author: oxo-call-community
source_url: "https://www.helmholtz-muenchen.de/en/ige/service/software-download/genehunter-modscore/index.html"
---

## Concepts
- **MOD-Score Analysis**: Maximizes parametric LOD scores.
- **Linkage Analysis**: Performs genetic linkage analysis.
- **Trait Modeling**: Models complex traits.
- **Parameter Optimization**: Optimizes trait model parameters.
- **Statistical Testing**: Provides statistical significance.

## Pitfalls
- **Model Complexity**: Complex trait models.
- **Computational Intensity**: Requires significant computation.
- **Data Quality**: Requires high-quality genotype data.
- **Parameter Selection**: Requires careful parameter selection.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Run MOD-score analysis
**Args:** `ghm -i data.ped -o results.txt`
**Explanation:** Runs MOD-score analysis.

### With trait model
**Args:** `ghm -i data.ped -t quantitative -o results.txt`
**Explanation:** Uses quantitative trait model.

### Specify parameters
**Args:** `ghm -i data.ped -p model.txt -o results.txt`
**Explanation:** Specifies trait model parameters.

### Generate report
**Args:** `ghm -i data.ped -r -o report.html`
**Explanation:** Generates analysis report.

### Batch processing
**Args:** `ghm -l samples.txt -o ./results/`
**Explanation:** Processes multiple datasets.