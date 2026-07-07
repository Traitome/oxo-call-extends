---
name: ena-dl
category: utility
description: "A tool to download FASTQs associated with Study, Experiment, or Run accessions."
tags: [ena-dl, utility, ENA, FASTQ-download, sequencing-data]
author: oxo-call-community
source_url: "https://github.com/rpetit3/ena-dl"
---

## Concepts

- **Tool Overview**: ena-dl is a command-line tool for downloading FASTQ files from the European Nucleotide Archive (ENA) using study, experiment, or run accessions.
- **Core Function**: Automates the download of sequencing data from ENA, supporting various accession types and batch operations.
- **Input/Output**: Input: ENA accession numbers (Study, Experiment, or Run). Output: FASTQ files (paired or single-end), download reports.
- **Algorithm**: Queries ENA API to retrieve file locations and downloads data using parallel connections for speed.
- **Key Features**: Multi-accession support, parallel downloading, resume capability, progress tracking, file validation, batch processing.
- **Installation**: `conda install -c bioconda ena-dl`

## Pitfalls

- **Internet Speed**: Download speed depends on network connection.
- **Storage Space**: Large datasets require significant disk space.
- **ENA Availability**: Dependent on ENA service availability.
- **File Validation**: Downloaded files should be validated for integrity.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Download single run
**Args:** `ena-dl ERR123456`
**Explanation:** Downloads FASTQ files for specified run accession.

### Download study data
**Args:** `ena-dl PRJEB12345`
**Explanation:** Downloads all FASTQ files associated with a study.

### Parallel downloading
**Args:** `ena-dl ERR123456 -t 8`
**Explanation:** Uses 8 threads for parallel downloading.

### Resume interrupted download
**Args:** `ena-dl ERR123456 --resume`
**Explanation:** Resumes interrupted download if partial files exist.

### Batch download from file
**Args:** `ena-dl -i accessions.txt`
**Explanation:** Downloads data for accessions listed in file.