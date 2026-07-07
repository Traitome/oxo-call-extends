---
name: clairvoyante
category: variant-calling
description: Deep learning-based variant caller for single-molecule sequencing data
tags: [clairvoyante, variant-calling, long-reads, deep-learning, snp, indel]
author: oxo-call-community
source_url: "https://github.com/aquaskyline/Clairvoyante"
---

## Concepts

- **Tool Overview**: Clairvoyante is a deep learning-based variant caller for single-molecule sequencing data (ONT, PacBio, Illumina), using a multi-task convolutional neural network.
- **Core Function**: Predicts variant type, zygosity, alternative allele, and indel length from aligned sequencing data.
- **Algorithm**: Uses a five-layer convolutional neural network for multi-task variant prediction.
- **Input**: Aligned BAM/SAM file and reference genome (FASTA).
- **Output**: VCF file with variant calls and quality scores.
- **Application**: Germline variant calling from long-read and short-read sequencing data.
- **Installation**: Install via bioconda: `conda install -c bioconda clairvoyante`

## Pitfalls

- **Computational Resources**: Requires significant computational resources for training and prediction.
- **Reference Genome**: Must match the reference used for alignment.
- **Model Complexity**: Full model requires more resources but provides better accuracy.
- **BAM Index**: Input BAM must be indexed.
- **Data Quality**: Performance depends on input data quality.

## Examples

### Call variants from BAM
**Args:** `runClairvoyante.py --bam reads.bam --ref reference.fa --model model.pb --output output.vcf`
**Explanation:** Calls variants from aligned BAM file using pre-trained model.

### Train custom model
**Args:** `trainClairvoyante.py --train_bam train.bam --train_vcf train.vcf --ref reference.fa --output model.pb`
**Explanation:** Trains a custom Clairvoyante model on labeled data.

### Evaluate model
**Args:** `evaluateClairvoyante.py --bam test.bam --vcf truth.vcf --ref reference.fa --model model.pb`
**Explanation:** Evaluates model performance against truth variants.

### Display help
**Args:** `runClairvoyante.py --help`
**Explanation:** Shows all available options and usage information.