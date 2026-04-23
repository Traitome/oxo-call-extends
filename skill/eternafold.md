---
name: eternafold
category: population-genomics
description: "RNA structure prediction algorithm improved through crowdsourced training data."
tags: [eternafold, population-genomics]
author: oxo-call-community
source_url: "https://eternagame.github.io/EternaFold"
---

## Concepts
- **Tool Overview**: EternaFold performs multitask learning to improve RNA structure prediction. Its training tasks include 1) predicting single structures, 2) maximizing the likelihood of structure probing data, and 3) predicting experimentally-measured affinities of RNA molecules to proteins and small molecules. Described in the paper https://www.nature.com/articles/s41592-022-01605-0
- **Core Function**: RNA structure prediction algorithm improved through crowdsourced training data.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda eternafold`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
