---
name: kofamscan
category: annotation
description: KofamKOALA assigns K numbers to the user's sequence data by HMMER/HMMSEARCH against KOfam
tags: [kofamscan, annotation]
author: oxo-call-community
source_url: "https://www.genome.jp/tools/kofamkoala/"
---

## Concepts

- **Tool Overview**: kofamscan v1.3.0 - KofamKOALA assigns K numbers to the user's sequence data by HMMER/HMMSEARCH against KOfam (a customized HMM database of KEGG Orthologs (KOs)). K number assignments with scores above the predefined thresholds for individual KOs are more reliable than other proposed assignments. Such high score assignments are highlighted with asterisks '*' in the output. The K number assignments facilitate the interpretation of the annotation results by linking the user's sequence data to the KEGG pathways and EC numbers..
- **Core Function**: KofamKOALA assigns K numbers to the user's sequence data by HMMER/HMMSEARCH against KOfam
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kofamscan`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Annotate proteins
**Args:** `-f mapper -p profiles -k ko_list -i proteins.faa -o annotation.tsv`
**Explanation:** Annotates protein sequences with KEGG Orthology using HMM profiles.

