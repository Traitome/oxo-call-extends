---
name: ratatoskr
category: metagenomics
description: Ratatoskr collects and downloads taxonomic type strain data for metagenomic analysis.
tags: [ratatoskr, metagenomics, taxonomy, type-strains]
author: oxo-call-community
source_url: "https://github.com/Fabian-Bastiaanssen/Ratatoskr"
---

## Concepts

- **Tool Overview**: ratatoskr downloads data.
- **Core Function**: Type strain collection.
- **Algorithm**: Uses database queries.
- **Input Format**: Accepts taxon names.
- **Output**: Produces strain data.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Network**: Requires internet access.
- **Parameters**: Must be configured.
- **Runtime**: Download may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ratatoskr --help`
**Explanation:** Shows available options and usage instructions.

### Download strains
**Args:** `ratatoskr download -i taxa.txt -o strains/`
**Explanation:** Downloads type strain data.

### With parameters
**Args:** `ratatoskr download -i taxa.txt -p params.yaml -o strains/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ratatoskr -v download -i taxa.txt -o strains/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ratatoskr -t 4 download -i taxa.txt -o strains/`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `ratatoskr download -i taxa.txt -d ncbi -o strains/`
**Explanation:** Uses specific database.

### Generate report
**Args:** `ratatoskr download -i taxa.txt -o strains/ --report report.html`
**Explanation:** Generates HTML report.