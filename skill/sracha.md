---
name: sracha
category: sra
description: SRACHA - Fast parallel SRA downloader and streaming FASTQ converter
tags: [sracha, sra, downloader, fastq, parallel]
author: oxo-call-community
source_url: "https://github.com/rnabioco/sracha-rs#readme"
---

## Concepts

- **Tool Overview**: sracha (v0.1.8) - An SRA download and conversion tool
- **Core Function**: Fast parallel SRA downloader and streaming FASTQ converter
- **Input/Output**: Accepts SRA accessions; outputs FASTQ files
- **Algorithm**: Parallel download and streaming conversion
- **Installation**: `conda install -c bioconda sracha`
- **Key Features**: SRA download, FASTQ conversion, parallel processing

## Pitfalls

- **Input Requirements**: Requires valid SRA accession numbers
- **Network Speed**: Network speed affects download speed
- **Disk Space**: Large datasets require significant disk space
- **Memory Usage**: Parallel processing requires significant memory
- **Output Format**: Output format depends on configuration
- **Download Reliability**: Network issues may affect download

## Examples

### Display help
**Args:** `sracha --help`
**Explanation:** Shows available options and usage information.

### Basic SRA download and conversion
**Args:** `sracha -i SRR123456 -o output.fastq`
**Explanation:** Download SRA and convert to FASTQ.

### With parallel downloads
**Args:** `sracha -i SRR123456 -o output.fastq --parallel 4`
**Explanation:** Set number of parallel downloads.

### With quality filtering
**Args:** `sracha -i SRR123456 -o output.fastq --quality-filter`
**Explanation:** Enable quality filtering during conversion.

### Multiple accessions
**Args:** `sracha -i SRR123456 SRR123457 -o output.fastq`
**Explanation:** Download and convert multiple SRA accessions.

### Output detailed results
**Args:** `sracha -i SRR123456 -o output.fastq --detailed`
**Explanation:** Output detailed download information.

### Output statistics
**Args:** `sracha -i SRR123456 -o output.fastq --stats`
**Explanation:** Output download statistics.

### Generate report
**Args:** `sracha -i SRR123456 -o output.fastq --report`
**Explanation:** Generate download report.

### With streaming
**Args:** `sracha -i SRR123456 -o output.fastq --streaming`
**Explanation:** Enable streaming conversion.