---
name: bamsurgeon
category: variant-calling
description: Bamsurgeon - Tools for adding genomic variants to BAM files for testing variant callers
tags: [variant-simulation, bam-manipulation, variant-caller-testing, benchmarking]
author: oxo-call-community
source_url: "https://github.com/adamewing/bamsurgeon"
---

## Concepts

- **Tool Overview**: Bamsurgeon adds genomic variants (SNPs, indels, structural variants) to BAM files, creating synthetic datasets for testing and benchmarking variant callers.

- **Variant Injection**: Injects specified variants into existing BAM files while maintaining realistic read characteristics.

- **Testing Framework**: Enables systematic testing of variant calling pipelines with known ground truth.

- **Multiple Variant Types**: Supports SNPs, insertions, deletions, and more complex structural variants.

## Pitfalls

- **Reference Required**: Requires reference genome FASTA matching the BAM file.

- **Read Modification**: Modified reads may have artifacts. Verify results carefully.

- **Coverage Effects**: Injected variants may affect local coverage. Monitor for unrealistic patterns.

- **Complex Variants**: Large structural variants may be difficult to simulate realistically.

## Examples

### Add SNP to BAM
**Args:** `addsnv.py -v snp.vcf -f reference.fasta -b input.bam -o output.bam`
**Explanation:** Adds SNP variants from VCF file to BAM file.

### Add indel
**Args:** `addindel.py -v indel.vcf -f reference.fasta -b input.bam -o output.bam`
**Explanation:** Adds insertion/deletion variants from VCF file.

### Multiple variants
**Args:** `bamsurgeon.py -v variants.vcf -f reference.fasta -b input.bam -o output.bam`
**Explanation:** Adds multiple variant types from VCF file to BAM.

### Specify minimum coverage
**Args:** `addsnv.py -v snp.vcf -f reference.fasta -b input.bam -o output.bam --min-coverage 10`
**Explanation:** Ensures minimum 10x coverage at variant positions for realistic simulation.
