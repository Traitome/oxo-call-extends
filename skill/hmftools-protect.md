---
name: hmftools-protect
category: hpc
description: PROTECT determines the clinical evidence applicable for a particular tumor sample based on all genomic events and signatures that are determined by the Hartwig pipeline.
tags: [hmftools-protect, hpc, SAM]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/protect/README.md"
---

## Concepts

- **Tool Overview**: hmftools-protect (v2.3) - PROTECT determines the clinical evidence applicable for a particular tumor sample based on all genomic events and signatures that are determined by the Hartwig pipeline.
- **Core Function**: Provides functionality for hpc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hmftools-protect`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
