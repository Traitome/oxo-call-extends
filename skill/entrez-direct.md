---
name: entrez-direct
category: annotation
description: "Entrez Direct (EDirect) - Access to NCBI's Entrez databases"
tags: [entrez-direct, annotation]
author: oxo-call-community
source_url: "https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/25.3.20260410/README"
---

## Concepts
- **Tool Overview**: Entrez Direct (EDirect) provides access to Entrez, the NCBI's suite of interconnected databases (publication, sequence, structure, gene, variation, expression, etc.) from a Unix terminal window. Search terms are entered as command-line arguments. Individual operations are connected with Unix pipes to construct multi-step queries. Selected records can then be retrieved in a variety of formats.
- **Core Function**: Entrez Direct (EDirect) - Access to NCBI's Entrez databases
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda entrez-direct`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
