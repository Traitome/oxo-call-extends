---
name: clairvoyante
category: alignment
description: Identifying the variants of DNA sequences sensitively and accurately is an important but challenging task in the field of genomics. This task is particularly difficult when dealing with Single Molecule Sequencing, the error rate of which is still tens to hundreds of times higher than Next Generation Sequencing. With the increasing prevalence of Single Molecule Sequencing, an efficient variant caller will not only expedite basic research but also enable various downstream applications. To meet this demand, we developed Clairvoyante, a multi-task five-layer convolutional neural network model for predicting variant type, zygosity, alternative allele and Indel length. On NA12878, Clairvoyante achieved 99.73%, 97.68% and 95.36% accuracy on known variants, and achieved 98.65%, 92.57%, 77.89% F1 score on the whole genome, in Illumina, PacBio, and Oxford Nanopore data, respectively. Training Clairvoyante with a sample and call variant on another shows that Clairvoyante is sample agnostic and general for variant calling. A slim version of Clairvoyante with reduced model parameters produced a much lower F1, suggesting the full model's power in disentangling subtle details in read alignment. Clairvoyante is the first method for Single Molecule Sequencing to finish a whole genome variant calling in two hours on a 28 CPU-core machine, with top-tier accuracy and sensitivity. A toolset was developed to train, utilize and visualize the Clairvoyante model easily, and is publically available here is this repo.
tags: [clairvoyante, alignment, SAM]
author: oxo-call-community
source_url: "https://github.com/aquaskyline/Clairvoyante"
---

## Concepts

- **Tool Overview**: clairvoyante (v1.02) - Identifying the variants of DNA sequences sensitively and accurately is an important but challenging task in the field of genomics. This task is particularly difficult when dealing with Single Molecule Sequencing, the error rate of which is still tens to hundreds of times higher than Next Generation Sequencing. With the increasing prevalence of Single Molecule Sequencing, an efficient variant caller will not only expedite basic research but also enable various downstream applications. To meet this demand, we developed Clairvoyante, a multi-task five-layer convolutional neural network model for predicting variant type, zygosity, alternative allele and Indel length. On NA12878, Clairvoyante achieved 99.73%, 97.68% and 95.36% accuracy on known variants, and achieved 98.65%, 92.57%, 77.89% F1 score on the whole genome, in Illumina, PacBio, and Oxford Nanopore data, respectively. Training Clairvoyante with a sample and call variant on another shows that Clairvoyante is sample agnostic and general for variant calling. A slim version of Clairvoyante with reduced model parameters produced a much lower F1, suggesting the full model's power in disentangling subtle details in read alignment. Clairvoyante is the first method for Single Molecule Sequencing to finish a whole genome variant calling in two hours on a 28 CPU-core machine, with top-tier accuracy and sensitivity. A toolset was developed to train, utilize and visualize the Clairvoyante model easily, and is publically available here is this repo.
- **Core Function**: Identifying the variants of DNA sequences sensitively and accurately is an important but challenging task in the field of genomics. This task is particularly difficult when dealing with Single Molecule Sequencing, the error rate of which is still tens to hundreds of times higher than Next Generation Sequencing. With the increasing prevalence of Single Molecule Sequencing, an efficient variant caller will not only expedite basic research but also enable various downstream applications. To meet this demand, we developed Clairvoyante, a multi-task five-layer convolutional neural network model for predicting variant type, zygosity, alternative allele and Indel length. On NA12878, Clairvoyante achieved 99.73%, 97.68% and 95.36% accuracy on known variants, and achieved 98.65%, 92.57%, 77.89% F1 score on the whole genome, in Illumina, PacBio, and Oxford Nanopore data, respectively. Training Clairvoyante with a sample and call variant on another shows that Clairvoyante is sample agnostic and general for variant calling. A slim version of Clairvoyante with reduced model parameters produced a much lower F1, suggesting the full model's power in disentangling subtle details in read alignment. Clairvoyante is the first method for Single Molecule Sequencing to finish a whole genome variant calling in two hours on a 28 CPU-core machine, with top-tier accuracy and sensitivity. A toolset was developed to train, utilize and visualize the Clairvoyante model easily, and is publically available here is this repo.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda clairvoyante`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
