---
name: ncbi-genome-download
category: utility
description: ncbi-genome-download downloads genome files from the NCBI FTP server with flexible filtering options.
tags: [ncbi-genome-download, utility, ncbi, download, genome]
author: oxo-call-community
source_url: "https://github.com/kblin/ncbi-genome-download/"
---

## Concepts

- **Tool Overview**: ncbi-genome-download is a command-line tool for downloading genome sequences from NCBI.
- **Core Function**: Retrieves complete genomes, chromosomes, and annotations from NCBI's FTP server.
- **Algorithm**: Parses NCBI's genome assembly reports and downloads specified files.
- **Input Format**: Accepts taxonomic filters, assembly levels, and file format specifications.
- **Output**: Downloads genome sequences in FASTA, GenBank, or other formats to specified directory.
- **Use Case**: Building local genome databases, downloading reference sequences, batch retrieval of genomes.

## Pitfalls

- **Network Dependency**: Requires stable internet connection for large downloads.
- **Rate Limiting**: NCBI may throttle FTP connections.
- **Storage Requirements**: Genome files can be very large.
- **Version Differences**: Options may vary between versions.
- **Partial Downloads**: Network interruptions can cause incomplete downloads.
- **Database Updates**: Genome versions may become outdated.

## Examples

### Display help
**Args:** `ncbi-genome-download --help`
**Explanation:** Shows available options and usage instructions.

### Download bacterial genomes
**Args:** `ncbi-genome-download bacteria`
**Explanation:** Downloads all bacterial genomes from NCBI.

### Download specific taxon
**Args:** `ncbi-genome-download --taxon "Escherichia coli" --assembly-level complete`
**Explanation:** Downloads complete E. coli genomes.

### Specify output directory
**Args:** `ncbi-genome-download bacteria --output-folder genomes/bacteria/`
**Explanation:** Saves downloads to specified directory.

### Filter by assembly level
**Args:** `ncbi-genome-download --assembly-level chromosome bacteria`
**Explanation:** Downloads only chromosome-level bacterial assemblies.

### Download in GenBank format
**Args:** `ncbi-genome-download --format genbank bacteria`
**Explanation:** Downloads genomes in GenBank format.