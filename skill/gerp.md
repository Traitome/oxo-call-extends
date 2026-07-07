---
name: gerp
category: comparative-genomics
description: GERP - Identifies constrained elements in multiple alignments by quantifying substitution deficits.
tags: [gerp, comparative-genomics, constraint-analysis, conservation]
author: oxo-call-community
source_url: "http://mendel.stanford.edu/SidowLab/downloads/gerp/index.html"
---

## Concepts
- **Constraint Analysis**: Identifies evolutionarily constrained genomic regions.
- **Multiple Alignment**: Analyzes multiple sequence alignments.
- **Substitution Rate**: Quantifies substitution deficits.
- **Phylogenetic Analysis**: Uses phylogenetic information.
- **Conservation Scoring**: Scores evolutionary conservation.

## Pitfalls
- **Alignment Quality**: Requires high-quality multiple alignments.
- **Phylogenetic Tree**: Requires appropriate phylogenetic tree.
- **Computational Resources**: Large datasets require resources.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Interpretation**: Requires careful interpretation of scores.

## Examples
### Run GERP on alignment
**Args:** `gerp -f alignment.mfa -t tree.nwk -o scores.txt`
**Explanation:** Runs GERP on multiple alignment with tree.

### With options
**Args:** `gerp -f alignment.mfa -t tree.nwk -w 100 -o scores.txt`
**Explanation:** Uses window size of 100 for scoring.

### Batch processing
**Args:** `gerp -l alignments.txt -t tree.nwk -o ./results/`
**Explanation:** Processes multiple alignments.

### Generate constrained elements
**Args:** `gerp -f alignment.mfa -t tree.nwk -c -o elements.bed`
**Explanation:** Outputs constrained elements in BED format.

### Generate report
**Args:** `gerp -f alignment.mfa -t tree.nwk -r -o report.html`
**Explanation:** Generates analysis report.