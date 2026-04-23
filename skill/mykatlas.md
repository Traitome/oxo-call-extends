---
name: mykatlas
category: annotation
description: Assists in discoveries of antibiotic-resistance with mykrobe
tags: [mykatlas, annotation, antibiotic-resistance, mykrobe, bacteria]
author: oxo-call-community
source_url: "http://github.com/phelimb/atlas"
---

## Concepts

- **Tool Overview**: MykAtlas v0.6.1 - assists in antibiotic resistance discovery with Mykrobe.
- **Core Function**: Provides database and utilities for antibiotic resistance gene detection with Mykrobe.
- **Input/Output**: Works with Mykrobe for resistance prediction; provides reference data.
- **Installation**: `conda install -c bioconda mykatlas`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Dependencies**: Designed to work with Mykrobe.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fasta -o results.json`
**Explanation:** Assists Mykrobe in antibiotic resistance prediction.
