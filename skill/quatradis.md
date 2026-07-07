---
name: quatradis
category: utility
description: QuaTradis provides tools to analyze output from TraDIS transposon insertion sequencing analyses.
tags: [quatradis, utility, tradis, transposon]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/QuaTradis"
---

## Concepts

- **Tool Overview**: quatradis analyzes TraDIS data.
- **Core Function**: Transposon analysis.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces insertion sites.
- **Use Case**: Functional genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Insertion Density**: Must be sufficient.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quatradis --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `quatradis analyze -i reads.fastq -o results.txt`
**Explanation:** Analyzes TraDIS data.

### With parameters
**Args:** `quatradis analyze -i reads.fastq -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quatradis -v analyze -i reads.fastq -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quatradis -t 4 analyze -i reads.fastq -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With genome
**Args:** `quatradis analyze -i reads.fastq -g genome.fasta -o results.txt`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `quatradis analyze -i reads.fastq -o results.txt --report report.html`
**Explanation:** Generates HTML report.