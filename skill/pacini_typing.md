---
name: pacini_typing
category: utility
description: Pacini-typing is a YAML-based bacterial genotyping application.
tags: [pacini_typing, utility, bacterial-genotyping, yaml]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/Pacini-typing"
---

## Concepts

- **Tool Overview**: Pacini-typing performs bacterial genotyping using YAML configuration.
- **Core Function**: Determines bacterial genotypes from sequencing data.
- **Algorithm**: Uses YAML-based rules for genotype calling.
- **Input Format**: Accepts FASTA sequences and YAML configuration.
- **Output**: Produces genotype calls and reports.
- **Use Case**: Bacterial identification, epidemiological surveillance, and strain typing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Configuration Complexity**: Requires proper YAML configuration.
- **Reference Data**: Depends on reference database.
- **Algorithm Selection**: Different algorithms may give different results.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pacini_typing --help`
**Explanation:** Shows available options and usage instructions.

### Run genotyping
**Args:** `pacini_typing -i genome.fasta -c config.yaml -o results.txt`
**Explanation:** Performs bacterial genotyping.

### With database
**Args:** `pacini_typing -i genome.fasta -d database/ -o results.txt`
**Explanation:** Uses custom reference database.

### Output format
**Args:** `pacini_typing -i genome.fasta -o results.json --json`
**Explanation:** Outputs in JSON format.

### Verbose mode
**Args:** `pacini_typing -i genome.fasta -v -o results.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `pacini_typing batch -d genomes/ -o results/`
**Explanation:** Processes multiple genome files.

### Update database
**Args:** `pacini_typing update -d database/`
**Explanation:** Updates reference database.