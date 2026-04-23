---
name: caalm
category: annotation
description: Carbohydrate Activity Annotation with protein Language Models
tags: [caalm, carbohydrate, annotation, protein, language-model]
author: oxo-call-community
source_url: "https://github.com/lczong/CAALM"
---

## Concepts

- **Tool Overview**: CAALM annotates carbohydrate-active enzymes using protein language models.
- **Core Function**: Predicts carbohydrate activity from protein sequences using deep learning.
- **Input**: Protein FASTA files.
- **Output**: Carbohydrate activity predictions and enzyme classifications.
- **Model**: Uses protein language models for annotation.
- **Installation**: Install via bioconda: `conda install -c bioconda caalm`

## Pitfalls

- **Protein Input**: Requires protein sequences, not nucleotide.
- **Model Download**: May need to download pre-trained model weights.
- **GPU Optional**: GPU accelerates prediction but not required.

## Examples

### Annotate carbohydrate enzymes
**Args:** `caalm -i proteins.fa -o cazyme_annotations.tsv`
**Explanation:** Predicts carbohydrate activity for protein sequences.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
