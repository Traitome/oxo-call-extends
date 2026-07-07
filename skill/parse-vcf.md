---
name: parse-vcf
category: formatting
description: parse-vcf provides VCF parsing and manipulation utilities.
tags: [parse-vcf, formatting, vcf, variant-analysis]
author: oxo-call-community
source_url: "https://github.com/david-a-parry/parse_vcf.py"
---

## Concepts

- **Tool Overview**: parse-vcf parses and processes VCF files.
- **Core Function**: Manipulates and analyzes variant call format data.
- **Algorithm**: Parses VCF format and provides query methods.
- **Input Format**: Accepts VCF files.
- **Output**: Produces processed variants and statistics.
- **Use Case**: Variant analysis, VCF manipulation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large VCF files require memory.
- **Format Compliance**: Requires standard VCF format.
- **Compression**: May need decompression for gzipped files.
- **Runtime**: Processing large files may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parse-vcf --help`
**Explanation:** Shows available options and usage instructions.

### Parse VCF
**Args:** `parse-vcf -i input.vcf -o output.txt`
**Explanation:** Parses and processes VCF file.

### Filter by quality
**Args:** `parse-vcf -i input.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters variants by quality score.

### Verbose mode
**Args:** `parse-vcf -v -i input.vcf -o output.txt`
**Explanation:** Runs with verbose output.

### Extract specific fields
**Args:** `parse-vcf -i input.vcf -f CHROM,POS,REF,ALT -o output.txt`
**Explanation:** Extracts specific fields from VCF.

### Output format
**Args:** `parse-vcf -i input.vcf -o output.json --json`
**Explanation:** Outputs in JSON format.

### Count variants
**Args:** `parse-vcf -i input.vcf --count`
**Explanation:** Counts total variants.