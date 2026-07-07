---
name: rhocall
category: utility
description: RhoCall detects regions of homozygosity and makes UPD calls.
tags: [rhocall, utility, homozygosity, upd-calling]
author: oxo-call-community
source_url: "https://github.com/dnil/rhocall"
---

## Concepts

- **Tool Overview**: rhocall detects homozygosity regions.
- **Core Function**: Regions of homozygosity calling.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts VCF files.
- **Output**: Produces ROH calls.
- **Use Case**: Genetic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Variant Quality**: Affects calling.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rhocall --help`
**Explanation:** Shows available options and usage instructions.

### Call ROIs
**Args:** `rhocall call -i input.vcf -o rohs.bed`
**Explanation:** Calls regions of homozygosity.

### With parameters
**Args:** `rhocall call -i input.vcf -p params.yaml -o rohs.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rhocall -v call -i input.vcf -o rohs.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rhocall -t 4 call -i input.vcf -o rohs.bed`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `rhocall call -i input.vcf -r reference.fasta -o rohs.bed`
**Explanation:** Uses reference genome.

### Generate plot
**Args:** `rhocall call -i input.vcf -o rohs.bed --plot plot.png`
**Explanation:** Generates visualization plot.