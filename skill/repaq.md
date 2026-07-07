---
name: repaq
category: formatting
description: Repaq is a fast lossless FASTQ compressor with ultra-high compression ratio for sequencing data.
tags: [repaq, formatting, fastq-compression, sequencing-data]
author: oxo-call-community
source_url: "https://github.com/OpenGene/repaq/blob/v0.5.1/README.md"
---

## Concepts

- **Tool Overview**: repaq compresses FASTQ.
- **Core Function**: Lossless compression.
- **Algorithm**: Uses specialized methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces compressed files.
- **Use Case**: Data storage.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Compression Ratio**: Affects performance.
- **Parameters**: Must be configured.
- **Runtime**: Compression may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `repaq --help`
**Explanation:** Shows available options and usage instructions.

### Compress FASTQ
**Args:** `repaq compress -i reads.fastq -o reads.repaq`
**Explanation:** Compresses FASTQ file.

### Decompress FASTQ
**Args:** `repaq decompress -i reads.repaq -o reads.fastq`
**Explanation:** Decompresses repaq file.

### With parameters
**Args:** `repaq compress -i reads.fastq -p high -o reads.repaq`
**Explanation:** Uses high compression mode.

### Verbose mode
**Args:** `repaq -v compress -i reads.fastq -o reads.repaq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `repaq -t 4 compress -i reads.fastq -o reads.repaq`
**Explanation:** Uses 4 threads for parallel processing.

### Check integrity
**Args:** `repaq check -i reads.repaq`
**Explanation:** Verifies file integrity.