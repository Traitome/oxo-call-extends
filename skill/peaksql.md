---
name: peaksql
category: utility
description: peaksql provides dynamic machine learning database for genomics.
tags: [peaksql, utility, database, machine-learning]
author: oxo-call-community
source_url: "https://vanheeringen-lab.github.io/peaksql/"
---

## Concepts

- **Tool Overview**: peaksql manages genomic databases.
- **Core Function**: Provides ML-ready database for genomics.
- **Algorithm**: Uses database and ML integration.
- **Input Format**: Accepts genomic data files.
- **Output**: Produces database and ML features.
- **Use Case**: Genomics, machine learning, data management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Data Quality**: Results depend on input data.
- **Database Schema**: Requires proper schema design.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peaksql --help`
**Explanation:** Shows available options and usage instructions.

### Create database
**Args:** `peaksql create -i data/ -o database.db`
**Explanation:** Creates genomic database.

### Query database
**Args:** `peaksql query -d database.db -q "SELECT * FROM peaks" -o results.txt`
**Explanation:** Queries database for results.

### Verbose mode
**Args:** `peaksql -v create -i data/ -o database.db`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peaksql -t 4 create -i data/ -o database.db`
**Explanation:** Uses 4 threads for parallel processing.

### Export features
**Args:** `peaksql export -d database.db -o features.csv --ml`
**Explanation:** Exports ML-ready features.

### Generate report
**Args:** `peaksql report -d database.db -o report.html`
**Explanation:** Generates HTML report.