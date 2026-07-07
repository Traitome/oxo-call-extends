---
name: spechla
category: immunogenetics
description: SpecHLA - Full-resolution HLA typing from sequencing data
tags: [spechla, immunogenetics, hla-typing, sequencing, immunology]
author: oxo-call-community
source_url: "https://github.com/deepomicslab/SpecHLA"
---

## Concepts

- **Tool Overview**: spechla (v1.0.10) - A high-resolution HLA typing tool
- **Core Function**: Performs full-resolution HLA typing from sequencing data
- **Input/Output**: Accepts sequencing data; outputs HLA type assignments
- **Algorithm**: Deep learning-based HLA typing
- **Installation**: `conda install -c bioconda spechla`
- **Key Features**: HLA typing, full-resolution, deep learning

## Pitfalls

- **Input Requirements**: Requires properly formatted sequencing data
- **Read Quality**: Read quality affects typing accuracy
- **HLA Database**: Requires comprehensive HLA database
- **Memory Usage**: Large sequencing datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Typing Accuracy**: Accuracy depends on data quality and coverage

## Examples

### Display help
**Args:** `spechla --help`
**Explanation:** Shows available options and usage information.

### Basic HLA typing
**Args:** `spechla -i reads.fastq -o hla_types.txt`
**Explanation:** Perform HLA typing from reads.

### With reference genome
**Args:** `spechla -i reads.fastq -r reference.fasta -o hla_types.txt`
**Explanation:** Use reference genome for typing.

### With HLA database
**Args:** `spechla -i reads.fastq -d hla_db/ -o hla_types.txt`
**Explanation:** Use specific HLA database.

### Full-resolution typing
**Args:** `spechla -i reads.fastq -o hla_types.txt --full-resolution`
**Explanation:** Perform full-resolution typing.

### Output detailed results
**Args:** `spechla -i reads.fastq -o hla_types.txt --detailed`
**Explanation:** Output detailed typing information.

### Output statistics
**Args:** `spechla -i reads.fastq -o hla_types.txt --stats`
**Explanation:** Output typing statistics.

### Generate report
**Args:** `spechla -i reads.fastq -o hla_types.txt --report`
**Explanation:** Generate typing report.

### With threads
**Args:** `spechla -i reads.fastq -o hla_types.txt -p 8`
**Explanation:** Use multiple threads for typing.