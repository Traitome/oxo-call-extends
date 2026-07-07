---
name: unifeb
category: bioinformatics
description: UniFEB - Universal functional enrichment browser.
tags: [unifeb, functional-enrichment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/unifeb/"
---

## Concepts

- **Tool Overview**: UniFEB - A tool for functional enrichment analysis and visualization.
- **Core Function**: Performs functional enrichment analysis on gene lists.
- **Input**: Gene list, annotation database.
- **Output**: Enrichment results and visualizations.
- **Installation**: Install via pip or conda
- **Use Case**: Gene expression analysis, functional genomics, bioinformatics.

## Pitfalls

- **Database Requirements**: Requires annotation databases.
- **Memory**: May require significant memory for large gene lists.

## Examples

### Perform enrichment
**Args:** `unifeb -i genes.txt -d go -o enrichment/`
**Explanation:** Perform GO enrichment analysis.

### With visualization
**Args:** `unifeb -i genes.txt -d go -o enrichment/ --plot`
**Explanation:** Generate enrichment plot.
