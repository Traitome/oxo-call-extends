---
name: cuna
category: utility
description: "CUNA: Cytosine Uracil Neural Algorithm for ancient DNA damage detection using nanopore signals."
tags: [cuna, utility, ancient-DNA, nanopore, damage-detection, deep-learning]
author: oxo-call-community
source_url: "https://github.com/iris1901/CUNA"
---
## Concepts

- **Tool Overview**: cuna (v0.3.0+) is a deep learning pipeline for detecting cytosine deamination (C→U) events in ancient DNA using raw nanopore sequencing signals.
- **Core Function**: Uses neural networks to identify ancient DNA damage patterns from nanopore raw signal data, distinguishing true damage from sequencing errors.
- **Input/Output**: Input: Fast5 raw signal files, base-called FASTQ. Output: Damage probability scores, modified base calls.
- **Algorithm**: Deep learning model trained on known ancient DNA damage patterns to detect C→U deamination events.
- **Key Features**: Works directly on raw nanopore signals, high accuracy for ancient DNA samples, provides confidence scores.
- **Installation**: `conda install -c bioconda cuna`

## Pitfalls

- **Raw Signal Requirement**: Requires raw Fast5 files; base-called data alone is insufficient.
- **Training Data**: Performance depends on training data quality; may need retraining for specific sequencing conditions.
- **Ancient DNA Specific**: Designed for ancient DNA; may produce false positives on modern DNA.
- **Memory Usage**: Processing raw signals requires significant memory for large datasets.
- **Output Interpretation**: Damage scores should be interpreted with caution; consider biological context.

## Examples

### Detect ancient DNA damage
**Args:** `cuna -i reads.fast5 -o damage_scores.tsv`
**Explanation:** Analyze raw nanopore signals to detect C→U deamination events.

### Process base-called reads
**Args:** `cuna -i reads.fastq -f fast5/ -o damage_scores.tsv`
**Explanation:** Combine base-called FASTQ with raw Fast5 files for damage detection.

### Generate confidence scores
**Args:** `cuna -i reads.fast5 -o damage_scores.tsv --confidence`
**Explanation:** Output confidence scores along with damage predictions.
