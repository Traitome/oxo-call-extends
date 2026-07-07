---
name: entrez-direct
category: annotation
description: "Entrez Direct (EDirect) - Access to NCBI's Entrez databases"
tags: [entrez-direct, annotation, NCBI, Entrez, data-retrieval]
author: oxo-call-community
source_url: "https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/25.3.20260410/README"
---

## Concepts

- **Tool Overview**: Entrez Direct (EDirect) is a suite of command-line tools that provide direct access to NCBI's Entrez databases, allowing users to search, retrieve, and analyze biological data from a Unix terminal.
- **Core Function**: Enables programmatic access to NCBI databases including PubMed, GenBank, Gene, SNP, Structure, and many others.
- **Input/Output**: Input: Search terms, accession numbers, query parameters. Output: Sequence data, literature citations, gene information, XML/JSON/FASTA formats.
- **Algorithm**: Interfaces with NCBI's E-Utilities API to submit queries and retrieve results, with support for piping between commands.
- **Key Features**: Multi-database access, complex query construction, batch processing, format conversion, integration with Unix pipelines, automated retrieval.
- **Installation**: `conda install -c bioconda entrez-direct`

## Pitfalls

- **API Rate Limits**: NCBI imposes rate limits on API requests.
- **Internet Connection**: Requires stable internet connection.
- **Query Complexity**: Complex queries may require careful construction.
- **Result Volume**: Large result sets may require pagination or filtering.
- **Data Format**: Understanding output formats requires familiarity with NCBI conventions.

## Examples

### Search PubMed
**Args:** `esearch -db pubmed -query "CRISPR" | efetch -format xml > results.xml`
**Explanation:** Searches PubMed for CRISPR-related articles.

### Download sequence
**Args:** `efetch -db nucleotide -id NM_000014 -format fasta > sequence.fasta`
**Explanation:** Downloads FASTA sequence for specified accession.

### Batch retrieval
**Args:** `esearch -db gene -query "BRCA1" | elink -target snp | efetch -format tab > snps.txt`
**Explanation:** Retrieves SNPs associated with BRCA1 gene.

### Gene information
**Args:** `efetch -db gene -id 672 -format gene_table > gene_info.txt`
**Explanation:** Retrieves gene information for BRCA1.

### Literature search
**Args:** `esearch -db pubmed -query "cancer AND immunotherapy" | efetch -format abstract > abstracts.txt`
**Explanation:** Retrieves abstracts for cancer immunotherapy papers.