---
name: variant-effect-predictor
category: variant-calling
description: The VEP determines the effect of your variants (SNPs, insertions, deletions, CNVs or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.
tags: [variant-effect-predictor, variant-calling]
author: oxo-call-community
source_url: "http://www.ensembl.org/info/docs/tools/vep/index.html"
---

## Concepts

- **Tool Overview**: variant-effect-predictor (v87) - The VEP determines the effect of your variants (SNPs, insertions, deletions, CNVs or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.
- **Core Function**: The VEP determines the effect of your variants (SNPs, insertions, deletions, CNVs or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda variant-effect-predictor`

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
