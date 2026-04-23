---
name: star-fusion
category: variant-calling
description: STAR-Fusion fusion variant caller. All dependencies required to run FusionInspector and FusionAnnotator are included.
tags: [star-fusion, variant-calling]
author: oxo-call-community
source_url: "https://github.com/STAR-Fusion/STAR-Fusion/wiki"
---

## Concepts

- **Tool Overview**: star-fusion (v1.15.1) - STAR-Fusion fusion variant caller. All dependencies required to run FusionInspector and FusionAnnotator are included.
- **Core Function**: STAR-Fusion fusion variant caller. All dependencies required to run FusionInspector and FusionAnnotator are included.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda star-fusion`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `star-fusion -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run star-fusion with typical input and output options.
