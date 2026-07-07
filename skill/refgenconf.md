---
name: refgenconf
category: utility
description: RefGenConf is a standardized configuration object for reference genome assemblies for genome management.
tags: [refgenconf, utility, reference-genomes, configuration]
author: oxo-call-community
source_url: "https://refgenie.databio.org"
---

## Concepts

- **Tool Overview**: refgenconf manages genomes.
- **Core Function**: Genome configuration.
- **Algorithm**: Uses configuration methods.
- **Input Format**: Accepts genome metadata.
- **Output**: Produces config files.
- **Use Case**: Genome management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large configs require memory.
- **Config Quality**: Affects management.
- **Parameters**: Must be configured.
- **Runtime**: Management may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `refgenconf --help`
**Explanation:** Shows available options and usage instructions.

### Create config
**Args:** `refgenconf create -i genome_metadata.txt -o config.yaml`
**Explanation:** Creates genome configuration.

### With parameters
**Args:** `refgenconf create -i genome_metadata.txt -p params.yaml -o config.yaml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `refgenconf -v create -i genome_metadata.txt -o config.yaml`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `refgenconf -t 4 create -i genome_metadata.txt -o config.yaml`
**Explanation:** Uses 4 threads for parallel processing.

### With templates
**Args:** `refgenconf create -i genome_metadata.txt -t template.yaml -o config.yaml`
**Explanation:** Uses configuration template.

### Generate report
**Args:** `refgenconf create -i genome_metadata.txt -o config.yaml --report report.html`
**Explanation:** Generates HTML report.