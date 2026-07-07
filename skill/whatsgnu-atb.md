---
name: whatsgnu-atb
category: bioinformatics
description: Whatshap-ATB - Phasing tool.
tags: [whatsgnu-atb, haplotype-phasing, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/whatsgnu-atb/"
---

## Concepts

- **Tool Overview**: Whatshap-ATB - Haplotype phasing tool.
- **Core Function**: Phases variants using sequencing data.
- **Input**: VCF file.
- **Output**: Phased VCF.
- **Installation**: Install via pip or conda
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Complexity**: May have steep learning curve.

## Examples

### Phase variants
**Args:** `whatsgnu-atb phase -i input.vcf -o phased.vcf`
**Explanation:** Phase variants.

### With options
**Args:** `whatsgnu-atb phase -i input.vcf -o phased.vcf -t 8`
**Explanation:** Use 8 threads.
