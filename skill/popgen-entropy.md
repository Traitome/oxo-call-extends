---
name: popgen-entropy
category: population-genomics
description: popgen-entropy infers population structure from polyploid individuals.
tags: [popgen-entropy, population-genomics, polyploid, ancestry]
author: oxo-call-community
source_url: "https://bitbucket.org/buerklelab/mixedploidy-entropy/src/master/"
---

## Concepts

- **Tool Overview**: popgen-entropy analyzes population structure.
- **Core Function**: Mixed-ploidy ancestry estimation.
- **Algorithm**: Uses likelihood-based methods.
- **Input Format**: Accepts genotype likelihood data.
- **Output**: Produces ancestry estimates.
- **Use Case**: Population genetics, hybridization detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on genotype quality.
- **Inference Accuracy**: May have estimation errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `entropy --help`
**Explanation:** Shows available options and usage instructions.

### Infer ancestry
**Args:** `entropy -i genotypes.vcf -o ancestry.txt`
**Explanation:** Infers population structure from polyploid data.

### With parameters
**Args:** `entropy -i genotypes.vcf -p params.yaml -o ancestry.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `entropy -v -i genotypes.vcf -o ancestry.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `entropy -t 4 -i genotypes.vcf -o ancestry.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `entropy -i genotypes.vcf -o ancestry.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `entropy -i genotypes.vcf -o ancestry.txt --report report.html`
**Explanation:** Generates HTML report.