---
name: quick-variants
category: variant-calling
description: QuickVariants provides fast and accurate genetic variant identification from sequencing data.
tags: [quick-variants, variant-calling, snp, indel]
author: oxo-call-community
source_url: "https://github.com/caozhichongchong/QuickVariants"
---

## Concepts

- **Tool Overview**: quick-variants calls genetic variants.
- **Core Function**: Variant identification.
- **Algorithm**: Uses mapping-based methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces VCF files.
- **Use Case**: Variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects variant calling.
- **Parameters**: Must be configured.
- **Runtime**: Calling may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quick-variants --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `quick-variants call -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies genetic variants.

### With parameters
**Args:** `quick-variants call -i aligned.bam -p params.yaml -o variants.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quick-variants -v call -i aligned.bam -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quick-variants -t 4 call -i aligned.bam -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### With quality filter
**Args:** `quick-variants call -i aligned.bam -q 30 -o variants.vcf`
**Explanation:** Filters by quality.

### Generate report
**Args:** `quick-variants call -i aligned.bam -o variants.vcf --report report.html`
**Explanation:** Generates HTML report.