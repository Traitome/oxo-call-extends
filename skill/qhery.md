---
name: qhery
category: variant-calling
description: Identification of mutations in SARS-CoV-2 associated with resistance to treatment.
tags: ["qhery", "variant-calling"]
author: oxo-call-community
source_url: "http://github.com/mjsull/qhery/"
---

## Concepts

- **Tool Overview**: Identification of mutations in SARS-CoV-2 associated with resistance to treatment. (version 0.1.2)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qhery`

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

