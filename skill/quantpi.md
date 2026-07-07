---
name: quantpi
category: metagenomics
description: QuantPI is a general profiling system focused on robust microbiome research and metagenomic analysis.
tags: [quantpi, metagenomics, microbiome, profiling]
author: oxo-call-community
source_url: "https://github.com/ohmeta/quantpi"
---

## Concepts

- **Tool Overview**: quantpi profiles microbiomes.
- **Core Function**: Metagenomic analysis.
- **Algorithm**: Uses various methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces profiles.
- **Use Case**: Microbiomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Database**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quantpi --help`
**Explanation:** Shows available options and usage instructions.

### Run profiling
**Args:** `quantpi profile -i reads.fastq -o profile.txt`
**Explanation:** Profiles microbiome composition.

### With parameters
**Args:** `quantpi profile -i reads.fastq -p params.yaml -o profile.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quantpi -v profile -i reads.fastq -o profile.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quantpi -t 4 profile -i reads.fastq -o profile.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `quantpi profile -i reads.fastq -d database/ -o profile.txt`
**Explanation:** Uses custom database.

### Generate report
**Args:** `quantpi profile -i reads.fastq -o profile.txt --report report.html`
**Explanation:** Generates HTML report.