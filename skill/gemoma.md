---
name: gemoma
category: annotation
description: GeMoMa (Gene Model Mapper) is a homology-based gene prediction program that uses reference genome annotations to infer gene structures in target genomes.
tags: [gemoma, gene-prediction, homology-based, genome-annotation]
author: oxo-call-community
source_url: "http://www.jstacs.de/index.php/GeMoMa"
---

## Concepts
- **Homology-based Prediction**: Uses reference genome annotations for gene prediction.
- **Gene Structure Prediction**: Predicts exon-intron structures based on homology.
- **Intron Position Conservation**: Considers intron position conservation across species.
- **RNA-seq Integration**: Incorporates RNA-seq evidence for splice site prediction.
- **Cross-species Annotation**: Transfers annotations between related species.

## Pitfalls
- **Reference Quality**: Depends on high-quality reference genome annotations.
- **Evolutionary Distance**: Performance decreases with increasing evolutionary distance.
- **Gene Duplication**: May miss lineage-specific gene duplications.
- **Annotation Transfer**: Transfer errors can occur for rapidly evolving genes.
- **Computational Resources**: Requires significant memory for large genomes.

## Examples
### Predict genes using single reference
**Args:** `GeMoMa -t target.fasta -r reference.fasta -a reference_annot.gff3 -o predictions.gff3`
**Explanation:** Predicts genes in target genome using a single reference genome.

### With multiple references
**Args:** `GeMoMa -t target.fasta -r ref1.fasta ref2.fasta -a ref1_annot.gff3 ref2_annot.gff3 -o predictions.gff3`
**Explanation:** Uses multiple reference genomes for improved prediction.

### Incorporate RNA-seq data
**Args:** `GeMoMa -t target.fasta -r reference.fasta -a reference_annot.gff3 -rnaseq rnaseq.bam -o predictions.gff3`
**Explanation:** Incorporates RNA-seq evidence for splice site prediction.

### Evaluate predictions
**Args:** `GeMoMa -t target.fasta -r reference.fasta -a reference_annot.gff3 -eval -o evaluation.txt`
**Explanation:** Evaluates prediction accuracy using reference annotations.

### Generate training set
**Args:** `GeMoMa -t target.fasta -r reference.fasta -a reference_annot.gff3 -train -o training_data/`
**Explanation:** Generates training data for machine learning models.