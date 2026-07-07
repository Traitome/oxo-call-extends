---
name: fastq-dl
category: utility
description: "A tool to download FASTQs associated with Study, Experiment, or Run accessions."
tags: [fastq-dl, utility, FASTQ, download, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rpetit3/fastq-dl"
---

## Concepts

- **Tool Overview**: fastq-dl is a tool for downloading FASTQ files associated with SRA Study, Experiment, or Run accessions from NCBI.
- **Core Function**: Downloads sequencing data from NCBI SRA using accession numbers.
- **Input/Output**: Input: SRA accession numbers. Output: FASTQ files.
- **Algorithm**: Uses NCBI SRA API to fetch and download sequencing data.
- **Key Features**: Batch downloading, SRA accession support, automatic file naming, progress tracking, resume support.
- **Installation**: `conda install -c bioconda fastq-dl`

## Pitfalls

- **Network Issues**: Requires stable internet connection.
- **Data Availability**: Depends on NCBI SRA availability.
- **Storage Requirements**: Large files require significant disk space.
- **Download Limits**: NCBI may have download rate limits.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Download single run
**Args:** `fastq-dl -a SRR1234567 -o output/`
**Explanation:** Downloads FASTQ for single SRA run.

### Download multiple accessions
**Args:** `fastq-dl -a SRR1234567 SRR1234568 -o output/`
**Explanation:** Downloads FASTQ for multiple SRA runs.

### From study accession
**Args:** `fastq-dl -a SRP123456 -o output/`
**Explanation:** Downloads all runs in a study.

### Resume download
**Args:** `fastq-dl -a SRR1234567 -o output/ --resume`
**Explanation:** Resumes interrupted download.

### Specify threads
**Args:** `fastq-dl -a SRR1234567 -o output/ -t 8`
**Explanation:** Uses 8 threads for faster download.