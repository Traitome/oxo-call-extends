---
name: panqc
category: qc
description: A toolkit for quality control & adjustment of nucleotide redundancy in bacterial pan-genome analyses
tags: [panqc, qc]
author: oxo-call-community
source_url: "https://github.com/maxgmarin/panqc"
---

## Concepts
- **Tool Overview**: panqc is a pan-genome quality control toolkit that evaluates and corrects for nucleotide redundancy in pan-genome analyses. The panqc Nucleotide Redundancy Correction (NRC) pipeline adjusts for redundancy at the DNA level within pan-genome estimates by comparing genes classified as absent at the amino acid level against their corresponding assemblies at the nucleotide level and by clustering genes using k-mer based nucleotide similarity metrics.
- **Core Function**: Processes bioinformatics data for qc tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda panqc`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
