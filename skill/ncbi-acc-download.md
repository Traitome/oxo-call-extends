---
name: ncbi-acc-download
category: utility
description: Download files from NCBI Entrez by accession.
tags: [ncbi-acc-download, utility, ncbi, download, accession]
author: oxo-call-community
source_url: "https://github.com/kblin/ncbi-acc-download/"
---

## Concepts

- **Tool Overview**: NCBI Acc Download v0.2.8 - downloads files from NCBI Entrez by accession number.
- **Core Function**: Retrieves sequence and annotation files from NCBI databases using accession numbers.
- **Input/Output**: Takes accession numbers; downloads corresponding files from NCBI.
- **Installation**: `conda install -c bioconda ncbi-acc-download`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network**: Requires internet access to NCBI servers.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Download by accession
**Args:** `NC_000913.3`
**Explanation:** Downloads files for E. coli K-12 genome accession.

### Download protein
**Args:** `--format protein WP_000000001.1`
**Explanation:** Downloads protein sequence by accession.
