---
name: enabrowsertools
category: utility
description: "enaBrowserTools is a set of scripts that interface with the ENA web services to download data from ENA easily."
tags: [enabrowsertools, utility, ENA, data-download, sequence-data]
author: oxo-call-community
source_url: "https://github.com/enasequence/enaBrowserTools"
---

## Concepts

- **Tool Overview**: enaBrowserTools is a collection of Python scripts that provide easy access to the European Nucleotide Archive (ENA) web services for downloading sequencing data.
- **Core Function**: Enables users to search and download sequence data, metadata, and related files from the ENA database.
- **Input/Output**: Input: Accession numbers, search terms, or query parameters. Output: Sequence files (FASTA, FASTQ), metadata files, analysis reports.
- **Algorithm**: Interfaces with ENA REST API to search and retrieve data based on user queries.
- **Key Features**: ENA database access, batch downloads, metadata retrieval, search filters, support for various data types, progress tracking.
- **Installation**: `conda install -c bioconda enabrowsertools`

## Pitfalls

- **Internet Connection**: Requires stable internet connection for data download.
- **ENA Service Availability**: Dependent on ENA web service availability.
- **Data Volume**: Large datasets may require significant storage space.
- **Authentication**: Some datasets may require authentication.
- **Version Compatibility**: API changes may affect tool functionality.

## Examples

### Download by accession
**Args:** `enaDataGet -f fastq ERR123456`
**Explanation:** Downloads FASTQ files for the specified ENA run accession.

### Download study data
**Args:** `enaDataGet -f fastq PRJEB12345`
**Explanation:** Downloads all FASTQ files associated with a study.

### Search for data
**Args:** `enaSearch -t study -q "human" > results.txt`
**Explanation:** Searches ENA for studies related to "human".

### Download metadata
**Args:** `enaDataGet -f xml ERR123456`
**Explanation:** Downloads XML metadata for the specified accession.

### Batch download
**Args:** `enaDataGet -f fastq -i accessions.txt`
**Explanation:** Downloads data for multiple accessions listed in file.