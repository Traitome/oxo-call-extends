---
name: kmergenie
category: assembly
description: KmerGenie estimates the best k-mer length for genome de novo assembly.
tags: [kmergenie, assembly]
author: oxo-call-community
source_url: "http://kmergenie.bx.psu.edu"
---

## Concepts

- **Tool Overview**: kmergenie v1.7051 - KmerGenie estimates the best k-mer length for genome de novo assembly..
- **Core Function**: KmerGenie estimates the best k-mer length for genome de novo assembly.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kmergenie`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Estimate best k
**Args:** `-k 151 -l reads.lst -o output`
**Explanation:** Estimates best k-mer size for genome assembly from read files.

