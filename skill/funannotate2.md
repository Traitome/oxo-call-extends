---
name: funannotate2
category: annotation
description: "Funannotate2: eukaryotic genome annotation pipeline."
tags: [funannotate2, genome annotation, eukaryotic, gene prediction]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/funannotate2"
---
## Concepts
- **Eukaryotic Annotation**: Comprehensive genome annotation for eukaryotic organisms.
- **Gene Prediction**: Predicts protein-coding genes using multiple ab initio predictors.
- **Functional Annotation**: Assigns functional information to predicted genes.
- **Repeat Masking**: Identifies and masks repetitive elements in genomes.
- **Evidence Integration**: Combines multiple evidence types for accurate annotation.

## Pitfalls
- **Computational Requirements**: High computational requirements for large genomes.
- **Memory Usage**: Requires significant memory for annotation processes.
- **Database Dependencies**: Needs multiple annotation databases installed.
- **Time Consuming**: Full annotation can take hours to days.
- **Parameter Tuning**: Requires careful parameter adjustment for optimal results.

## Examples
### Run full annotation pipeline
**Args:** `funannotate2 annotate -i genome.fasta -o annotation/`
**Explanation:** Runs complete genome annotation pipeline.

### Predict genes
**Args:** `funannotate2 predict -i genome.fasta -o predictions.gff`
**Explanation:** Predicts genes using ab initio predictors.

### Functional annotation
**Args:** `funannotate2 functional -i predictions.gff -o functional.txt`
**Explanation:** Adds functional annotations to predicted genes.

### Repeat masking
**Args:** `funannotate2 mask -i genome.fasta -o masked.fasta`
**Explanation:** Masks repetitive elements in genome.

### Update annotations
**Args:** `funannotate2 update -i annotation/ -o updated/`
**Explanation:** Updates existing annotations with new evidence.