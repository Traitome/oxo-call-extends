---
name: xcftools
category: bioinformatics
description: XCFtools - Variant calling tool.
tags: [xcftools, variant-calling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/xcftools/"
---

## Concepts

- **Tool Overview**: XCFtools - Variant calling utilities.
- **Core Function**: Calls variants from sequencing data.
- **Input**: BAM file.
- **Output**: VCF file.
- **Installation**: Install via conda or source
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Complexity**: May have steep learning curve.

## Examples

### Call variants
**Args:** `xcftools call -i input.bam -o variants.vcf`
**Explanation:** Call variants.

### With options
**Args:** `xcftools call -i input.bam -o variants.vcf -t 8`
**Explanation:** Use 8 threads.
