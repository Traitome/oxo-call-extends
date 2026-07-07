---
name: readucks
category: utility
description: Readucks is a simple demultiplexer for nanopore reads based on barcode sequences.
tags: [readucks, utility, demultiplexing, nanopore]
author: oxo-call-community
source_url: "https://github.com/artic-network/readucks"
---

## Concepts

- **Tool Overview**: readucks demultiplexes reads.
- **Core Function**: Read demultiplexing.
- **Algorithm**: Uses barcode methods.
- **Input Format**: Accepts nanopore reads.
- **Output**: Produces demultiplexed reads.
- **Use Case**: Nanopore sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Barcode Quality**: Affects demultiplexing.
- **Parameters**: Must be configured.
- **Runtime**: Demultiplexing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `readucks --help`
**Explanation:** Shows available options and usage instructions.

### Demultiplex reads
**Args:** `readucks demultiplex -i reads.fastq -b barcodes.txt -o output_dir/`
**Explanation:** Demultiplexes nanopore reads.

### With parameters
**Args:** `readucks demultiplex -i reads.fastq -p params.yaml -o output_dir/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `readucks -v demultiplex -i reads.fastq -o output_dir/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `readucks -t 4 demultiplex -i reads.fastq -o output_dir/`
**Explanation:** Uses 4 threads for parallel processing.

### With barcode file
**Args:** `readucks demultiplex -i reads.fastq -b barcodes.txt -o output_dir/`
**Explanation:** Uses barcode sequences.

### Generate report
**Args:** `readucks demultiplex -i reads.fastq -o output_dir/ --report report.html`
**Explanation:** Generates HTML report.