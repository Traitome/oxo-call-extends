---
name: ntroot
category: population-genomics
description: ntRoot performs ancestry inference from genomic sequencing data.
tags: [ntroot, population-genomics, ancestry, inference]
author: oxo-call-community
source_url: "https://github.com/BirolLab/ntroot"
---

## Concepts

- **Tool Overview**: ntRoot infers ancestry and population structure from genomic data.
- **Core Function**: Analyzes genetic variation to determine ancestral origins.
- **Algorithm**: Uses statistical methods for ancestry estimation.
- **Input Format**: Accepts VCF files or genotype data.
- **Output**: Produces ancestry predictions and population assignments.
- **Use Case**: Population genetics, ancestry analysis, and genetic studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Panels**: Requires appropriate reference population data.
- **Data Quality**: Results depend on input data quality.
- **Population Admixture**: Complex admixture may affect results.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `ntroot --help`
**Explanation:** Shows available options and usage instructions.

### Infer ancestry
**Args:** `ntroot -i genotypes.vcf -o ancestry.txt`
**Explanation:** Infers ancestry from VCF file.

### With reference panel
**Args:** `ntroot -i genotypes.vcf -r reference.vcf -o ancestry.txt`
**Explanation:** Uses custom reference panel for comparison.

### Output probabilities
**Args:** `ntroot -i genotypes.vcf -o ancestry.txt --probabilities`
**Explanation:** Outputs ancestry probabilities.

### Threads
**Args:** `ntroot -i genotypes.vcf -t 8 -o ancestry.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ntroot -i genotypes.vcf -v -o ancestry.txt`
**Explanation:** Runs with verbose output.

### Quality filtering
**Args:** `ntroot -i genotypes.vcf -q 30 -o ancestry.txt`
**Explanation:** Filters by minimum quality score.