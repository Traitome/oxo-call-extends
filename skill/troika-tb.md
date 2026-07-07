---
name: troika-tb
category: analysis
description: Troika-TB - Tool for analyzing tuberculosis sequencing data.
tags: [troika-tb, tuberculosis, pathogen-genomics, variant-calling, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/Troika"
---

## Concepts

- **Tool Overview**: Troika-TB - A tool for analyzing and interpreting tuberculosis genome sequencing data.
- **Core Function**: Performs variant calling, lineage classification, and drug resistance prediction for TB.
- **Input**: FASTQ reads or BAM files, reference genome.
- **Output**: Variant calls, lineage assignments, drug resistance predictions.
- **Installation**: `pip install troika-tb`
- **Use Case**: Tuberculosis research, clinical diagnostics, public health.

## Pitfalls

- **Reference Genome**: Requires specific TB reference genome.
- **Quality Control**: Requires good quality sequencing data.

## Examples

### Analyze TB data
**Args:** `troika-tb -i reads.fastq -r h37rv.fasta -o results/`
**Explanation:** Analyze tuberculosis sequencing data.

### Drug resistance prediction
**Args:** `troika-tb resistance -i variants.vcf -o resistance.txt`
**Explanation:** Predict drug resistance from variants.
