---
name: platypus-variant
category: variant-calling
description: platypus-variant is a haplotype-based variant caller.
tags: [platypus-variant, variant-calling, haplotype, ngs]
author: oxo-call-community
source_url: "http://www.well.ox.ac.uk/platypus"
---

## Concepts

- **Tool Overview**: platypus-variant calls genetic variants.
- **Core Function**: Haplotype-based variant calling.
- **Algorithm**: Uses haplotype assembly methods.
- **Input Format**: Accepts BAM/FASTA files.
- **Output**: Produces VCF variant calls.
- **Use Case**: Variant analysis, genome sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Calling Accuracy**: May have false positives/negatives.
- **Runtime**: Calling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `platypus-variant --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `platypus-variant callVariants --bamFiles=reads.bam --output=variants.vcf`
**Explanation:** Calls variants from sequencing data.

### With parameters
**Args:** `platypus-variant callVariants --bamFiles=reads.bam --params=params.yaml --output=variants.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `platypus-variant callVariants --bamFiles=reads.bam --output=variants.vcf --verbose`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `platypus-variant callVariants --bamFiles=reads.bam --nCPU=4 --output=variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `platypus-variant callVariants --bamFiles=reads.bam --output=variants.vcf --format=vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `platypus-variant callVariants --bamFiles=reads.bam --output=variants.vcf --report=report.html`
**Explanation:** Generates HTML report.