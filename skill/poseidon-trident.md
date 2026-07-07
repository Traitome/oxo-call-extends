---
name: poseidon-trident
category: formatting
description: poseidon-trident works with Poseidon genotype databases.
tags: [poseidon-trident, formatting, genotype-database, ancient-dna]
author: oxo-call-community
source_url: "https://www.poseidon-adna.org"
---

## Concepts

- **Tool Overview**: poseidon-trident manages genotype databases.
- **Core Function**: Database manipulation.
- **Algorithm**: Uses modular database methods.
- **Input Format**: Accepts Poseidon format files.
- **Output**: Produces database outputs.
- **Use Case**: Ancient DNA analysis, population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Data Quality**: Results depend on input quality.
- **Database Compatibility**: May have format issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `trident --help`
**Explanation:** Shows available options and usage instructions.

### Create database
**Args:** `trident build -i genotypes.vcf -o database/`
**Explanation:** Builds Poseidon genotype database.

### With parameters
**Args:** `trident build -i genotypes.vcf -p params.yaml -o database/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `trident -v build -i genotypes.vcf -o database/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `trident -t 4 build -i genotypes.vcf -o database/`
**Explanation:** Uses 4 threads for parallel processing.

### Query database
**Args:** `trident query -d database/ -o results.txt`
**Explanation:** Queries Poseidon database.

### Generate report
**Args:** `trident build -i genotypes.vcf -o database/ --report report.html`
**Explanation:** Generates HTML report.