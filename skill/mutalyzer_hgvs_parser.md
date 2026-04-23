---
name: mutalyzer_hgvs_parser
category: annotation
description: Mutalyzer HGVS variant description parser.
tags: [mutalyzer_hgvs_parser, annotation, hgvs, variant, parser]
author: oxo-call-community
source_url: "https://github.com/mutalyzer/hgvs-parser"
---

## Concepts

- **Tool Overview**: Mutalyzer HGVS Parser v0.4.0 - parses HGVS variant descriptions.
- **Core Function**: Parses and validates HGVS (Human Genome Variation Society) variant description strings.
- **Input/Output**: Takes HGVS variant description strings; outputs parsed variant representations.
- **Installation**: `conda install -c bioconda mutalyzer_hgvs_parser`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure HGVS descriptions follow the standard nomenclature.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `parse "NM_004006.2:c.4375C>T"`
**Explanation:** Parses an HGVS variant description string.
