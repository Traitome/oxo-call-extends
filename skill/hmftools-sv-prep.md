---
name: hmftools-sv-prep
category: qc
description: SV Prep generates a maximally filtered SV BAM file by identifying candidate SV junctions and extracting all reads that may provide support to that junction.
tags: [hmftools-sv-prep, qc, BAM]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/sv-prep"
---

## Concepts

- **Tool Overview**: hmftools-sv-prep (v1.2.4) - SV Prep generates a maximally filtered SV BAM file by identifying candidate SV junctions and extracting all reads that may provide support to that junction.
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hmftools-sv-prep`

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
