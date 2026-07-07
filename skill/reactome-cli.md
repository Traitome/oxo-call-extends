---
name: reactome-cli
category: containerization
description: Reactome CLI provides command-line access to Reactome pathway database for pathway analysis.
tags: [reactome-cli, containerization, pathway-analysis, reactome]
author: oxo-call-community
source_url: "https://github.com/reactome/reactome_galaxy"
---

## Concepts

- **Tool Overview**: reactome-cli analyzes pathways.
- **Core Function**: Pathway analysis.
- **Algorithm**: Uses Reactome methods.
- **Input Format**: Accepts gene lists.
- **Output**: Produces pathway results.
- **Use Case**: Pathway analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Gene Identifiers**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reactome-cli --help`
**Explanation:** Shows available options and usage instructions.

### Analyze pathways
**Args:** `reactome-cli analyze -i genes.txt -o pathways.txt`
**Explanation:** Analyzes Reactome pathways.

### With parameters
**Args:** `reactome-cli analyze -i genes.txt -p params.yaml -o pathways.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reactome-cli -v analyze -i genes.txt -o pathways.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reactome-cli -t 4 analyze -i genes.txt -o pathways.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With species
**Args:** `reactome-cli analyze -i genes.txt -s "Homo sapiens" -o pathways.txt`
**Explanation:** Uses species filter.

### Generate report
**Args:** `reactome-cli analyze -i genes.txt -o pathways.txt --report report.html`
**Explanation:** Generates HTML report.