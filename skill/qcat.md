---
name: qcat
category: qc
description: Qcat is a Python command-line tool for demultiplexing Oxford Nanopore reads from FASTQ files.
tags: [qcat, qc, fastq, nanopore]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/qcat"
---

## Concepts

- **Tool Overview**: qcat demultiplexes nanopore reads.
- **Core Function**: Read demultiplexing.
- **Algorithm**: Uses barcode matching.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces demultiplexed reads.
- **Use Case**: Nanopore sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Barcode Quality**: Affects demultiplexing.
- **Adapter Sequences**: Must be present.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qcat --help`
**Explanation:** Shows available options and usage instructions.

### Demultiplex reads
**Args:** `qcat demultiplex -i reads.fastq -o output/`
**Explanation:** Demultiplexes nanopore reads.

### With parameters
**Args:** `qcat demultiplex -i reads.fastq -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qcat -v demultiplex -i reads.fastq -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qcat -t 4 demultiplex -i reads.fastq -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### Specific barcode
**Args:** `qcat demultiplex -i reads.fastq -b barcode01 -o output/`
**Explanation:** Extracts specific barcode.

### Generate report
**Args:** `qcat demultiplex -i reads.fastq -o output/ --report report.html`
**Explanation:** Generates HTML report.