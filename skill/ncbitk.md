---
name: ncbitk
category: utility
description: NCBITK is a toolkit for accessing and processing NCBI's GenBank sequence data.
tags: [ncbitk, utility, ncbi, genbank, sequence]
author: oxo-call-community
source_url: "https://github.com/andrewsanchez/NCBITK"
---

## Concepts

- **Tool Overview**: NCBITK is a comprehensive toolkit for accessing NCBI's GenBank database programmatically.
- **Core Function**: Provides utilities for downloading, parsing, and analyzing GenBank sequence data.
- **Algorithm**: Interfaces with NCBI Entrez API to retrieve and process sequence information.
- **Input Format**: Accepts GenBank accession numbers, taxonomic identifiers, and search queries.
- **Output**: Produces sequence files, annotations, and analysis results in various formats.
- **Use Case**: Batch downloading sequences, automated annotation retrieval, and data integration.

## Pitfalls

- **API Rate Limits**: NCBI enforces rate limits on API requests.
- **Network Dependency**: Requires internet access to NCBI servers.
- **Version Compatibility**: API may change between versions.
- **Authentication**: Some endpoints require API keys for higher rate limits.
- **Data Volume**: Large downloads can consume significant bandwidth.
- **Error Handling**: Network errors require robust exception handling.

## Examples

### Display help
**Args:** `ncbitk --help`
**Explanation:** Shows available options and usage instructions.

### Download GenBank record
**Args:** `ncbitk download -a NC_000913.3 -o genome.gb`
**Explanation:** Downloads GenBank record by accession number.

### Batch download
**Args:** `ncbitk download -l accessions.txt -o sequences/`
**Explanation:** Downloads multiple sequences from accession list.

### Search by organism
**Args:** `ncbitk search -o "Escherichia coli" -n 10 -o results.txt`
**Explanation:** Searches GenBank for E. coli sequences.

### Parse GenBank file
**Args:** `ncbitk parse -i genome.gb -f features -o features.tsv`
**Explanation:** Extracts features from GenBank file.

### Convert to FASTA
**Args:** `ncbitk convert -i genome.gb -f fasta -o genome.fasta`
**Explanation:** Converts GenBank file to FASTA format.