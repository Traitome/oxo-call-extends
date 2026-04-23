---
name: rgi
category: annotation
description: This tool provides a preliminary annotation of your DNA sequence(s) based upon the data available in The Comprehensive Antibiotic Resistance Database (CARD). Hits to genes tagged with Antibiotic Resistance ontology terms will be highlighted. As CARD expands to include more pathogens, genomes, plasmids, and ontology terms this tool will grow increasingly powerful in providing first-pass detection of antibiotic resistance associated genes. See license at CARD website.
tags: ["rgi", "annotation"]
author: oxo-call-community
source_url: "https://card.mcmaster.ca"
---

## Concepts

- **Tool Overview**: This tool provides a preliminary annotation of your DNA sequence(s) based upon the data available in The Comprehensive Antibiotic Resistance Database (CARD). Hits to genes tagged with Antibiotic Resistance ontology terms will be highlighted. As CARD expands to include more pathogens, genomes, plasmids, and ontology terms this tool will grow increasingly powerful in providing first-pass detection of antibiotic resistance associated genes. See license at CARD website. (version 6.0.5)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rgi`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Annotate features
**Args:** `-i genome.fasta -o annotation.gff`
**Explanation:** Predicts and annotates genomic features.

