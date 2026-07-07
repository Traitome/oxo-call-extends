---
name: cyvcf2
category: variant-calling
description: Cython wrapper around htslib for fast parsing of VCF files
tags: [cyvcf2, variant-calling, VCF, htslib, Cython]
author: oxo-call-community
source_url: "https://brentp.github.io/cyvcf2"
---

## Concepts

- **Tool Overview**: cyvcf2 (v0.32.1+) is a Cython wrapper around htslib for fast parsing of Variant Call Format (VCF) files.
- **Core Function**: Provides high-performance VCF parsing and manipulation with Python bindings.
- **Input/Output**: Input: VCF files. Output: Variant records, genotypes, annotations.
- **Key Features**: Fast VCF parsing, support for BCF, genotype access, annotation handling.
- **Installation**: `conda install -c bioconda cyvcf2`

## Pitfalls

- **VCF Format**: Requires properly formatted VCF files according to VCF specification.
- **Indexing**: VCF files should be indexed for random access.
- **Memory Usage**: Loading large VCF files may require significant memory.
- **Python Compatibility**: Ensure compatibility with Python version requirements.
- **Annotation Fields**: Custom annotation fields require careful handling.

## Examples

### Parse VCF file
**Args:**
```python
from cyvcf2 import VCF
vcf = VCF('variants.vcf.gz')
for variant in vcf:
    print(variant.CHROM, variant.POS, variant.REF, variant.ALT)
```
**Explanation:** Iterate through VCF records and print basic variant information.

### Access genotype information
**Args:**
```python
from cyvcf2 import VCF
vcf = VCF('variants.vcf.gz')
for variant in vcf:
    for sample in variant.samples:
        print(sample.gt_bases)
```
**Explanation:** Access genotype bases for each sample.

### Filter variants by quality
**Args:**
```python
from cyvcf2 import VCF
vcf = VCF('variants.vcf.gz')
for variant in vcf:
    if variant.QUAL > 30:
        print(variant)
```
**Explanation:** Filter variants with quality score > 30.
