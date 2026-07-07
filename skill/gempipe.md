---
name: gempipe
category: metabolic-modeling
description: GEM-PIPE is a tool for the reconstruction of strain-specific genome-scale metabolic models.
tags: [gempipe, metabolic-modeling, genome-scale, constraint-based-modeling]
author: oxo-call-community
source_url: "https://gempipe.readthedocs.io/"
---

## Concepts
- **Metabolic Modeling**: Reconstructs genome-scale metabolic models.
- **Strain-specific Models**: Builds models specific to individual strains.
- **Constraint-based Analysis**: Uses constraint-based approaches for metabolic analysis.
- **Genome Annotation**: Integrates genome annotation data.
- **Model Validation**: Validates metabolic models against experimental data.

## Pitfalls
- **Annotation Quality**: Depends on high-quality genome annotations.
- **Computational Resources**: Metabolic models require significant computational resources.
- **Gap Filling**: May require manual curation for gap filling.
- **Parameter Sensitivity**: Model predictions depend on parameter settings.
- **Validation Data**: Requires experimental data for model validation.

## Examples
### Build metabolic model
**Args:** `gempipe build -i genome.fasta -a annotations.gff3 -o model.xml`
**Explanation:** Builds a genome-scale metabolic model from genome sequence and annotations.

### Refine model
**Args:** `gempipe refine -i model.xml -g growth_data.csv -o refined_model.xml`
**Explanation:** Refines metabolic model using growth experimental data.

### Simulate growth
**Args:** `gempipe simulate -i model.xml -o growth_results.txt`
**Explanation:** Simulates microbial growth under different conditions.

### Gap filling
**Args:** `gempipe gapfill -i model.xml -m medium.txt -o filled_model.xml`
**Explanation:** Fills gaps in metabolic network using medium composition.

### Export model
**Args:** `gempipe export -i model.xml -f sbml -o model.sbml`
**Explanation:** Exports metabolic model to SBML format.