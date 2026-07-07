---
name: phizz
category: utility
description: phizz queries HPO database and other sources.
tags: [phizz, utility, hpo, database]
author: oxo-call-community
source_url: "https://github.com/moonso/phizz"
---

## Concepts

- **Tool Overview**: phizz queries HPO database.
- **Core Function**: HPO database query tool.
- **Algorithm**: Uses database query methods.
- **Input Format**: Accepts HPO term queries.
- **Output**: Produces HPO database results.
- **Use Case**: HPO analysis, database queries.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large queries require memory.
- **Database Access**: Requires proper database access.
- **Query Quality**: Results depend on query quality.
- **Runtime**: Querying may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phizz --help`
**Explanation:** Shows available options and usage instructions.

### Query HPO
**Args:** `phizz -q "HP:0000118" -o hpo_results.txt`
**Explanation:** Queries HPO database.

### With parameters
**Args:** `phizz -q "HP:0000118" -p params.yaml -o hpo_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phizz -v -q "HP:0000118" -o hpo_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phizz -t 4 -q "HP:0000118" -o hpo_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phizz -q "HP:0000118" -o hpo_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phizz -q "HP:0000118" -o hpo_results.txt --report report.html`
**Explanation:** Generates HTML report.