---
name: ncbi-acc-download
category: utility
description: ncbi-acc-download downloads files from NCBI Entrez databases using accession numbers.
tags: [ncbi-acc-download, utility, ncbi, download, accession]
author: oxo-call-community
source_url: "https://github.com/kblin/ncbi-acc-download/"
---

## Concepts

- **Tool Overview**: ncbi-acc-download v0.2.8 is a command-line tool for downloading sequences from NCBI Entrez databases.
- **Core Function**: Retrieves sequence and annotation files from NCBI using accession numbers.
- **Algorithm**: Queries NCBI Entrez API and downloads corresponding data files.
- **Input Format**: Accepts NCBI accession numbers as command-line arguments.
- **Output**: Downloads sequence files in FASTA, GenBank, or other formats.
- **Use Case**: Retrieving reference sequences, downloading genomes, and fetching annotation data.

## Pitfalls

- **Network Dependency**: Requires internet access to NCBI servers.
- **Rate Limiting**: NCBI may block excessive download requests.
- **Accession Format**: Requires valid NCBI accession numbers.
- **Version Differences**: Options may vary between versions.
- **Output Management**: Multiple downloads can clutter the working directory.
- **Error Handling**: Network errors may cause incomplete downloads.

## Examples

### Display help
**Args:** `ncbi-acc-download --help`
**Explanation:** Shows available options and usage instructions.

### Download genome by accession
**Args:** `ncbi-acc-download NC_000913.3`
**Explanation:** Downloads E. coli K-12 genome by accession number.

### Download protein sequence
**Args:** `ncbi-acc-download --format protein WP_000000001.1`
**Explanation:** Downloads protein sequence in FASTA format.

### Download GenBank format
**Args:** `ncbi-acc-download --format genbank NC_000913.3`
**Explanation:** Downloads sequence in GenBank format with annotations.

### Multiple accessions
**Args:** `ncbi-acc-download NC_000913.3 NC_012920.1`
**Explanation:** Downloads multiple sequences in batch.

### Output directory
**Args:** `ncbi-acc-download --output-dir genomes/ NC_000913.3`
**Explanation:** Saves downloaded files to specified directory.