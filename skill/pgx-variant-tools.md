---
name: pgx-variant-tools
category: variant-calling
description: pgx-variant-tools provides methods for calling and manipulating normalized variants.
tags: [pgx-variant-tools, variant-calling, normalization, manipulation]
author: oxo-call-community
source_url: "https://github.com/LUMC/pgx-variant-tools"
---

## Concepts

- **Tool Overview**: pgx-variant-tools manages variants.
- **Core Function**: Calls and normalizes variants.
- **Algorithm**: Uses variant normalization methods.
- **Input Format**: Accepts VCF variant files.
- **Output**: Produces normalized variant results.
- **Use Case**: Variant calling, normalization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large variant sets require memory.
- **Variant Quality**: Results depend on variant quality.
- **Reference Genome**: Requires proper reference genome.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgx-variant-tools --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `pgx-variant-tools -i input.vcf -o normalized.vcf`
**Explanation:** Calls and normalizes variants.

### With reference
**Args:** `pgx-variant-tools -i input.vcf -r ref.fa -o normalized.vcf`
**Explanation:** Uses specific reference genome.

### Verbose mode
**Args:** `pgx-variant-tools -v -i input.vcf -o normalized.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgx-variant-tools -t 4 -i input.vcf -o normalized.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgx-variant-tools -i input.vcf -o normalized.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pgx-variant-tools -i input.vcf -o normalized.vcf --report report.html`
**Explanation:** Generates HTML report.