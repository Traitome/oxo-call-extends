---
name: sortmerna
category: qc
description: SortMeRNA - Biological sequence filtering and OTU-picking for NGS reads
tags: [sortmerna, qc, filtering, otu-picking, rRNA, metagenomics]
author: oxo-call-community
source_url: "https://sortmerna.readthedocs.io"
---

## Concepts

- **Tool Overview**: sortmerna (v4.3.7) - A sequence filtering and OTU-picking tool
- **Core Function**: Filters, maps, and picks OTUs from NGS reads
- **Input/Output**: Accepts FASTQ reads; outputs filtered reads and OTUs
- **Algorithm**: Uses rRNA databases for filtering and clustering
- **Installation**: `conda install -c bioconda sortmerna`
- **Key Features**: rRNA filtering, OTU-picking, metagenomics analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **Database**: Requires rRNA database for filtering
- **Memory Usage**: Large FASTQ files require significant memory
- **OTU Clustering**: OTU clustering parameters affect results
- **Output Format**: Output format depends on analysis type
- **Read Length**: Read length affects filtering accuracy

## Examples

### Display help
**Args:** `sortmerna --help`
**Explanation:** Shows available options and usage information.

### Basic rRNA filtering
**Args:** `sortmerna -i reads.fastq -r rRNA_databases/ -o filtered/`
**Explanation:** Filter rRNA reads from FASTQ.

### With OTU picking
**Args:** `sortmerna -i reads.fastq -r rRNA_databases/ -o filtered/ --otu`
**Explanation:** Perform OTU picking on filtered reads.

### With alignment output
**Args:** `sortmerna -i reads.fastq -r rRNA_databases/ -o filtered/ --aligned aligned.sam`
**Explanation:** Output aligned reads in SAM format.

### With multiple databases
**Args:** `sortmerna -i reads.fastq -r db1.fasta db2.fasta -o filtered/`
**Explanation:** Use multiple rRNA databases.

### With threads
**Args:** `sortmerna -i reads.fastq -r rRNA_databases/ -o filtered/ -p 8`
**Explanation:** Use multiple threads for filtering.

### Output statistics
**Args:** `sortmerna -i reads.fastq -r rRNA_databases/ -o filtered/ --stats`
**Explanation:** Output filtering statistics.

### Generate report
**Args:** `sortmerna -i reads.fastq -r rRNA_databases/ -o filtered/ --report`
**Explanation:** Generate filtering report.