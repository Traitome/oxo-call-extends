---
name: eagle2
category: variant-calling
description: "The Eagle software estimates haplotype phase either within a genotyped cohort or using a phased reference panel."
tags: [eagle2, variant-calling]
author: oxo-call-community
source_url: "https://github.com/poruloh/Eagle"
---

## Concepts
- **Tool Overview**: Eagle2 is now the default phasing method used by the Sanger and Michigan imputation servers and uses a new very fast HMM-based algorithm that improves speed and accuracy over existing methods via two key ideas; a new data structure based on the positional Burrows-Wheeler transform and a rapid search algorithm that explores only the most relevant paths through the HMM. Compared to the Eagle1 algorithm, Eagle2 has similar speed but much greater accuracy at sample sizes <50,000; as such, we have made the Eagle2 algorithm the default option. (The Eagle1 algorithm can be accessed via the --v1 flag.) Eagle v2.3+ supports phasing sequence data with or without a reference and also supports phasing chrX.
- **Core Function**: The Eagle software estimates haplotype phase either within a genotyped cohort or using a phased reference panel.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda eagle2`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
