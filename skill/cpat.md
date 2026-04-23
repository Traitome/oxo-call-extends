---
name: cpat
category: annotation
description: Coding Potential Assessment Tool for distinguishing coding and noncoding RNA
tags: [cpat, coding-potential, lncrna, noncoding-rna, rna, annotation]
author: oxo-call-community
source_url: "https://github.com/liguowang/cpat"
---

## Concepts

- **Tool Overview**: CPAT (Coding Potential Assessment Tool) is a fast and accurate tool for distinguishing coding and noncoding RNA transcripts using logistic regression based on sequence features.
- **Core Function**: Classifies RNA transcripts as coding (mRNA) or noncoding (lncRNA) based on ORF coverage, Fickett score, hexamer usage, and ORF length.
- **Input/Output**: Input: Transcript sequences in FASTA format. Output: Classification table with coding probability scores and labels.
- **Species Models**: Provides pre-trained models for human, mouse, fly, and zebrafish. Custom models can be trained.
- **Speed**: Extremely fast compared to alignment-based methods (CPC, PhyloCSF), processing thousands of transcripts in seconds.
- **Accuracy**: Achieves >96% accuracy with very low false positive rate for noncoding RNA identification.

## Pitfalls

- **Species Model**: Must use the correct species-specific model. Using human model for mouse data reduces accuracy.
- **Transcript Length**: Very short transcripts (<200nt) may have unreliable coding potential scores.
- **Incomplete Transcripts**: Partial transcripts may be misclassified if the ORF is truncated.
- **Threshold**: Default threshold varies by species. Adjust for your specific application if needed.

## Examples

### Classify human transcripts
**Args:** `-i transcripts.fa -o cpat_results.tsv -d human_logitModel.txt -x human_Hexamer.tsv`
**Explanation:** Classifies human transcript sequences using the human pre-trained model and hexamer table.

### Classify mouse transcripts
**Args:** `-i transcripts.fa -o cpat_results.tsv -d mouse_logitModel.txt -x mouse_Hexamer.tsv`
**Explanation:** Uses the mouse-specific model for more accurate classification of mouse transcripts.

### Set custom threshold
**Args:** `-i transcripts.fa -o cpat_results.tsv -d human_logitModel.txt -x human_Hexamer.tsv -c 0.5`
**Explanation:** Sets coding probability threshold to 0.5 instead of default, adjusting sensitivity/specificity tradeoff.

### Process large transcriptome
**Args:** `-i transcriptome.fa -o cpat_results.tsv -d human_logitModel.txt -x human_Hexamer.tsv --top-orf 5`
**Explanation:** Considers top 5 ORFs per transcript instead of default 1, more thorough for complex transcripts.

### Train custom model
**Args:** `-x training_hexamer.tsv -d custom_model.txt -g coding.fa -n noncoding.fa`
**Explanation:** Trains a custom CPAT model from coding and noncoding training sequences for non-model organisms.

### Filter noncoding transcripts
**Args:** `-i transcripts.fa -o cpat_results.tsv -d human_logitModel.txt -x human_Hexamer.tsv --best-orf`
**Explanation:** Reports only the best ORF information, useful for downstream filtering of noncoding transcripts.
