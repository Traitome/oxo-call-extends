---
name: sra-tools
category: sra
description: SRA Toolkit - NCBI SRA data management toolkit and SDK
tags: [sra-tools, sra, ncbi, data-management, toolkit]
author: oxo-call-community
source_url: "https://github.com/ncbi/sra-tools/wiki"
---

## Concepts

- **Tool Overview**: sra-tools (v3.4.1) - NCBI SRA data management toolkit
- **Core Function**: Provides comprehensive tools for SRA data management and analysis
- **Input/Output**: Accepts SRA data; outputs processed data and metadata
- **Algorithm**: SRA data processing and management algorithms
- **Installation**: `conda install -c bioconda sra-tools`
- **Key Features**: SRA management, data download, format conversion

## Pitfalls

- **Input Requirements**: Requires properly configured SRA access
- **Network Access**: Requires network access for SRA data
- **Disk Space**: Large datasets require significant disk space
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on tool configuration
- **Data Integrity**: Data integrity depends on network and storage

## Examples

### Display help
**Args:** `sra-tools --help`
**Explanation:** Shows available options and usage information.

### Basic SRA download
**Args:** `prefetch SRR123456`
**Explanation:** Download SRA data using prefetch.

### Convert to FASTQ
**Args:** `fastq-dump SRR123456.sra`
**Explanation:** Convert SRA to FASTQ format.

### With split files
**Args:** `fastq-dump --split-files SRR123456.sra`
**Explanation:** Split paired-end reads into separate files.

### With quality filtering
**Args:** `fastq-dump --skip-technical SRR123456.sra`
**Explanation:** Skip technical reads during conversion.

### Output detailed results
**Args:** `vdb-dump --details SRR123456.sra`
**Explanation:** Output detailed SRA information.

### Output statistics
**Args:** `sra-stat SRR123456.sra`
**Explanation:** Output SRA statistics.

### Generate report
**Args:** `sra-tools --report SRR123456.sra`
**Explanation:** Generate SRA data report.

### With threads
**Args:** `fastq-dump --threads 8 SRR123456.sra`
**Explanation:** Use multiple threads for conversion.