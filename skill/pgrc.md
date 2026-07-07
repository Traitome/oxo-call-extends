---
name: pgrc
category: formatting
description: pgrc compresses DNA streams in FASTQ datasets.
tags: [pgrc, formatting, compression, fastq]
author: oxo-call-community
source_url: "https://github.com/kowallus/PgRC"
---

## Concepts

- **Tool Overview**: pgrc compresses FASTQ data.
- **Core Function**: Compresses DNA sequence streams.
- **Algorithm**: Uses specialized DNA compression.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces compressed DNA streams.
- **Use Case**: Data compression, storage optimization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Compression Ratio**: May vary with sequence quality.
- **Data Integrity**: Requires proper decompression.
- **Runtime**: Compression may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgrc --help`
**Explanation:** Shows available options and usage instructions.

### Compress FASTQ
**Args:** `pgrc -i input.fastq -o output.pgrc`
**Explanation:** Compresses FASTQ DNA stream.

### With level
**Args:** `pgrc -i input.fastq -l 9 -o output.pgrc`
**Explanation:** Uses maximum compression level.

### Verbose mode
**Args:** `pgrc -v -i input.fastq -o output.pgrc`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgrc -t 4 -i input.fastq -o output.pgrc`
**Explanation:** Uses 4 threads for parallel processing.

### Decompress
**Args:** `pgrc -d -i input.pgrc -o output.fastq`
**Explanation:** Decompresses pgrc file.

### Generate report
**Args:** `pgrc -i input.fastq -o output.pgrc --report report.html`
**Explanation:** Generates HTML report.