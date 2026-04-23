---
name: trumicount
category: expression
description: For NGS experiments using unique molecular identifiers (UMIs), molecules that are lost entirely during sequencing cause under- estimation of the molecule count, and amplification artifacts like PCR chimeras cause over-estimation. TRUmiCount corrects UMI data for both types of errors, thus improving the accuracy of measured molecule counts considerably.
tags: [trumicount, expression]
author: oxo-call-community
source_url: "https://cibiv.github.io/trumicount/"
---

## Concepts

- **Tool Overview**: trumicount (v0.9.14) - For NGS experiments using unique molecular identifiers (UMIs), molecules that are lost entirely during sequencing cause under- estimation of the molecule count, and amplification artifacts like PCR chimeras cause over-estimation. TRUmiCount corrects UMI data for both types of errors, thus improving the accuracy of measured molecule counts considerably.
- **Core Function**: For NGS experiments using unique molecular identifiers (UMIs), molecules that are lost entirely during sequencing cause under- estimation of the molecule count, and amplification artifacts like PCR chimeras cause over-estimation. TRUmiCount corrects UMI data for both types of errors, thus improving the accuracy of measured molecule counts considerably.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trumicount`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
