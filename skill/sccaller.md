---
name: sccaller
category: variant-calling
description: Dong X et al. Accurate identification of single-nucleotide variants in whole-genome-amplified single cells. Nat Methods. 2017 May;14(5):491-493. doi: 10.1038/nmeth.4227
tags: ["sccaller", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/biosinodx/SCcaller"
---

## Concepts

- **Tool Overview**: Dong X et al. Accurate identification of single-nucleotide variants in whole-genome-amplified single cells. Nat Methods. 2017 May;14(5):491-493. doi: 10.1038/nmeth.4227 (version 2.0.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sccaller`

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

