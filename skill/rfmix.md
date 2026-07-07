---
name: rfmix
category: utility
description: RFMix models ancestry along admixed chromosomes using haplotype sequences.
tags: [rfmix, utility, ancestry-analysis, admixture]
author: oxo-call-community
source_url: "https://github.com/slowkoni/rfmix"
---

## Concepts

- **Tool Overview**: rfmix models ancestry.
- **Core Function**: Ancestry inference along chromosomes.
- **Algorithm**: Uses discriminative methods.
- **Input Format**: Accepts haplotype sequences.
- **Output**: Produces ancestry probabilities.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Haplotype Quality**: Affects inference.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rfmix --help`
**Explanation:** Shows available options and usage instructions.

### Run ancestry inference
**Args:** `rfmix -f input.vcf -r reference.vcf -o output/`
**Explanation:** Models ancestry along admixed chromosomes.

### With parameters
**Args:** `rfmix -f input.vcf -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rfmix -v -f input.vcf -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rfmix -t 4 -f input.vcf -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### With ancestry map
**Args:** `rfmix -f input.vcf -a ancestry.map -o output/`
**Explanation:** Uses ancestry map file.

### Generate plot
**Args:** `rfmix -f input.vcf -o output/ --plot ancestry.png`
**Explanation:** Generates ancestry visualization.