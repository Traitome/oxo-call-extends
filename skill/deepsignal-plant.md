---
name: deepsignal-plant
category: epigenomics
description: A deep-learning method for detecting DNA methylation state from Oxford Nanopore sequencing reads of plants.
tags: [deepsignal-plant, epigenomics, methylation, nanopore, deep-learning, plant]
author: oxo-call-community
source_url: "https://github.com/PengNi/deepsignal-plant"
---

## Concepts

- **Tool Overview**: DeepSignal-Plant v0.1.6 - Deep learning method for detecting DNA methylation from Nanopore reads specifically for plant genomes.
- **Core Function**: Detects 5mC methylation in plant genomes from Oxford Nanopore signal data using deep learning.
- **Input/Output**: Expects Nanopore FAST5/FASTQ and reference genome; outputs methylation calls in BED/VCF format.
- **Installation**: `conda install -c bioconda deepsignal-plant`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Nanopore signal data and a plant reference genome.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepsignal-plant call_mods --input_path reads/ --ref ref.fa --output results/`
**Explanation:** Detects DNA methylation from plant Nanopore reads.
