---
name: pastrami
category: population-genomics
description: Pastrami performs rapid human ancestry estimation.
tags: [pastrami, population-genomics, ancestry-estimation]
author: oxo-call-community
source_url: "https://github.com/healthdisparities/pastrami"
---

## Concepts

- **Tool Overview**: Pastrami estimates human ancestry from genomic data.
- **Core Function**: Performs ancestry estimation efficiently.
- **Algorithm**: Uses machine learning for ancestry prediction.
- **Input Format**: Accepts genotype data in various formats.
- **Output**: Produces ancestry proportions.
- **Use Case**: Population genetics, ancestry analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Panels**: Results depend on reference panel quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pastrami --help`
**Explanation:** Shows available options and usage instructions.

### Estimate ancestry
**Args:** `pastrami -i genotypes.vcf -o ancestry.txt`
**Explanation:** Estimates ancestry proportions.

### With reference panel
**Args:** `pastrami -i genotypes.vcf -r reference.bed -o ancestry.txt`
**Explanation:** Uses custom reference panel.

### Verbose mode
**Args:** `pastrami -v -i genotypes.vcf -o ancestry.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pastrami -t 8 -i genotypes.vcf -o ancestry.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pastrami -i genotypes.vcf -o ancestry.json --json`
**Explanation:** Outputs in JSON format.

### Plot results
**Args:** `pastrami_plot -i ancestry.txt -o plot.png`
**Explanation:** Generates ancestry visualization.