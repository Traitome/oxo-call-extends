---
name: sra-human-scrubber
category: qc
description: SRA Human Scrubber - Tool to identify and remove human reads from sequencing data
tags: [sra-human-scrubber, qc, human-reads, privacy, sra]
author: oxo-call-community
source_url: "https://github.com/ncbi/sra-human-scrubber"
---

## Concepts

- **Tool Overview**: sra-human-scrubber (v2.2.1) - A human read removal tool
- **Core Function**: Identifies and removes human reads for SRA submission
- **Input/Output**: Accepts sequencing data; outputs cleaned FASTQ files
- **Algorithm**: Human read identification and removal
- **Installation**: `conda install -c bioconda sra-human-scrubber`
- **Key Features**: Human read removal, privacy protection, SRA compliance

## Pitfalls

- **Input Requirements**: Requires properly formatted sequencing data
- **Read Quality**: Read quality affects identification accuracy
- **Human Genome**: Human genome reference affects identification
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Removal Accuracy**: Accuracy depends on read quality and reference

## Examples

### Display help
**Args:** `sra-human-scrubber --help`
**Explanation:** Shows available options and usage information.

### Basic human read removal
**Args:** `sra-human-scrubber -i reads.fastq -o cleaned_reads.fastq`
**Explanation:** Remove human reads from sequencing data.

### With human genome reference
**Args:** `sra-human-scrubber -i reads.fastq -r human_genome.fasta -o cleaned_reads.fastq`
**Explanation:** Use specific human genome reference.

### With sensitivity
**Args:** `sra-human-scrubber -i reads.fastq -o cleaned_reads.fastq --sensitivity high`
**Explanation:** Set identification sensitivity.

### Multiple files
**Args:** `sra-human-scrubber -i reads1.fastq reads2.fastq -o cleaned_reads.fastq`
**Explanation:** Remove human reads from multiple files.

### Output detailed results
**Args:** `sra-human-scrubber -i reads.fastq -o cleaned_reads.fastq --detailed`
**Explanation:** Output detailed removal information.

### Output statistics
**Args:** `sra-human-scrubber -i reads.fastq -o cleaned_reads.fastq --stats`
**Explanation:** Output removal statistics.

### Generate report
**Args:** `sra-human-scrubber -i reads.fastq -o cleaned_reads.fastq --report`
**Explanation:** Generate removal report.

### With threads
**Args:** `sra-human-scrubber -i reads.fastq -o cleaned_reads.fastq -p 8`
**Explanation:** Use multiple threads for removal.