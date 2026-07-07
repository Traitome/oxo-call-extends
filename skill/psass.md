---
name: psass
category: population-genomics
description: psass compares pooled-sequencing data between two populations for population genetics analysis.
tags: [psass, population-genomics, pooled-sequencing, population-comparison]
author: oxo-call-community
source_url: "https://github.com/RomainFeron/PSASS"
---

## Concepts

- **Tool Overview**: psass analyzes pooled sequencing data.
- **Core Function**: Population comparison.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts VCF/BAM files.
- **Output**: Produces population statistics.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Pooling Effects**: May affect accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psass --help`
**Explanation:** Shows available options and usage instructions.

### Compare populations
**Args:** `psass -p1 population1.vcf -p2 population2.vcf -o results.txt`
**Explanation:** Compares two pooled populations.

### With parameters
**Args:** `psass -p1 population1.vcf -p2 population2.vcf -params params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psass -v -p1 population1.vcf -p2 population2.vcf -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psass -t 4 -p1 population1.vcf -p2 population2.vcf -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psass -p1 population1.vcf -p2 population2.vcf -o results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `psass -p1 population1.vcf -p2 population2.vcf -o results.txt --report report.html`
**Explanation:** Generates HTML report.