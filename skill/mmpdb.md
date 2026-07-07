---
name: mmpdb
category: utility
description: A package to identify matched molecular pairs and use them to predict property changes
tags: [mmpdb, utility, chemistry]
author: oxo-call-community
source_url: "https://github.com/rdkit/mmpdb"
---

## Concepts

- **Tool Overview**: mmpdb v3.1.4 identifies matched molecular pairs for property prediction.
- **Core Function**: Finds matched molecular pairs and predicts property changes.
- **Molecular Pairs**: Identifies structurally similar molecule pairs.
- **Property Prediction**: Predicts property changes based on molecular modifications.
- **Input/Output**: Accepts molecular structures; outputs matched pairs and predictions.
- **Cheminformatics**: Supports drug discovery and chemical analysis workflows.

## Pitfalls

- **Chemical Specific**: Designed for molecular structure analysis.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal matching.
- **Data Quality**: Results depend on input structure quality.
- **RDKit Dependence**: Requires RDKit chemistry toolkit.
- **Computational Resources**: Matching may require significant resources.

## Examples

### Create MMP database
**Args:** `mmpdb create -i molecules.sdf -o mmpdb.db`
**Explanation:** Creates MMP database from SDF file.

### Query database
**Args:** `mmpdb query -d mmpdb.db -q query.sdf -o results.txt`
**Explanation:** Queries MMP database for matched pairs.

### Predict properties
**Args:** `mmpdb predict -d mmpdb.db -i compounds.sdf -o predictions.txt`
**Explanation:** Predicts property changes.

### Generate report
**Args:** `mmpdb report -d mmpdb.db -o report.html`
**Explanation:** Generates HTML report.

### Batch processing
**Args:** `mmpdb batch -i sdf/ -d mmpdb.db -o results/`
**Explanation:** Processes multiple SDF files.