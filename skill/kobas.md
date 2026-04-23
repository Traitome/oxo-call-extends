---
name: kobas
category: annotation
description: KEGG Orthology Based Annotation System
tags: [kobas, annotation]
author: oxo-call-community
source_url: "http://kobas.cbi.pku.edu.cn"
---

## Concepts

- **Tool Overview**: kobas v3.0.3 - KEGG Orthology Based Annotation System.
- **Core Function**: KEGG Orthology Based Annotation System
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kobas`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Annotate genes
**Args:** `kobas annotate -i genes.txt -s hsapiens -t gene`
**Explanation:** Annotates gene list with KEGG pathways and GO terms.

