---
name: vardict
category: variant-calling
description: VarDict - Variant caller for targeted sequencing.
tags: [vardict, variant-calling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/VarDict"
---

## Concepts

- **Tool Overview**: VarDict - A variant caller optimized for targeted sequencing.
- **Core Function**: Calls variants with focus on sensitivity for low-frequency variants.
- **Input**: BAM file, BED file.
- **Output**: VCF file.
- **Installation**: Install via conda or source
- **Use Case**: Variant calling, cancer genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Bed Format**: Requires proper BED format.

## Examples

### Call variants
**Args:** `vardict -G ref.fasta -f 0.01 -N sample -b sample.bam -R regions.bed > variants.vcf`
**Explanation:** Call variants from BAM file.

### With options
**Args:** `vardict -G ref.fasta -f 0.01 -N sample -b sample.bam -R regions.bed -t 8 > variants.vcf`
**Explanation:** Use 8 threads.
