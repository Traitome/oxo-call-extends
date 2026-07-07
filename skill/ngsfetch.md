---
name: ngsfetch
category: utility
description: NGSfetch retrieves SRA metadata and FASTQ files efficiently using ffq and aria2c.
tags: [ngsfetch, utility, sra, fastq-download]
author: oxo-call-community
source_url: "https://github.com/NaotoKubota/ngsfetch"
---

## Concepts

- **Tool Overview**: NGSfetch downloads sequencing data from SRA/ENA databases.
- **Core Function**: Fetches metadata and FASTQ files efficiently.
- **Algorithm**: Uses ffq for metadata retrieval and aria2c for parallel downloads.
- **Input Format**: Accepts SRA/ENA accession numbers.
- **Output**: Produces FASTQ files and metadata reports.
- **Use Case**: Data retrieval, reproducibility, and pipeline automation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Access**: Requires internet connection.
- **Download Limits**: May be subject to NCBI download limits.
- **File Size**: Large datasets require storage.
- **Authentication**: Some databases require authentication.
- **Rate Limiting**: May trigger rate limiting.

## Examples

### Display help
**Args:** `ngsfetch --help`
**Explanation:** Shows available options and usage instructions.

### Download FASTQ
**Args:** `ngsfetch SRR1234567`
**Explanation:** Downloads FASTQ files for SRA accession.

### Download multiple accessions
**Args:** `ngsfetch SRR1234567 SRR1234568 SRR1234569`
**Explanation:** Downloads multiple SRA accessions.

### Download with metadata
**Args:** `ngsfetch SRR1234567 --metadata`
**Explanation:** Downloads FASTQ and metadata.

### Specify output directory
**Args:** `ngsfetch SRR1234567 -o data/`
**Explanation:** Saves files to specified directory.

### Resume download
**Args:** `ngsfetch SRR1234567 --resume`
**Explanation:** Resumes interrupted download.

### Dry run
**Args:** `ngsfetch SRR1234567 --dry-run`
**Explanation:** Shows what would be downloaded without downloading.