---
name: proteomiqon-alignmentbasedquantification
category: alignment
description: Given an MS run in the mzLite or mzml format and a list of a list of peptides deduced by alignment, this tool iterates accross all and performs an XIC extration and quantification in similar to the PSMbasedQuantification tool.
tags: ["proteomiqon-alignmentbasedquantification", "alignment"]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/AlignmentBasedQuantification.html"
---

## Concepts

- **Tool Overview**: Given an MS run in the mzLite or mzml format and a list of a list of peptides deduced by alignment, this tool iterates accross all and performs an XIC extration and quantification in similar to the PSMbasedQuantification tool. (version 0.0.2)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda proteomiqon-alignmentbasedquantification`

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

