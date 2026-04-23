---
name: sigprofilerassignment
category: variant-calling
description: SigProfilerAssignment - Assignment of known mutational signatures to individual samples and individual somatic mutations
tags: [sigprofilerassignment, variant-calling, sam]
author: oxo-call-community
source_url: "https://github.com/AlexandrovLab/SigProfilerAssignment.git"
---

## Concepts

- **Tool Overview**: sigprofilerassignment (v1.1.3) - SigProfilerAssignment - Assignment of known mutational signatures to individual samples and individual somatic mutations
- **Core Function**: SigProfilerAssignment - Assignment of known mutational signatures to individual samples and individual somatic mutations
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sigprofilerassignment`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sigprofilerassignment -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sigprofilerassignment with typical input and output options.
