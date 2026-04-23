---
name: tidehunter
category: annotation
description: TideHunter: efficient and sensitive tandem repeat detection from noisy long reads using seed-and-chain
tags: [tidehunter, annotation]
author: oxo-call-community
source_url: "https://github.com/yangao07/TideHunter"
---

## Concepts

- **Tool Overview**: tidehunter (v1.5.6) - TideHunter: efficient and sensitive tandem repeat detection from noisy long reads using seed-and-chain
- **Core Function**: TideHunter: efficient and sensitive tandem repeat detection from noisy long reads using seed-and-chain
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tidehunter`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tidehunter -i <input.fasta> -o <output.gff>`
**Explanation:** Run tidehunter with typical input and output options.
