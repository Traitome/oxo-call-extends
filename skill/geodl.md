---
name: geodl
category: data-download
description: geoDL - Download FASTQ files from GEO-NCBI and ENA with ease.
tags: [geodl, data-download, GEO, ENA, FASTQ]
author: oxo-call-community
source_url: "https://github.com/jduc/geoDL"
---

## Concepts
- **Data Download**: Downloads sequencing data from public repositories.
- **GEO Access**: Accesses GEO-NCBI data.
- **ENA Access**: Accesses ENA data.
- **FASTQ Retrieval**: Retrieves FASTQ files.
- **Batch Processing**: Processes multiple accessions.

## Pitfalls
- **Network Dependency**: Requires network connectivity.
- **Data Volume**: Large files require storage space.
- **Rate Limits**: May hit download rate limits.
- **Authentication**: Some resources require authentication.
- **File Integrity**: Verify downloaded files.

## Examples
### Download FASTQ from GEO
**Args:** `geodl -g GSE12345 -o ./fastq/`
**Explanation:** Downloads FASTQ files from GEO series.

### Download from ENA
**Args:** `geodl -e ERR123456 -o ./fastq/`
**Explanation:** Downloads FASTQ file from ENA.

### Batch download
**Args:** `geodl -l accessions.txt -o ./fastq/`
**Explanation:** Downloads multiple accessions from list.

### With authentication
**Args:** `geodl -g GSE12345 -u username -p password -o ./fastq/`
**Explanation:** Downloads with authentication.

### Verify downloads
**Args:** `geodl -g GSE12345 -c -o ./fastq/`
**Explanation:** Downloads and verifies file integrity.