---
name: gecco
category: annotation
description: Gene cluster prediction tool using Conditional Random Fields for identifying biosynthetic gene clusters.
tags: [gecco, gene-cluster, biosynthetic, CRF, bioinformatics]
author: oxo-call-community
source_url: "https://gecco.embl.de/"
---

## Concepts
- **Gene Cluster Prediction**: Identifies biosynthetic gene clusters (BGCs) in microbial genomes.
- **Conditional Random Fields**: Uses CRF-based machine learning for accurate prediction.
- **Biosynthetic Gene Clusters**: Detects clusters encoding secondary metabolites like antibiotics.
- **Domain Prediction**: Identifies functional domains within gene clusters.
- **AntiSMASH Integration**: Compatible with antiSMASH output for comprehensive analysis.

## Pitfalls
- **Genome Quality**: Requires high-quality genome assemblies with accurate gene prediction.
- **Training Data**: Performance depends on training dataset composition.
- **False Positives**: May predict false positive gene clusters.
- **Computational Time**: Analysis of large genomes can be time-consuming.
- **Parameter Tuning**: CRF parameters may need adjustment for optimal results.

## Examples
### Predict gene clusters
**Args:** `gecco predict -i genome.fasta -o clusters.gff3`
**Explanation:** Predicts biosynthetic gene clusters in a genome sequence.

### With antiSMASH comparison
**Args:** `gecco compare -i genome.fasta -a antismash_results.gbk -o comparison.txt`
**Explanation:** Compares Gecco predictions with antiSMASH results.

### Train custom model
**Args:** `gecco train -i training_data/ -o custom_model.pkl`
**Explanation:** Trains a custom CRF model on labeled gene cluster data.

### Annotate domains
**Args:** `gecco domains -i genome.fasta -o domain_annotations.txt`
**Explanation:** Annotates functional domains in predicted gene clusters.

### Generate visualization
**Args:** `gecco plot -i clusters.gff3 -o cluster_plot.png`
**Explanation:** Generates visualization of predicted gene clusters.