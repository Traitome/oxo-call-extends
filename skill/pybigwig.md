---
name: pybigwig
category: programming
description: pybigwig is a Python extension written in C for quick access to bigWig files for genomic data visualization.
tags: [pybigwig, programming, bigwig, genomic-data]
author: oxo-call-community
source_url: "https://github.com/deeptools/pyBigWig"
---

## Concepts

- **Tool Overview**: pybigwig reads bigWig files.
- **Core Function**: BigWig file access.
- **Algorithm**: Uses libBigWig library.
- **Input Format**: Accepts bigWig files.
- **Output**: Produces signal values.
- **Use Case**: Genomic data visualization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on file integrity.
- **Index Requirement**: Files need indexing.
- **Runtime**: Access may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pybigwig --help`
**Explanation:** Shows available options and usage instructions.

### Extract values
**Args:** `pybigwig extract -i signal.bw -c chr1:1-1000 -o values.txt`
**Explanation:** Extracts signal values from region.

### With parameters
**Args:** `pybigwig extract -i signal.bw -c chr1:1-1000 -p params.yaml -o values.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pybigwig -v extract -i signal.bw -c chr1:1-1000 -o values.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pybigwig -t 4 extract -i signal.bw -c chr1:1-1000 -o values.txt`
**Explanation:** Uses 4 threads for parallel processing.

### List chromosomes
**Args:** `pybigwig list -i signal.bw`
**Explanation:** Lists available chromosomes.

### Generate report
**Args:** `pybigwig extract -i signal.bw -c chr1:1-1000 -o values.txt --report report.html`
**Explanation:** Generates HTML report.