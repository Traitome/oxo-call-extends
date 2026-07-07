---
name: cyvcf
category: variant-calling
description: Cython wrapper around htslib for fast parsing of Variant Call Format (VCF) files
tags: [cyvcf, variant-calling, VCF, htslib, Cython]
author: oxo-call-community
source_url: "https://github.com/brentp/cyvcf2"
---

## Concepts

- **Tool Overview**: cyvcf (v0.8.0+) is an older Cython wrapper around htslib for parsing VCF files, now superseded by cyvcf2.
- **Core Function**: Provides basic VCF parsing functionality with Python bindings.
- **Input/Output**: Input: VCF files. Output: Variant records and genotypes.
- **Key Features**: Fast parsing, basic variant access, genotype retrieval.
- **Installation**: `conda install -c bioconda cyvcf`

## Pitfalls

- **Deprecated**: Consider using cyvcf2 instead for improved performance and features.
- **VCF Format**: Requires properly formatted VCF files.
- **Limited Features**: May lack advanced features available in cyvcf2.
- **Maintenance**: May not receive updates or bug fixes.
- **Compatibility**: May have compatibility issues with newer VCF specifications.

## Examples

### Parse VCF file
**Args:**
```python
import cyvcf
vcf = cyvcf.VCF('variants.vcf')
for variant in vcf:
    print(variant.chrom, variant.pos, variant.ref, variant.alt)
```
**Explanation:** Iterate through VCF records.

### Access genotypes
**Args:**
```python
import cyvcf
vcf = cyvcf.VCF('variants.vcf')
for variant in vcf:
    print(variant.genotypes)
```
**Explanation:** Access genotype information for variants.

### Filter by region
**Args:**
```python
import cyvcf
vcf = cyvcf.VCF('variants.vcf')
for variant in vcf('chr1:1000-2000'):
    print(variant)
```
**Explanation:** Retrieve variants in specific genomic region.
