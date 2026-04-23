---
name: symbiontscreener
category: utility
description: Symbiont-Screener is a reference-free approach to identifying high-confidence host's long reads from symbionts and contaminants and overcoming the low sequencing accuracy according to a trio-based screening model.
tags: [symbiontscreener, utility]
author: oxo-call-community
source_url: "https://github.com/BGI-Qingdao/Symbiont-Screener"
---

## Concepts

- **Tool Overview**: symbiontscreener (v1.0.0) - Symbiont-Screener is a reference-free approach to identifying high-confidence host's long reads from symbionts and contaminants and overcoming the low sequencing accuracy according to a trio-based screening model.
- **Core Function**: Symbiont-Screener is a reference-free approach to identifying high-confidence host's long reads from symbionts and contaminants and overcoming the low sequencing accuracy according to a trio-based screening model.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda symbiontscreener`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `symbiontscreener -i <input_file> -o <output_file>`
**Explanation:** Run symbiontscreener with typical input and output options.
