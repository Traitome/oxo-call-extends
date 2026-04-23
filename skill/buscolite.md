---
name: buscolite
category: qc
description: BUSCO analysis for gene predictions
tags: [busco, qc, completeness, gene-prediction, annotation]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/buscolite"
---

## Concepts

- **Tool Overview**: buscolite performs BUSCO analysis specifically for gene predictions.
- **Core Function**: Assesses completeness of gene predictions using BUSCO orthologs.
- **Input**: Predicted gene sequences (protein or CDS).
- **Output**: BUSCO completeness scores and missing ortholog reports.
- **Application**: Quality assessment of gene annotation pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda buscolite`

## Pitfalls

- **Gene Mode**: Designed for protein mode analysis of gene predictions.
- **Lineage Selection**: Choose appropriate lineage dataset.
- **Partial Genes**: Fragmented BUSCOs may indicate incomplete predictions.

## Examples

### Assess gene prediction completeness
**Args:** `buscolite -i predicted_proteins.fa -l eukaryota_odb10 -o busco_results/`
**Explanation:** Assesses completeness of predicted protein set.

### Use specific lineage
**Args:** `buscolite -i proteins.fa -l insecta_odb10 -o insect_busco/`
**Explanation:** Uses insect-specific lineage for assessment.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
