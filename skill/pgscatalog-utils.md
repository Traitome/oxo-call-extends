---
name: pgscatalog-utils
category: population-genomics
description: pgscatalog-utils provides utilities for PGS Catalog API and scoring files.
tags: [pgscatalog-utils, population-genomics, utilities, api]
author: oxo-call-community
source_url: "https://github.com/PGScatalog/pygscatalog"
---

## Concepts

- **Tool Overview**: pgscatalog-utils provides PGS utilities.
- **Core Function**: Manages PGS Catalog API access.
- **Algorithm**: Uses API and file utilities.
- **Input Format**: Accepts various data formats.
- **Output**: Produces utility processing results.
- **Use Case**: PGS utilities, API management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **API Access**: Requires proper API credentials.
- **Network Access**: Requires internet connection.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgscatalog-utils --help`
**Explanation:** Shows available options and usage instructions.

### Query API
**Args:** `pgscatalog-utils -q "pgs_id" -o results.txt`
**Explanation:** Queries PGS Catalog API.

### Download scores
**Args:** `pgscatalog-utils -d pgs_id -o scores.txt`
**Explanation:** Downloads PGS scoring files.

### Verbose mode
**Args:** `pgscatalog-utils -v -q "pgs_id" -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgscatalog-utils -t 4 -q "pgs_id" -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgscatalog-utils -q "pgs_id" -o results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pgscatalog-utils -q "pgs_id" -o results.txt --report report.html`
**Explanation:** Generates HTML report.