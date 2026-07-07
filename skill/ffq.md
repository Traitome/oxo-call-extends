---
name: ffq
category: utility
description: "A command line tool that makes it easier to find sequencing data from the SRA / GEO / ENA."
tags: [ffq, utility, SRA, GEO, ENA, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pachterlab/ffq"
---

## Concepts

- **Tool Overview**: ffq is a command-line tool for finding and downloading sequencing data from SRA, GEO, and ENA repositories.
- **Core Function**: Searches and retrieves metadata and download links for sequencing datasets.
- **Input/Output**: Input: Accession numbers (SRA/GEO/ENA). Output: Metadata, download URLs.
- **Algorithm**: Queries repository APIs for dataset information.
- **Key Features**: Multi-repository search, SRA support, GEO support, ENA support, metadata retrieval, download link generation.
- **Installation**: `conda install -c bioconda ffq`

## Pitfalls

- **Network Access**: Requires internet connection.
- **API Limits**: Repositories may have rate limits.
- **Data Availability**: Dataset must be publicly available.
- **Access Permissions**: Some datasets require special access.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Search SRA
**Args:** `ffq SRR1234567`
**Explanation:** Searches for SRA dataset metadata.

### Search GEO
**Args:** `ffq GSM123456`
**Explanation:** Searches for GEO sample metadata.

### Search ENA
**Args:** `ffq ERR123456`
**Explanation:** Searches for ENA dataset metadata.

### Download links
**Args:** `ffq SRR1234567 --download`
**Explanation:** Gets download links for dataset.

### Output format
**Args:** `ffq SRR1234567 -o metadata.json`
**Explanation:** Saves metadata to JSON file.