---
name: rapsearch
category: utility
description: RAPSearch2 performs fast protein similarity searches for functional annotation.
tags: [rapsearch, utility, protein-similarity, annotation]
author: oxo-call-community
source_url: "http://omics.informatics.indiana.edu/mg/RAPSearch2/"
---

## Concepts

- **Tool Overview**: rapsearch searches proteins.
- **Core Function**: Protein similarity search.
- **Algorithm**: Uses fast search methods.
- **Input Format**: Accepts protein sequences.
- **Output**: Produces similarity results.
- **Use Case**: Functional annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Database Quality**: Affects search.
- **Parameters**: Must be configured.
- **Runtime**: Search may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rapsearch --help`
**Explanation:** Shows available options and usage instructions.

### Build database
**Args:** `rapsearch build -i proteins.fasta -o database/`
**Explanation:** Builds search database.

### Search proteins
**Args:** `rapsearch search -i query.fasta -d database/ -o results.txt`
**Explanation:** Searches protein database.

### With parameters
**Args:** `rapsearch search -i query.fasta -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rapsearch -v search -i query.fasta -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rapsearch -t 4 search -i query.fasta -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Generate report
**Args:** `rapsearch search -i query.fasta -o results.txt --report report.html`
**Explanation:** Generates HTML report.