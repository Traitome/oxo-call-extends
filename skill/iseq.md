---
name: iseq
category: data-acquisition
description: Integrated tool to fetch public sequencing data from GSA, SRA, ENA, and DDBJ databases
tags: [iseq, sequencing-data, SRA, ENA, GSA, DDBJ]
author: oxo-call-community
source_url: "https://github.com/BioOmics/iSeq"
---

## Concepts

- **Tool Overview**: iSeq (v1.9.8) - A Bash script for downloading sequencing data and metadata from multiple public databases
- **Multi-database Support**: Simultaneous retrieval from GSA, SRA, ENA, and DDBJ databases
- **Accession Formats**: Handles over 25 different accession formats including Project, Study, Sample, Experiment, and Run
- **Advanced Features**: Aspera downloads, parallel downloads, multi-threaded processing, FASTQ merging
- **Integrity Verification**: Automatic file validation with MD5 checksums
- **Metadata Retrieval**: Comprehensive metadata extraction for each dataset

## Pitfalls

- **Network Dependencies**: Requires stable internet connection; may fail with poor connectivity
- **Database Rate Limits**: Some databases impose rate limits on API requests
- **Aspera Configuration**: Aspera downloads require separate installation and configuration
- **Large Datasets**: Downloading large sequencing datasets requires significant storage space
- **Accession Format**: Incorrect accession formats may cause retrieval failures
- **SRA Toolkit Dependency**: SRA file conversion requires SRA Toolkit installation

## Examples

### Download by project accession
**Args:** `iseq -i PRJNA211801`
**Explanation:** Downloads all sequencing data associated with the specified project.

### Download with metadata
**Args:** `iseq -i SRR1234567 -m`
**Explanation:** Downloads sequencing data and extracts associated metadata.

### Parallel downloads
**Args:** `iseq -i PRJEB37513 -p 4`
**Explanation:** Downloads data using 4 parallel connections for faster transfer.

### Convert to FASTQ
**Args:** `iseq -i SRR9876543 -q`
**Explanation:** Downloads SRA file and converts it to FASTQ format.

### Use Aspera for high-speed transfer
**Args:** `iseq -i ERP120836 -a`
**Explanation:** Uses Aspera protocol for accelerated data transfer from ENA.

### Merge paired-end files
**Args:** `iseq -i ERX4009132 -e`
**Explanation:** Merges multiple FASTQ files from the same experiment into single files.