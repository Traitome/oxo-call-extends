---
name: igor_vdj
category: utility
description: IGoR is a C++ software designed to infer V(D)J recombination related processes from sequencing data
tags: [igor_vdj, IGoR, VDJ recombination, immune repertoire]
author: oxo-call-community
source_url: "https://github.com/qmarcou/IGoR"
---

## Concepts

- **Tool Overview**: IGoR (Inference and Generation of Repertoires) is a versatile C++ software for analyzing and modeling immune receptor generation processes
- **Core Function**: Infers V(D)J recombination probabilities, somatic hypermutation patterns, and selection pressures from high-throughput sequencing data
- **Input/Output**: Accepts AIRR-seq data in various formats; outputs probabilistic annotations and repertoire models
- **Installation**: `conda install -c bioconda igor_vdj`
- **Key Features**: Supports both BCR and TCR analysis, handles cDNA and gDNA data, provides SHM statistics

## Pitfalls

- **Computational Intensity**: Inference algorithms can be computationally expensive for large datasets
- **Reference Gene Sets**: Requires high-quality germline gene references for accurate recombination inference
- **Model Complexity**: Choosing appropriate model parameters requires understanding of recombination biology
- **Memory Usage**: May require significant RAM for processing large repertoire datasets
- **Learning Curve**: Advanced features require understanding of the underlying probabilistic models

## Examples

### Infer V(D)J recombination model from data
**Args:** `igor infer -i sequences.fasta -o model.json`
**Explanation:** Learns recombination probabilities from input sequence data.

### Generate synthetic sequences from model
**Args:** `igor generate -m model.json -n 1000 -o synthetic_sequences.fasta`
**Explanation:** Generates synthetic immune receptor sequences using a trained model.

### Analyze SHM patterns
**Args:** `igor shm -i sequences.fasta -m model.json -o shm_analysis.txt`
**Explanation:** Analyzes somatic hypermutation patterns and hotspots.

### Annotate sequences with recombination events
**Args:** `igor annotate -i sequences.fasta -m model.json -o annotated.csv`
**Explanation:** Annotates input sequences with inferred recombination events and probabilities.

### Compare two repertoire models
**Args:** `igor compare -m1 model1.json -m2 model2.json -o comparison.txt`
**Explanation:** Compares recombination models from different datasets or conditions.
