---
name: soapdenovo2-prepare
category: assembly
description: SOAPdenovo2 Prepare - Data preparation module for scaffold assembly
tags: [soapdenovo2-prepare, assembly, scaffold, preparation, soapdenovo]
author: oxo-call-community
source_url: "https://github.com/aquaskyline/SOAPdenovo2"
---

## Concepts

- **Tool Overview**: soapdenovo2-prepare (v2.0) - Data preparation for scaffold assembly
- **Core Function**: Prepares contig data for scaffold assembly in SOAPdenovo2
- **Input/Output**: Accepts contigs and reads; outputs prepared data for scaffolding
- **Algorithm**: Processes contigs and read information for scaffold construction
- **Installation**: `conda install -c bioconda soapdenovo2-prepare`
- **Key Features**: Data preparation, scaffold support, assembly workflow

## Pitfalls

- **Input Requirements**: Requires properly formatted contigs and reads
- **Contig Quality**: Quality of contigs affects scaffold preparation
- **Read Coverage**: Requires sufficient read coverage for scaffolding
- **Memory Usage**: Large assemblies require significant memory
- **Output Format**: Output must match SOAPdenovo2 format requirements
- **Configuration**: Requires proper configuration for preparation

## Examples

### Display help
**Args:** `SOAPdenovo2-Prepare --help`
**Explanation:** Shows available options and usage information.

### Basic preparation
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -r reads.fastq -o prepared_data/`
**Explanation:** Prepare data for scaffold assembly.

### With config file
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -s config.txt -o prepared_data/`
**Explanation:** Use configuration file for preparation.

### Paired-end preparation
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -p reads_1.fastq reads_2.fastq -o prepared_data/`
**Explanation:** Prepare paired-end read data.

### With threads
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -r reads.fastq -o prepared_data/ -p 8`
**Explanation:** Use multiple threads for preparation.

### Output statistics
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -r reads.fastq -o prepared_data/ --stats`
**Explanation:** Output preparation statistics.

### Generate report
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -r reads.fastq -o prepared_data/ --report`
**Explanation:** Generate preparation report.

### Validate input
**Args:** `SOAPdenovo2-Prepare -c contigs.fasta -r reads.fastq -o prepared_data/ --validate`
**Explanation:** Validate input data before preparation.