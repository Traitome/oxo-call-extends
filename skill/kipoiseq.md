---
name: kipoiseq
category: machine-learning
description: "kipoiseq: sequence-based data-loaders for Kipoi"
tags: [kipoiseq, machine-learning, data-loading, genomics, sequences]
author: oxo-call-community
source_url: "https://kipoi.org/kipoiseq/"
---
## Concepts

- **Sequence Data Loading**: Efficiently loads genomic sequence data for machine learning
- **Data Augmentation**: Supports sequence augmentation for training robustness
- **One-hot Encoding**: Converts DNA sequences to one-hot encoded matrices
- **Variant Integration**: Handles genetic variants in sequence context
- **Streaming Processing**: Enables streaming large genomic datasets
- **Model Compatibility**: Designed to work seamlessly with Kipoi models

## Pitfalls

- **Memory Management**: Large genomes require careful memory management
- **Sequence Length**: Fixed sequence lengths may truncate important regions
- **Strand Handling**: Proper strand orientation is critical for predictions
- **Variant Representation**: Variant encoding affects model performance
- **Reference Genome**: Must match the reference used for model training
- **Batch Processing**: Optimal batch size depends on hardware capabilities

## Examples

### Load FASTA sequences
**Args:** `kipoiseq load fasta genome.fa --regions regions.bed -o sequences.npz`
**Explanation:** Loads sequences from FASTA file for specified genomic regions.

### One-hot encode sequences
**Args:** `kipoiseq one-hot -i sequences.fasta -o encoded.npy`
**Explanation:** Converts DNA sequences to one-hot encoded numpy arrays.

### Apply variant effects
**Args:** `kipoiseq variant-effect -i variants.vcf -r genome.fa -o affected_seqs.fasta`
**Explanation:** Applies variants to reference sequences to create alternative sequences.

### Augment sequences
**Args:** `kipoiseq augment -i sequences.fasta -o augmented.fasta --mutate 0.01`
**Explanation:** Augments sequences with random mutations for training.

### Stream large dataset
**Args:** `kipoiseq stream -i big_genome.fa -r regions.bed --batch-size 32`
**Explanation:** Streams sequences in batches to avoid loading entire genome into memory.

### Create TFRecord dataset
**Args:** `kipoiseq tfrecord -i sequences.fasta -o dataset.tfrecord`
**Explanation:** Converts sequences to TensorFlow TFRecord format for efficient training.