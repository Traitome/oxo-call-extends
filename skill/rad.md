---
name: rad
category: alignment
description: RAD (Read-structure Agnostic Demultiplexer) demultiplexes long-read single-cell RNA-seq data.
tags: [rad, alignment, demultiplexing, single-cell]
author: oxo-call-community
source_url: "https://github.com/indianewok/rad/blob/v0.6.0/README.md"
---

## Concepts

- **Tool Overview**: rad demultiplexes reads.
- **Core Function**: Read demultiplexing.
- **Algorithm**: Uses barcode detection.
- **Input Format**: Accepts long reads.
- **Output**: Produces demultiplexed files.
- **Use Case**: Single-cell analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Barcode Quality**: Affects demultiplexing.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rad --help`
**Explanation:** Shows available options and usage instructions.

### Demultiplex reads
**Args:** `rad demux -i reads.fastq -b barcodes.txt -o output/`
**Explanation:** Demultiplexes long reads.

### With parameters
**Args:** `rad demux -i reads.fastq -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rad -v demux -i reads.fastq -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rad -t 4 demux -i reads.fastq -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### With whitelist
**Args:** `rad demux -i reads.fastq -w whitelist.txt -o output/`
**Explanation:** Uses barcode whitelist.

### Generate report
**Args:** `rad demux -i reads.fastq -o output/ --report report.html`
**Explanation:** Generates HTML report.