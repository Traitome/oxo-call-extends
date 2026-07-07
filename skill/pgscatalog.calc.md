---
name: pgscatalog.calc
category: population-genomics
description: pgscatalog.calc works with calculated polygenic scores.
tags: [pgscatalog.calc, population-genomics, polygenic, scores]
author: oxo-call-community
source_url: "https://github.com/PGScatalog/pygscatalog"
---

## Concepts

- **Tool Overview**: pgscatalog.calc analyzes polygenic scores.
- **Core Function**: Calculates and manages PGS data.
- **Algorithm**: Uses polygenic scoring methods.
- **Input Format**: Accepts genetic data files.
- **Output**: Produces polygenic score results.
- **Use Case**: Polygenic scores, genetic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Score Quality**: Results depend on data quality.
- **Reference Data**: Requires proper reference data.
- **Runtime**: Calculation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgscatalog.calc --help`
**Explanation:** Shows available options and usage instructions.

### Calculate scores
**Args:** `pgscatalog.calc -i genotypes.txt -o scores.txt`
**Explanation:** Calculates polygenic scores.

### With weights
**Args:** `pgscatalog.calc -i genotypes.txt -w weights.txt -o scores.txt`
**Explanation:** Uses specific weight file.

### Verbose mode
**Args:** `pgscatalog.calc -v -i genotypes.txt -o scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgscatalog.calc -t 4 -i genotypes.txt -o scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgscatalog.calc -i genotypes.txt -o scores.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pgscatalog.calc -i genotypes.txt -o scores.txt --report report.html`
**Explanation:** Generates HTML report.