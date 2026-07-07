---
name: translate-gard
category: analysis
description: Translate-GARD - Tool for detecting horizontal gene transfer.
tags: [translate-gard, hgt, horizontal-gene-transfer, phylogenetics, evolution]
author: oxo-call-community
source_url: "https://github.com/compbio/translate-gard"
---

## Concepts

- **Tool Overview**: Translate-GARD - A tool for detecting horizontal gene transfer (HGT) events using phylogenetic methods.
- **Core Function**: Identifies genes with unusual phylogenetic patterns indicative of HGT.
- **Input**: Sequence alignments, phylogenetic trees, taxonomic information.
- **Output**: HGT predictions, confidence scores, evolutionary analysis.
- **Installation**: `pip install translate-gard` or `conda install -c bioconda translate-gard`
- **Use Case**: Evolutionary biology, comparative genomics, microbial evolution.

## Pitfalls

- **Phylogenetic Signal**: Requires good phylogenetic signal for detection.
- **False Positives**: May produce false positive HGT calls.

## Examples

### Detect HGT
**Args:** `translate-gard -i alignment.fasta -t tree.nwk -o hgt_results/`
**Explanation:** Detect horizontal gene transfer events from sequence data.

### With taxonomic info
**Args:** `translate-gard -i alignments/ -t tree.nwk -tax taxonomy.txt -o results/`
**Explanation:** Use taxonomic information to improve HGT detection.
