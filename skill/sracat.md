---
name: sracat
category: sra
description: SRACAT - Tool for extracting unordered read data from SRA files
tags: [sracat, sra, read-extraction, sequencing, ncbi]
author: oxo-call-community
source_url: "https://github.com/lanl/sracat/blob/v0.2/README.md"
---

## Concepts

- **Tool Overview**: sracat (v0.2) - An SRA extraction tool
- **Core Function**: Extracts unordered read data from SRA files
- **Input/Output**: Accepts SRA files; outputs extracted read data
- **Algorithm**: SRA file parsing and read extraction
- **Installation**: `conda install -c bioconda sracat`
- **Key Features**: SRA extraction, read data, unordered extraction

## Pitfalls

- **Input Requirements**: Requires properly formatted SRA files
- **SRA Format**: SRA format affects extraction accuracy
- **Read Order**: Unordered extraction may affect downstream analysis
- **Memory Usage**: Large SRA files require significant memory
- **Output Format**: Output format depends on configuration
- **Extraction Speed**: Speed depends on file size and settings

## Examples

### Display help
**Args:** `sracat --help`
**Explanation:** Shows available options and usage information.

### Basic SRA extraction
**Args:** `sracat -i data.sra -o extracted_reads.fastq`
**Explanation:** Extract reads from SRA file.

### With quality filtering
**Args:** `sracat -i data.sra -o extracted_reads.fastq --quality-filter`
**Explanation:** Enable quality filtering during extraction.

### With read count
**Args:** `sracat -i data.sra -o extracted_reads.fastq --count 10000`
**Explanation:** Extract specific number of reads.

### Multiple SRA files
**Args:** `sracat -i data1.sra data2.sra -o extracted_reads.fastq`
**Explanation:** Extract from multiple SRA files.

### Output detailed results
**Args:** `sracat -i data.sra -o extracted_reads.fastq --detailed`
**Explanation:** Output detailed extraction information.

### Output statistics
**Args:** `sracat -i data.sra -o extracted_reads.fastq --stats`
**Explanation:** Output extraction statistics.

### Generate report
**Args:** `sracat -i data.sra -o extracted_reads.fastq --report`
**Explanation:** Generate extraction report.

### With threads
**Args:** `sracat -i data.sra -o extracted_reads.fastq -p 8`
**Explanation:** Use multiple threads for extraction.