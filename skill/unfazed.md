---
name: unfazed
category: bioinformatics
description: Unfazed - Tool for variant calling and phasing.
tags: [unfazed, variant-calling, phasing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/unfazed/"
---

## Concepts

- **Tool Overview**: Unfazed - A tool for variant calling and haplotype phasing.
- **Core Function**: Calls variants and phases haplotypes from sequencing data.
- **Input**: BAM/SAM file, reference genome.
- **Output**: VCF file with phased variants.
- **Installation**: Install via conda or source
- **Use Case**: Variant analysis, haplotype phasing, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Reference Genome**: Requires indexed reference genome.

## Examples

### Call variants
**Args:** `unfazed call -i input.bam -r ref.fasta -o variants.vcf`
**Explanation:** Call variants from BAM file.

### Phase haplotypes
**Args:** `unfazed phase -i variants.vcf -o phased.vcf`
**Explanation:** Phase haplotypes.
