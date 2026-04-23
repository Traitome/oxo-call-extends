---
name: mtglink
category: assembly
description: MTG-link is a local assembly tool for linked-read data
tags: [mtglink, assembly]
author: oxo-call-community
source_url: "https://github.com/anne-gcd/MTG-Link"
---

## Concepts

- **Tool Overview**: mtglink v2.4.1 - MTG-link is a local assembly tool for linked-read data.
- **Core Function**: MTG-link is a local assembly tool for linked-read data
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mtglink`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Scaffold contigs
**Args:** `mtglink -i input.gaf -j links.txt -o output`
**Explanation:** Scaffolds contigs using linked-read information.

