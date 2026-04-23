---
name: pvacseq
category: variant-calling
description: Personalized Variant Antigens by Cancer Sequencing (pVAC-Seq)
tags: ["pvacseq", "variant-calling"]
author: oxo-call-community
source_url: "http://pvac-seq.readthedocs.io/"
---

## Concepts

- **Tool Overview**: Personalized Variant Antigens by Cancer Sequencing (pVAC-Seq) (version 4.0.10)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pvacseq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Call variants
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants from aligned reads.

