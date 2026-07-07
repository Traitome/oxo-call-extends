---
name: varlociraptor
category: variant-calling
description: VarLociraptor - Variant calling and filtering tool.
tags: [varlociraptor, variant-calling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/varlociraptor/varlociraptor"
---

## Concepts

- **Tool Overview**: VarLociraptor - A tool for variant calling and filtering.
- **Core Function**: Calls and filters variants from sequencing data.
- **Input**: BAM file, VCF file.
- **Output**: Filtered variants.
- **Installation**: Install via conda or source
- **Use Case**: Variant calling, quality control, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Configuration**: Requires proper configuration.

## Examples

### Call variants
**Args:** `varlociraptor call -i sample.bam -o variants.vcf`
**Explanation:** Call variants.

### With options
**Args:** `varlociraptor call -i sample.bam -o variants.vcf -t 8`
**Explanation:** Use 8 threads.
