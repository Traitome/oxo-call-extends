---
name: get_fasta_info
category: sequence-analysis
description: get_fasta_info - Get fast info on fasta and fastq files.
tags: [get_fasta_info, sequence-analysis, FASTA, FASTQ, quality-control]
author: oxo-call-community
source_url: "https://github.com/nylander/get_fasta_info"
---

## Concepts
- **Sequence Analysis**: Analyzes FASTA and FASTQ files.
- **Quality Control**: Provides QC metrics for sequencing data.
- **Statistics Generation**: Generates sequence statistics.
- **Batch Processing**: Processes multiple sequence files.
- **Format Detection**: Detects and handles different formats.

## Pitfalls
- **File Format**: Requires correct input format.
- **Compressed Files**: May require decompression first.
- **Large Files**: May require memory optimization.
- **Encoding Issues**: May encounter encoding problems.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Get FASTA info
**Args:** `get_fasta_info -i sequence.fasta -o stats.txt`
**Explanation:** Generates statistics for FASTA file.

### Get FASTQ info
**Args:** `get_fastq_info -i reads.fastq -o stats.txt`
**Explanation:** Generates statistics for FASTQ file.

### Batch processing
**Args:** `get_fasta_info -l files.txt -o ./stats/`
**Explanation:** Processes multiple sequence files.

### Detailed output
**Args:** `get_fasta_info -i sequence.fasta -d -o stats.txt`
**Explanation:** Generates detailed statistics.

### Generate report
**Args:** `get_fasta_info -i sequence.fasta -r -o report.html`
**Explanation:** Generates HTML report.