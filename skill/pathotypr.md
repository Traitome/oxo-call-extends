---
name: pathotypr
category: variant-calling
description: Alignment-free genome classification using SNP markers and machine learning for genomic surveillance
tags: [pathotypr, variant-calling]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/pathotypr"
---

## Concepts
- **Tool Overview**: Pathotypr is a high-performance, alignment-free tool for genome classification using SNP markers and a pre-trained Random Forest model. It can be adapted to any organism given a custom set of markers or a trained model. The current curated models support Mycobacterium tuberculosis complex (MTBC) lineage assignment (L1-L10, A1-A4) and drug resistance genotyping using the WHO mutation catalogue (grades 1-2).
- **Core Function**: Alignment-free genome classification using SNP markers and machine learning for genomic surveillance
- **Input/Output**: BAM/SAM/VCF
- **Installation**: `conda install -c bioconda pathotypr`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
