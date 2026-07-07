---
name: ctat-lncrna
category: utility
description: ctat-lncrna uses slncky for long non-coding RNA analysis
tags: [ctat-lncrna, utility, lncRNA, RNA-seq, transcriptomics, slncky]
author: oxo-call-community
source_url: "https://github.com/NCIP/ctat-lncrna"
---

## Concepts

- **Tool Overview**: ctat-lncrna (v1.0.1+) is a tool for analyzing long non-coding RNA (lncRNA) sequences using the slncky algorithm.
- **Core Function**: Identifies and characterizes lncRNAs from RNA-Seq data, providing classification and functional annotation.
- **Input/Output**: Input: FASTA sequences, RNA-Seq alignments, gene annotations. Output: lncRNA predictions, classification reports, functional annotations.
- **Algorithm**: Uses slncky (SVM-based LncRNA Classification Kit) for machine learning-based classification of lncRNAs.
- **Key Features**: Classifies lncRNAs by type (intergenic, intronic, antisense), predicts coding potential, integrates with genomic annotations.
- **Installation**: `conda install -c bioconda ctat-lncrna`

## Pitfalls

- **Annotation Requirements**: Requires comprehensive gene annotations for accurate classification.
- **Training Data**: Performance depends on training data quality; may need retraining for specific organisms.
- **Sequence Length**: Designed for long non-coding RNAs; short sequences may produce unreliable results.
- **Memory Usage**: Large transcriptome datasets may require significant memory.
- **Output Interpretation**: Classification results should be validated with experimental methods.

## Examples

### Predict lncRNAs from FASTA
**Args:** `ctat-lncrna -i transcripts.fasta -g genes.gtf -o lncRNA_predictions.tsv`
**Explanation:** Classify transcripts as lncRNAs or protein-coding based on sequence features.

### Analyze intergenic lncRNAs
**Args:** `ctat-lncrna -i transcripts.fasta -g genes.gtf -o results/ --type intergenic`
**Explanation:** Focus analysis on intergenic lncRNAs only.

### Predict coding potential
**Args:** `ctat-lncrna -i transcripts.fasta -o coding_potential.txt --predict-coding`
**Explanation:** Calculate coding potential scores for input sequences.
