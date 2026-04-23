---
name: varfish-annotator-cli
category: variant-calling
description: Annotate variants for import into VarFish Server.
tags: [varfish-annotator-cli, variant-calling]
author: oxo-call-community
source_url: "https://github.com/bihealth/varfish-annotator"
---

## Concepts

- **Tool Overview**: varfish-annotator-cli (v0.34) - Annotate variants for import into VarFish Server.
- **Core Function**: Annotate variants for import into VarFish Server.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda varfish-annotator-cli`

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
