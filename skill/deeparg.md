---
name: deeparg
category: metagenomics
description: DeepARG - deep learning based prediction of Antibiotic Resistance Genes from metagenomes.
tags: [deeparg, metagenomics, antibiotic-resistance, ARG, deep-learning]
author: oxo-call-community
source_url: "https://github.com/gaarangoa/deeparg"
---

## Concepts

- **Tool Overview**: deeparg (v1.0.4+) is a deep learning-based tool for predicting Antibiotic Resistance Genes (ARGs) from metagenomic data. It provides accurate and rapid identification of resistance genes.
- **Core Function**: Identifies antibiotic resistance genes in metagenomic sequences, enabling surveillance of antimicrobial resistance in microbial communities.
- **Input/Output**: Input: Metagenomic reads (FASTQ), assembled contigs (FASTA). Output: ARG predictions, resistance classes, abundance estimates, functional annotations.
- **Algorithm**: Uses deep neural networks trained on known ARG sequences to classify reads/contigs into resistance categories.
- **Key Features**: High accuracy, supports multiple resistance classes, rapid analysis, abundance estimation, functional annotation.
- **Installation**: `conda install -c bioconda deeparg`

## Pitfalls

- **Database Coverage**: May miss novel or uncharacterized ARGs.
- **Short Reads**: Short sequencing reads may reduce prediction accuracy.
- **Sequence Similarity**: Closely related genes may be misclassified.
- **Abundance Threshold**: Low-abundance ARGs may be missed.
- **Training Data**: Performance depends on training dataset diversity.

## Examples

### Predict ARGs from reads
**Args:** `deeparg predict -i reads.fastq -o arg_predictions.txt`
**Explanation:** Predict antibiotic resistance genes from metagenomic reads.

### From assembled contigs
**Args:** `deeparg predict -i contigs.fasta -o arg_predictions.txt`
**Explanation:** Analyze assembled contigs for ARGs.

### With abundance estimation
**Args:** `deeparg predict -i reads.fastq -o arg_predictions.txt --abundance`
**Explanation:** Include abundance estimates for detected ARGs.