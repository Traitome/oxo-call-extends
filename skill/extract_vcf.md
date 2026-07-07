---
name: extract_vcf
category: formatting
description: "Tool to extract information from vcf file."
tags: [extract_vcf, formatting, VCF, variant-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/moonso/extract_vcf"
---

## Concepts

- **Tool Overview**: extract_vcf is a tool for extracting specific information from VCF (Variant Call Format) files.
- **Core Function**: Extracts variant information, annotations, and genotypes from VCF files for downstream analysis.
- **Input/Output**: Input: VCF file. Output: Extracted information (CSV/TSV), filtered VCF files.
- **Algorithm**: Parses VCF format and extracts specified fields based on user-defined criteria.
- **Key Features**: VCF parsing, field extraction, filtering, annotation extraction, batch processing.
- **Installation**: `conda install -c bioconda extract_vcf`

## Pitfalls

- **VCF Format**: Requires properly formatted VCF files.
- **Annotation Availability**: Some annotations may not be present in all VCF files.
- **Memory Usage**: Large VCF files may require significant memory.
- **Filtering Criteria**: Complex filtering may require careful parameter tuning.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Extract specific fields
**Args:** `extract_vcf -i variants.vcf -o extracted.csv --fields CHROM POS REF ALT`
**Explanation:** Extracts specified fields from VCF file.

### Filter by quality
**Args:** `extract_vcf -i variants.vcf -o filtered.vcf --filter "QUAL > 30"`
**Explanation:** Filters variants by quality score.

### Extract genotypes
**Args:** `extract_vcf -i variants.vcf -o genotypes.csv --genotypes`
**Explanation:** Extracts genotype information from VCF.

### Extract annotations
**Args:** `extract_vcf -i variants.vcf -o annotations.csv --annotations`
**Explanation:** Extracts variant annotations from VCF.

### Batch processing
**Args:** `extract_vcf -i vcf_files/ -o results/ --batch`
**Explanation:** Processes multiple VCF files in batch mode.