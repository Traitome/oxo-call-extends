---
name: igdtools
category: formatting
description: Tools for converting VCF files to IGD (Indexable Genotype Data) format and processing IGD files for efficient genotype data storage and access.
tags: [igdtools, formatting, VCF, IGD, genotype, picovcf]
author: oxo-call-community
source_url: "https://picovcf.readthedocs.io/en/latest/igdtools.html"
---

## Concepts

- **VCF to IGD Conversion**: Converts Variant Call Format (VCF) files to the efficient IGD format.
- **IGD Format**: Indexable Genotype Data format for fast access to genotype data with sparse matrix storage.
- **Sparse Matrix Storage**: Efficiently stores low-frequency variants as sample lists and high-frequency variants as bit vectors.
- **Tabix Support**: Utilizes Tabix indexing for parallel processing of compressed VCF files.
- **GRG Integration**: Works with GRG (Genomic Relationship Graph) construction tools for population genetics analysis.

## Pitfalls

- **Tabix Indexing**: Requires Tabix index for multi-threaded conversion of compressed VCF files.
- **Phased Data**: Works best with phased genotype data; unphased data may be less efficient.
- **File Size**: IGD files are uncompressed; may be larger than compressed VCF for small datasets.
- **Memory Requirements**: Large datasets may require significant memory for conversion.
- **Format Specificity**: Output is IGD format; may require conversion for other tools.

## Examples

### Convert VCF to IGD
**Args:** `igdtools input.vcf.gz -o output.igd`
**Explanation:** Converts a compressed VCF file to IGD format.

### Multi-threaded conversion
**Args:** `igdtools -j 8 input.vcf.gz -o output.igd`
**Explanation:** Uses 8 threads for faster conversion (requires Tabix index).

### Filter variants during conversion
**Args:** `igdtools --min-af 0.01 input.vcf.gz -o filtered.igd`
**Explanation:** Filters variants with allele frequency below 0.01.

### Exclude variant IDs
**Args:** `igdtools --no-var-ids input.vcf.gz -o output.igd`
**Explanation:** Excludes variant identifiers from the output IGD file.

### Convert uncompressed VCF
**Args:** `igdtools input.vcf -o output.igd`
**Explanation:** Converts an uncompressed VCF file to IGD format.