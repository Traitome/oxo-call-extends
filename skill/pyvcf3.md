---
name: pyvcf3
category: variant-calling
description: PyVCF3 is a Variant Call Format (VCF) reader and writer for Python.
tags: [pyvcf3, variant-calling, vcf, variants]
author: oxo-call-community
source_url: "http://pyvcf.readthedocs.org/en/latest/index.html"
---

## Concepts

- **Tool Overview**: pyvcf3 reads VCF files.
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
**Args:** `pyvcf3 --help`
**Explanation:** Shows available options and usage instructions.

### Read VCF
**Args:** `pyvcf3 read -i variants.vcf -o parsed.txt`
**Explanation:** Parses VCF file.

### With parameters
**Args:** `pyvcf3 read -i variants.vcf -p params.yaml -o parsed.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyvcf3 -v read -i variants.vcf -o parsed.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyvcf3 -t 4 read -i variants.vcf -o parsed.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Filter variants
**Args:** `pyvcf3 filter -i variants.vcf -q 0.05 -o filtered.vcf`
**Explanation:** Filters by quality.

### Generate report
**Args:** `pyvcf3 read -i variants.vcf -o parsed.txt --report report.html`
**Explanation:** Generates HTML report.