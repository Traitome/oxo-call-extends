---
name: card_trick
category: annotation
description: Utility package to find gene-drug relationships within CARD antibiotic resistance database
tags: [card, antibiotic-resistance, amr, drug, annotation]
author: oxo-call-community
source_url: "https://gitlab.com/cgps/card_trick"
---

## Concepts

- **Tool Overview**: card_trick finds gene-drug relationships within the CARD antibiotic resistance database.
- **Core Function**: Queries CARD database for resistance gene and drug associations.
- **Input**: Gene names or ARO accessions.
- **Output**: Associated drug resistance profiles.
- **Application**: Antimicrobial resistance annotation and reporting.
- **Installation**: Install via bioconda: `conda install -c bioconda card_trick`

## Pitfalls

- **CARD Database**: Requires access to CARD database data.
- **ARO Ontology**: Understanding ARO classification helps interpretation.
- **Python Only**: Python library with CLI interface.

## Examples

### Find drug resistance for gene
**Args:** `card_trick search --gene "mecA" -o results.tsv`
**Explanation:** Searches CARD for drug resistance associated with mecA gene.

### List resistance categories
**Args:** `card_trick categories -o categories.tsv`
**Explanation:** Lists all antibiotic resistance categories in CARD.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
