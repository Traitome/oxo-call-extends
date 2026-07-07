---
name: deepmod
category: epigenomics
description: DeepMod - deep learning method for DNA modification (5mC and 6mA) prediction from Nanopore data.
tags: [deepmod, epigenomics, methylation, deep-learning, nanopore]
author: oxo-call-community
source_url: "https://github.com/WGLab/DeepMod"
---

## Concepts

- **Tool Overview**: deepmod (v0.1.3+) is a deep learning-based method for detecting DNA modifications (5mC and 6mA) from Oxford Nanopore sequencing data. It analyzes raw signal data to identify epigenetic modifications.
- **Core Function**: Predicts DNA methylation states (5mC, 6mA) from Nanopore raw signal data using recurrent neural networks, enabling direct detection without bisulfite sequencing.
- **Input/Output**: Input: Nanopore FAST5/FASTQ files, reference genome. Output: Methylation calls in BED/VCF format, modification statistics.
- **Algorithm**: Uses recurrent neural networks (RNNs) to model the relationship between raw Nanopore signals and DNA methylation states.
- **Key Features**: Direct signal analysis, supports multiple modification types, high accuracy, integrates with Nanopore workflows, no bisulfite required.
- **Installation**: `conda install -c bioconda deepmod`

## Pitfalls

- **Signal Quality**: Requires high-quality Nanopore signal data.
- **Reference Genome**: Must use compatible reference genome.
- **Computational Resources**: Requires significant computational resources.
- **Training Data**: Performance depends on training dataset diversity.
- **Modification Density**: May struggle with very low modification densities.

## Examples

### Detect DNA methylation
**Args:** `deepmod detect --fastq reads.fq --reference ref.fa --output methylation/`
**Explanation:** Detects DNA methylation from Nanopore reads against a reference.

### From FAST5 files
**Args:** `deepmod detect --fast5 fast5/ --reference ref.fa --output methylation/`
**Explanation:** Use raw FAST5 signal files for methylation detection.

### With model fine-tuning
**Args:** `deepmod train --fast5 training_data/ --reference ref.fa --output model/`
**Explanation:** Train custom methylation detection model.