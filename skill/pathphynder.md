---
name: pathphynder
category: population-genomics
description: A workflow for ancient DNA placement into reference phylogenies.
tags: [pathphynder, population-genomics]
author: oxo-call-community
source_url: "https://github.com/ruidlpm/pathPhynder"
---

## Concepts
- **Tool Overview**: Ancient DNA data is characterized by deamination and low-coverage sequencing, which results in a high fraction of missing data and erroneous calls. These factors affect the estimation of phylogenetic trees with modern and ancient DNA, especially when dealing with many ancient samples sequenced to lower coverage. Furthermore, most ancient DNA analyses of the Y chromosome, for example, rely on previously known markers, but additional variation will continuously emerge as more data is generated. This workflow offers a solution for integrating ancient and present-day haploid data, first by identifiying informative markers in a high coverage dataset, second, by calling and filtering these SNPs in ancient samples and lastly, by traversing the tree and evaluate the number of derived and ancestral markers in the ancients to find the most likely branch where it belongs.
- **Core Function**: A workflow for ancient DNA placement into reference phylogenies.
- **Input/Output**: FASTA/BAM/SAM/VCF/GFF/GTF
- **Installation**: `conda install -c bioconda pathphynder`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
