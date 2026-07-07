---
name: purge_dups
category: assembly
description: purge_dups removes haplotigs and overlaps from genome assemblies based on read depth analysis.
tags: [purge_dups, assembly, haplotigs, duplicate-removal]
author: oxo-call-community
source_url: "https://github.com/dfguan/purge_dups"
---

## Concepts

- **Tool Overview**: purge_dups purges assembly duplicates.
- **Core Function**: Haplotig removal.
- **Algorithm**: Uses read depth analysis.
- **Input Format**: Accepts assembly FASTA files.
- **Output**: Produces purged assembly.
- **Use Case**: Genome assembly polishing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Data Quality**: Results depend on input quality.
- **Depth Threshold**: Affects purging accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `purge_dups --help`
**Explanation:** Shows available options and usage instructions.

### Purge duplicates
**Args:** `purge_dups -i assembly.fasta -c coverage.txt -o purged.fasta`
**Explanation:** Removes haplotigs and overlaps based on coverage.

### With parameters
**Args:** `purge_dups -i assembly.fasta -c coverage.txt -p params.yaml -o purged.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `purge_dups -v -i assembly.fasta -c coverage.txt -o purged.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `purge_dups -t 4 -i assembly.fasta -c coverage.txt -o purged.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Create histogram
**Args:** `purge_dups hist -i assembly.fasta -c coverage.txt -o histogram.txt`
**Explanation:** Creates coverage histogram.

### Generate report
**Args:** `purge_dups -i assembly.fasta -c coverage.txt -o purged.fasta --report report.html`
**Explanation:** Generates HTML report.