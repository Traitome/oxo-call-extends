---
name: kinex
category: proteomics
description: Kinex infers causal kinases from phosphoproteomics data.
tags: [kinex, proteomics, kinase, phosphoproteomics, signaling]
author: oxo-call-community
source_url: "https://kinex.readthedocs.io/en/latest/"
---

## Concepts

- **Kinase Inference**: Identifies upstream kinases responsible for observed phosphorylation patterns
- **Phosphoproteomics Data**: Analyzes large-scale phosphorylation datasets from mass spectrometry
- **Signaling Pathways**: Maps phosphorylation events to known signaling pathways
- **Statistical Modeling**: Uses statistical methods to infer kinase-substrate relationships
- **Kinase-Substrate Relationships**: Leverages curated databases of known kinase-substrate interactions
- **Bioinformatics Analysis**: Integrates with other proteomics tools for comprehensive analysis

## Pitfalls

- **Data Quality**: Poor quality phosphoproteomics data leads to unreliable inference
- **Kinase Database Completeness**: Limited by the coverage of kinase-substrate databases
- **Multiple Testing Correction**: Requires proper adjustment for multiple hypothesis testing
- **Sample Size**: Small datasets may not provide sufficient statistical power
- **Phosphosite Localization**: Ambiguous phosphorylation site localization affects accuracy
- **Experimental Design**: Study design impacts the ability to detect meaningful kinase activity

## Examples

### Infer causal kinases
**Args:** `kinex -i phospho_data.csv -o kinase_inference.csv`
**Explanation:** Infers causal kinases from phosphoproteomics data using default parameters.

### Perform pathway enrichment
**Args:** `kinex -i data.csv -o results.csv --pathway-enrichment`
**Explanation:** Identifies enriched signaling pathways from kinase activity predictions.

### Calculate kinase activity scores
**Args:** `kinex -i phospho.csv -o activity_scores.csv --activity-score`
**Explanation:** Computes kinase activity scores for each kinase in the dataset.

### Compare conditions
**Args:** `kinex -i control.csv -i treated.csv -o comparison.csv --compare`
**Explanation:** Compares kinase activity between two experimental conditions.

### Validate kinase-substrate pairs
**Args:** `kinex -i data.csv -o validated.csv --validate-pairs`
**Explanation:** Validates predicted kinase-substrate relationships against known interactions.

### Generate kinase network
**Args:** `kinex -i phospho_data.csv -o network.graphml --network`
**Explanation:** Constructs a kinase-substrate interaction network in GraphML format.