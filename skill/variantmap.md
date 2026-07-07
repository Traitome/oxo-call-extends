---
name: variantmap
category: bioinformatics
description: VariantMap - Variant mapping tool.
tags: [variantmap, variant-mapping, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/variantmap/"
---

## Concepts

- **Tool Overview**: VariantMap - A tool for mapping variants across genomes.
- **Core Function**: Maps variants between different genome assemblies.
- **Input**: VCF file, chain file.
- **Output**: Mapped VCF file.
- **Installation**: Install via conda or source
- **Use Case**: Variant liftover, genome comparison, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Chain File**: Requires proper chain file.

## Examples

### Map variants
**Args:** `variantmap -i input.vcf -c hg19ToHg38.over.chain -o output.vcf`
**Explanation:** Map variants from hg19 to hg38.

### With options
**Args:** `variantmap -i input.vcf -c hg19ToHg38.over.chain -o output.vcf -f`
**Explanation:** Force mapping.
