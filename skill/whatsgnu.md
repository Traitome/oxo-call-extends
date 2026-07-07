---
name: whatsgnu
category: bioinformatics
description: Whatshap - Haplotype phasing tool.
tags: [whatsgnu, haplotype-phasing, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/whatshap/whatshap"
---

## Concepts

- **Tool Overview**: Whatshap - Read-based phasing tool.
- **Core Function**: Phases genetic variants using sequencing reads.
- **Input**: VCF and BAM files.
- **Output**: Phased VCF.
- **Installation**: Install via pip or conda
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Phase variants
**Args:** `whatshap phase -o phased.vcf input.vcf input.bam`
**Explanation:** Phase variants.

### With options
**Args:** `whatshap phase -o phased.vcf --threads 8 input.vcf input.bam`
**Explanation:** Use 8 threads.
