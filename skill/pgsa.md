---
name: pgsa
category: population-genomics
description: pgsa builds compact suffix array indices for sequencing reads.
tags: [pgsa, population-genomics, index, suffix-array]
author: oxo-call-community
source_url: "http://sun.aei.polsl.pl/pgsa/"
---

## Concepts

- **Tool Overview**: pgsa builds suffix array indices.
- **Core Function**: Creates compact read indices.
- **Algorithm**: Uses pseudogenome suffix arrays.
- **Input Format**: Accepts sequencing read files.
- **Output**: Produces compact index structures.
- **Use Case**: Read indexing, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large read sets require memory.
- **Index Quality**: Results depend on read quality.
- **Index Size**: May require significant storage.
- **Runtime**: Indexing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgsa --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `pgsa -i reads.fastq -o index.pgsa`
**Explanation:** Builds suffix array index.

### With parameters
**Args:** `pgsa -i reads.fastq -p params.yaml -o index.pgsa`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pgsa -v -i reads.fastq -o index.pgsa`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgsa -t 4 -i reads.fastq -o index.pgsa`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgsa -i reads.fastq -o index.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `pgsa -i reads.fastq -o index.pgsa --report report.html`
**Explanation:** Generates HTML report.