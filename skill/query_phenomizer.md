---
name: query_phenomizer
category: utility
description: query_phenomizer queries and parses results from the Phenomizer phenotype matching tool.
tags: [query_phenomizer, utility, phenotype, phenomizer]
author: oxo-call-community
source_url: "https://www.github.com/moonso/query_phenomizer"
---

## Concepts

- **Tool Overview**: query_phenomizer queries Phenomizer.
- **Core Function**: Phenotype matching.
- **Algorithm**: Uses ontology matching.
- **Input Format**: Accepts phenotype terms.
- **Output**: Produces disease matches.
- **Use Case**: Clinical genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Access**: Requires internet.
- **API Key**: May be required.
- **Parameters**: Must be configured.
- **Runtime**: Depends on network.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `query_phenomizer --help`
**Explanation:** Shows available options and usage instructions.

### Query phenotypes
**Args:** `query_phenomizer query -p "phenotype_term" -o matches.txt`
**Explanation:** Queries Phenomizer for matches.

### With parameters
**Args:** `query_phenomizer query -p "phenotype_term" -c config.yaml -o matches.txt`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `query_phenomizer -v query -p "phenotype_term" -o matches.txt`
**Explanation:** Runs with verbose output.

### Multiple phenotypes
**Args:** `query_phenomizer query -p "term1,term2" -o matches.txt`
**Explanation:** Queries multiple phenotypes.

### With HPO terms
**Args:** `query_phenomizer query -p "HP:0001234" -o matches.txt`
**Explanation:** Uses HPO identifiers.

### Generate report
**Args:** `query_phenomizer query -p "phenotype_term" -o matches.txt --report report.html`
**Explanation:** Generates HTML report.