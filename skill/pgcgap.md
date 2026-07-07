---
name: pgcgap
category: population-genomics
description: PGCGAP performs prokaryotic comparative genomics analysis.
tags: [pgcgap, population-genomics, comparative, prokaryotic]
author: oxo-call-community
source_url: "https://github.com/liaochenlanruo/pgcgap/blob/master/README.md"
---

## Concepts

- **Tool Overview**: PGCGAP analyzes prokaryotic genomes.
- **Core Function**: Performs comparative genomics analysis.
- **Algorithm**: Uses comprehensive analysis pipeline.
- **Input Format**: Accepts reads or genome files.
- **Output**: Produces comparative genomics results.
- **Use Case**: Comparative genomics, prokaryotic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genome sets require memory.
- **Read Quality**: Results depend on read quality.
- **Pipeline Configuration**: Requires proper config setup.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgcgap --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pgcgap -i reads/ -o comparative_results/`
**Explanation:** Runs comparative genomics pipeline.

### With genomes
**Args:** `pgcgap -g genomes/ -o comparative_results/`
**Explanation:** Uses assembled genomes for analysis.

### Verbose mode
**Args:** `pgcgap -v -i reads/ -o comparative_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgcgap -t 8 -i reads/ -o comparative_results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pgcgap -i reads/ -o comparative_results/ --format json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pgcgap -i reads/ -o comparative_results/ --report report.html`
**Explanation:** Generates HTML report.