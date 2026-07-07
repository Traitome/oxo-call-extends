---
name: pybiomart
category: programming
description: pybiomart provides a simple Pythonic interface to the BioMart database for querying biological data.
tags: [pybiomart, programming, biomart, database-query]
author: oxo-call-community
source_url: "https://jrderuiter.github.io/pybiomart/"
---

## Concepts

- **Tool Overview**: pybiomart queries BioMart databases.
- **Core Function**: Biological data retrieval.
- **Algorithm**: Uses BioMart API.
- **Input Format**: Accepts query parameters.
- **Output**: Produces query results.
- **Use Case**: Genomic data annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Access**: Requires internet connection.
- **Database Availability**: Dependent on BioMart service.
- **Query Complexity**: May affect performance.
- **Data Volume**: Large queries may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pybiomart --help`
**Explanation:** Shows available options and usage instructions.

### Query database
**Args:** `pybiomart query -d database -a attributes -f filters -o results.txt`
**Explanation:** Queries BioMart database.

### With parameters
**Args:** `pybiomart query -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pybiomart -v query -d database -o results.txt`
**Explanation:** Runs with verbose output.

### List databases
**Args:** `pybiomart list databases`
**Explanation:** Lists available BioMart databases.

### List attributes
**Args:** `pybiomart list attributes -d database`
**Explanation:** Lists available attributes for database.

### Generate report
**Args:** `pybiomart query -d database -o results.txt --report report.html`
**Explanation:** Generates HTML report.