---
name: progenomes
category: utility
description: progenomes provides command-line access to bacterial and archaeal genome databases.
tags: [progenomes, utility, genome-database, prokaryotes]
author: oxo-call-community
source_url: "https://github.com/BigDataBiology/progenomes-cli"
---

## Concepts

- **Tool Overview**: progenomes accesses genome databases.
- **Core Function**: Genome data retrieval.
- **Algorithm**: Uses database query methods.
- **Input Format**: Accepts query parameters.
- **Output**: Produces genome data.
- **Use Case**: Comparative genomics, data mining.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Access**: Requires internet connection.
- **Data Quality**: Results depend on database quality.
- **Query Complexity**: May affect performance.
- **Runtime**: Query may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `progenomes --help`
**Explanation:** Shows available options and usage instructions.

### Query database
**Args:** `progenomes query -o results.txt`
**Explanation:** Queries proGenomes database.

### With parameters
**Args:** `progenomes query -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `progenomes -v query -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `progenomes -t 4 query -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `progenomes query -o results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `progenomes query -o results.txt --report report.html`
**Explanation:** Generates HTML report.