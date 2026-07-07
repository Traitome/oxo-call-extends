---
name: rich-msa
category: alignment
description: Rich-MSA renders multiple sequence alignments in the terminal.
tags: [rich-msa, alignment, visualization, terminal]
author: oxo-call-community
source_url: "https://github.com/althonos/rich-msa"
---

## Concepts

- **Tool Overview**: rich-msa visualizes alignments.
- **Core Function**: MSA terminal visualization.
- **Algorithm**: Uses terminal rendering methods.
- **Input Format**: Accepts alignment files.
- **Output**: Produces terminal display.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Terminal Support**: Requires compatible terminal.
- **Alignment Size**: Limits visualization.
- **Parameters**: Must be configured.
- **Display Issues**: May have rendering issues.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rich-msa --help`
**Explanation:** Shows available options and usage instructions.

### View alignment
**Args:** `rich-msa view -i alignment.fasta`
**Explanation:** Displays MSA in terminal.

### With parameters
**Args:** `rich-msa view -i alignment.fasta -p params.yaml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rich-msa -v view -i alignment.fasta`
**Explanation:** Runs with verbose output.

### With colors
**Args:** `rich-msa view -i alignment.fasta --colors`
**Explanation:** Enables color highlighting.

### With consensus
**Args:** `rich-msa view -i alignment.fasta --consensus`
**Explanation:** Shows consensus sequence.

### Save to file
**Args:** `rich-msa view -i alignment.fasta -o alignment.txt`
**Explanation:** Saves alignment to file.