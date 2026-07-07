---
name: pyvcf
category: variant-calling
description: PyVCF is a Variant Call Format (VCF) reader and writer for Python.
tags: [pyvcf, variant-calling, vcf, variants]
author: oxo-call-community
source_url: "https://github.com/jamescasbon/PyVCF"
---

## Concepts

- **Tool Overview**: pyvcf reads VCF files.
- **Core Function**: VCF parsing.
- **Algorithm**: Uses file parsing.
- **Input Format**: Accepts VCF files.
- **Output**: Produces variant data.
- **Use Case**: Variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **VCF Version**: Must be supported.
- **Compression**: Must be handled.
- **Runtime**: Parsing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyvcf --help`
**Explanation:** Shows available options and usage instructions.

### Read VCF
**Args:** `pyvcf read -i variants.vcf -o parsed.txt`
**Explanation:** Parses VCF file.

### With parameters
**Args:** `pyvcf read -i variants.vcf -p params.yaml -o parsed.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyvcf -v read -i variants.vcf -o parsed.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyvcf -t 4 read -i variants.vcf -o parsed.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Filter variants
**Args:** `pyvcf filter -i variants.vcf -q 0.05 -o filtered.vcf`
**Explanation:** Filters by quality.

### Generate report
**Args:** `pyvcf read -i variants.vcf -o parsed.txt --report report.html`
**Explanation:** Generates HTML report.