---
name: pgscatalog.core
category: population-genomics
description: pgscatalog.core provides core tools for polygenic scores and PGS Catalog.
tags: [pgscatalog.core, population-genomics, polygenic, catalog]
author: oxo-call-community
source_url: "https://github.com/PGScatalog/pygscatalog"
---

## Concepts

- **Tool Overview**: pgscatalog.core manages polygenic scores.
- **Core Function**: Provides PGS Catalog core tools.
- **Algorithm**: Uses polygenic scoring methods.
- **Input Format**: Accepts genetic data files.
- **Output**: Produces PGS analysis results.
- **Use Case**: Polygenic scores, catalog management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Catalog Access**: Requires proper API access.
- **Score Quality**: Results depend on data quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgscatalog.core --help`
**Explanation:** Shows available options and usage instructions.

### Query catalog
**Args:** `pgscatalog.core -q "trait_name" -o results.txt`
**Explanation:** Queries PGS Catalog for scores.

### With parameters
**Args:** `pgscatalog.core -i genotypes.txt -p pgs_id -o scores.txt`
**Explanation:** Applies specific PGS to genotypes.

### Verbose mode
**Args:** `pgscatalog.core -v -i genotypes.txt -o scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgscatalog.core -t 4 -i genotypes.txt -o scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgscatalog.core -i genotypes.txt -o scores.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pgscatalog.core -i genotypes.txt -o scores.txt --report report.html`
**Explanation:** Generates HTML report.