---
name: pathwaymatcher
category: utility
description: PathwayMatcher searches for pathways related to protein lists in Reactome.
tags: [pathwaymatcher, utility, pathways, reactome]
author: oxo-call-community
source_url: "https://github.com/PathwayAnalysisPlatform/PathwayMatcher"
---

## Concepts

- **Tool Overview**: PathwayMatcher identifies biological pathways.
- **Core Function**: Searches Reactome for pathways related to proteins.
- **Algorithm**: Uses pathway enrichment analysis.
- **Input Format**: Accepts protein lists.
- **Output**: Produces pathway matches and statistics.
- **Use Case**: Systems biology, pathway analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Updates**: Requires updated Reactome database.
- **Protein Identifiers**: Requires correct identifier format.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathwaymatcher --help`
**Explanation:** Shows available options and usage instructions.

### Search pathways
**Args:** `pathwaymatcher -i proteins.txt -o pathways.txt`
**Explanation:** Finds pathways related to protein list.

### With Reactome
**Args:** `pathwaymatcher -i proteins.txt -r reactome.db -o pathways.txt`
**Explanation:** Uses custom Reactome database.

### Verbose mode
**Args:** `pathwaymatcher -v -i proteins.txt -o pathways.txt`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `pathwaymatcher -i proteins.txt -o pathways.json --json`
**Explanation:** Outputs in JSON format.

### Enrichment analysis
**Args:** `pathwaymatcher -i proteins.txt -e -o enrichment.txt`
**Explanation:** Performs pathway enrichment analysis.

### Generate report
**Args:** `pathwaymatcher -i proteins.txt -o pathways/ -r report.html`
**Explanation:** Generates HTML report.