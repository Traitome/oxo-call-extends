---
name: mykrobe
category: annotation
description: Antibiotic resistance prediction in minutes.
tags: [mykrobe, annotation, antibiotic-resistance, bacteria, prediction]
author: oxo-call-community
source_url: "https://github.com/Mykrobe-tools/mykrobe"
---

## Concepts

- **Tool Overview**: Mykrobe v0.13.0 - rapid antibiotic resistance prediction from genome sequence data.
- **Core Function**: Predicts antibiotic resistance for Staphylococcus aureus and Mycobacterium tuberculosis from genome sequences.
- **Input/Output**: Takes FASTQ or FASTA files; outputs resistance predictions and variant calls.
- **Installation**: `conda install -c bioconda mykrobe`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Species Support**: Primarily supports S. aureus and M. tuberculosis.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Predict resistance
**Args:** `mykrobe predict --sample sample_name --species staph_aureus -i reads.fastq.gz -o results.json`
**Explanation:** Predicts antibiotic resistance for S. aureus from sequencing reads.

### Genotype prediction
**Args:** `mykrobe genotype --sample sample_name --species tuberculosis -i assembly.fasta -o results.json`
**Explanation:** Predicts resistance genotypes for M. tuberculosis from assembly.
