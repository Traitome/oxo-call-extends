---
name: atlas-fastq-provider
category: utility
description: Atlas Fastq Provider - Package for providing FASTQs via download or file system linking
tags: [fastq-management, download, file-linking, data-retrieval]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/atlas-fastq-provider"
---

## Concepts

- **Tool Overview**: Provides FASTQ files for Expression Atlas pipelines by downloading from ENA/SRA or linking from local file systems.

- **Multiple Sources**: Supports downloading from public repositories (ENA, SRA) or linking existing files from local storage.

- **Automation**: Designed for automated pipeline integration, handling authentication, retries, and error handling.

- **Metadata Integration**: Works with Expression Atlas metadata to identify and retrieve appropriate FASTQ files.

## Pitfalls

- **Network Dependencies**: Downloads require stable internet connection and access to public repositories.

- **Storage Requirements**: Large datasets require significant disk space. Plan storage before initiating downloads.

- **Access Restrictions**: Some datasets may have access restrictions requiring authentication or special permissions.

- **File Integrity**: Always verify downloaded files using checksums to detect corruption.

## Examples

### Download FASTQ by accession
**Args:** `atlas-fastq-provider --accession SRR123456 --output fastqs/`
**Explanation:** Downloads FASTQ files for specified SRA accession to output directory.

### Link existing files
**Args:** `atlas-fastq-provider --link --source /data/fastqs/ --accession SRR123456 --output linked/`
**Explanation:** Creates symbolic links to existing FASTQ files instead of downloading.

### Batch download from metadata
**Args:** `atlas-fastq-provider --metadata experiment.tsv --output fastqs/`
**Explanation:** Downloads all FASTQ files referenced in metadata file.

### Specify download threads
**Args:** `atlas-fastq-provider --accession SRR123456 --threads 4 --output fastqs/`
**Explanation:** Uses 4 parallel threads for faster download of large files.

### Verify checksums
**Args:** `atlas-fastq-provider --accession SRR123456 --verify-checksum --output fastqs/`
**Explanation:** Verifies MD5 checksums after download to ensure file integrity.
