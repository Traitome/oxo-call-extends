---
name: gapseq
category: utility
description: Informed prediction and analysis of bacterial metabolic pathways and genome-scale networks.
tags: [gapseq, metabolism, metabolic pathways, bacteria]
author: oxo-call-community
source_url: "https://github.com/jotech/gapseq"
---

## Concepts
- **Metabolic Prediction**: Predicts metabolic pathways in bacteria.
- **Genome-scale Networks**: Builds genome-scale metabolic networks.
- **Pathway Analysis**: Analyzes metabolic pathway completeness.
- **Transport Prediction**: Predicts transport proteins.
- **Biomass Modeling**: Models biomass composition.

## Pitfalls
- **Genome Quality**: Results depend on genome annotation quality.
- **Database Coverage**: Limited by metabolic database coverage.
- **Gap Filling**: May require manual gap filling.
- **Complex Metabolism**: Complex metabolic networks may be incomplete.
- **Species Specificity**: Optimized for bacteria, not eukaryotes.

## Examples
### Find metabolic pathways
**Args:** `gapseq find -g genome.fasta -t 1 -o pathways/`
**Explanation:** Finds metabolic pathways in genome.

### Predict transport proteins
**Args:** `gapseq trans -g genome.fasta -o transport.txt`
**Explanation:** Predicts transport proteins.

### Build metabolic model
**Args:** `gapseq build -g genome.fasta -p pathways/ -o model.json`
**Explanation:** Builds genome-scale metabolic model.

### Draft model
**Args:** `gapseq draft -g genome.fasta -o draft_model.json`
**Explanation:** Creates draft metabolic model.

### Fill gaps
**Args:** `gapseq fill -m model.json -o filled_model.json`
**Explanation:** Fills gaps in metabolic model.