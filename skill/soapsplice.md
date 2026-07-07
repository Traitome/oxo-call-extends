---
name: soapsplice
category: transcriptomics
description: SOAPsplice - Genome-wide splice junction detection from RNA-seq
tags: [soapsplice, transcriptomics, splice-junctions, rna-seq, splicing]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapsplice.html"
---

## Concepts

- **Tool Overview**: soapsplice (v1.10) - A splice junction detection tool
- **Core Function**: Detects splice junction sites from RNA-seq data
- **Input/Output**: Accepts RNA-seq reads; outputs splice junction predictions
- **Algorithm**: Ab initio detection of splice sites from RNA-seq alignments
- **Installation**: `conda install -c bioconda soapsplice`
- **Key Features**: Splice junction detection, RNA-seq analysis, ab initio method

## Pitfalls

- **Input Requirements**: Requires properly formatted RNA-seq reads
- **Reference Genome**: Requires reference genome for junction detection
- **Read Length**: Short reads may reduce detection accuracy
- **Coverage**: Requires sufficient read coverage at junctions
- **Memory Usage**: Large genomes require significant memory
- **False Positives**: May produce false positives in repetitive regions

## Examples

### Display help
**Args:** `SOAPsplice --help`
**Explanation:** Shows available options and usage information.

### Basic junction detection
**Args:** `SOAPsplice -d reference.fasta -i reads.fastq -o junctions.txt`
**Explanation:** Detect splice junctions from RNA-seq.

### Paired-end detection
**Args:** `SOAPsplice -d reference.fasta -i reads_1.fastq -2 reads_2.fastq -o junctions.txt`
**Explanation:** Detect junctions from paired-end reads.

### With minimum support
**Args:** `SOAPsplice -d reference.fasta -i reads.fastq -o junctions.txt --min-support 5`
**Explanation:** Set minimum read support for junctions.

### Output GFF format
**Args:** `SOAPsplice -d reference.fasta -i reads.fastq -o junctions.gff --gff`
**Explanation:** Output junctions in GFF format.

### With threads
**Args:** `SOAPsplice -d reference.fasta -i reads.fastq -o junctions.txt -p 8`
**Explanation:** Use multiple threads for detection.

### Output statistics
**Args:** `SOAPsplice -d reference.fasta -i reads.fastq -o junctions.txt --stats`
**Explanation:** Output detection statistics.

### Generate report
**Args:** `SOAPsplice -d reference.fasta -i reads.fastq -o junctions.txt --report`
**Explanation:** Generate detection report.