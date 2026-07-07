---
name: pydemult
category: formatting
description: pydemult performs streamed and parallel demultiplexing of FASTQ files in Python.
tags: [pydemult, formatting, fastq, demultiplexing]
author: oxo-call-community
source_url: "https://github.com/jenzopr/pydemult"
---

## Concepts

- **Tool Overview**: pydemult demultiplexes FASTQ files.
- **Core Function**: Parallel FASTQ demultiplexing.
- **Algorithm**: Uses streaming processing.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces demultiplexed reads.
- **Use Case**: Sequencing data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Barcode Mismatches**: May affect accuracy.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pydemult --help`
**Explanation:** Shows available options and usage instructions.

### Demultiplex FASTQ
**Args:** `pydemult -i reads.fastq -b barcodes.txt -o output/`
**Explanation:** Demultiplexes FASTQ file by barcodes.

### With parameters
**Args:** `pydemult -i reads.fastq -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pydemult -v -i reads.fastq -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pydemult -t 4 -i reads.fastq -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### Paired-end reads
**Args:** `pydemult -i1 reads_R1.fastq -i2 reads_R2.fastq -o output/`
**Explanation:** Processes paired-end reads.

### Generate report
**Args:** `pydemult -i reads.fastq -o output/ --report report.html`
**Explanation:** Generates HTML report.