---
name: proteomiqon-proteininference
category: alignment
description: MS-based shotgun proteomics estimates protein abundances using a proxy: peptides. The process of 'Protein Inference' is concerned with the mapping of identified peptides to the proteins they putatively originated from.
tags: ["proteomiqon-proteininference", "alignment", "sam"]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/ProteinInference.html"
---

## Concepts

- **Tool Overview**: MS-based shotgun proteomics estimates protein abundances using a proxy: peptides. The process of 'Protein Inference' is concerned with the mapping of identified peptides to the proteins they putatively originated from. (version 0.0.7)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda proteomiqon-proteininference`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

