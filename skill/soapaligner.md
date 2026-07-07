---
name: soapaligner
category: alignment
description: SOAPaligner - Short oligonucleotide alignment tool for high-throughput sequencing
tags: [soapaligner, alignment, short-reads, soap, mapping]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapaligner.html"
---

## Concepts

- **Tool Overview**: soapaligner (v2.21) - A fast short-read alignment tool
- **Core Function**: Aligns short oligonucleotide reads to reference genome
- **Input/Output**: Accepts FASTQ reads; outputs alignment in SOAP/SAM format
- **Algorithm**: Uses efficient indexing for fast short-read alignment
- **Installation**: `conda install -c bioconda soapaligner`
- **Key Features**: Fast alignment, short-read support, SOAP format output

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **Reference Index**: Requires pre-built reference index
- **Read Length**: Designed for specific read length ranges
- **Memory Usage**: Large references require significant memory
- **Output Format**: Multiple output formats available
- **Paired-end**: Paired-end alignment requires specific parameters

## Examples

### Display help
**Args:** `soapaligner --help`
**Explanation:** Shows available options and usage information.

### Build index
**Args:** `2bwt-builder reference.fasta`
**Explanation:** Build reference index for SOAPaligner.

### Basic alignment
**Args:** `soapaligner -D reference.index -i reads.fastq -o aligned.soap`
**Explanation:** Align reads to reference genome.

### Paired-end alignment
**Args:** `soapaligner -D reference.index -a reads_1.fastq -b reads_2.fastq -o aligned.soap`
**Explanation:** Align paired-end reads.

### With quality filter
**Args:** `soapaligner -D reference.index -i reads.fastq -o aligned.soap -q 20`
**Explanation:** Filter by minimum quality score.

### Output SAM format
**Args:** `soapaligner -D reference.index -i reads.fastq -o aligned.sam -s`
**Explanation:** Output alignment in SAM format.

### Set threads
**Args:** `soapaligner -D reference.index -i reads.fastq -o aligned.soap -p 8`
**Explanation:** Use multiple threads for alignment.

### With mismatch tolerance
**Args:** `soapaligner -D reference.index -i reads.fastq -o aligned.soap -m 2`
**Explanation:** Set maximum allowed mismatches.