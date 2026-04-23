---
name: ngspeciesid
category: metagenomics
description: Reference-free clustering and consensus forming of long-read amplicon sequencing
tags: [ngspeciesid, metagenomics]
author: oxo-call-community
source_url: "https://github.com/ksahlin/NGSpeciesID"
---

## Concepts
- **Tool Overview**: NGSpeciesID is a tool for clustering and consensus forming of long-read amplicon sequencing data (has been used with both PacBio and Oxford Nanopore data). The repository is a modified version of isONclust, where consensus, primer-removal, and polishing feautures have been added.
- **Core Function**: Processes bioinformatics data for metagenomics tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda ngspeciesid`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
