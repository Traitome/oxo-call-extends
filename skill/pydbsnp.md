---
name: pydbsnp
category: variant-calling
description: pydbsnp provides an interface with dbSNP VCF data for variant annotation and querying.
tags: [pydbsnp, variant-calling, dbsnp, vcf]
author: oxo-call-community
source_url: "https://gitlab.com/aaylward/pydbsnp"
---

## Concepts

- **Tool Overview**: pydbsnp accesses dbSNP data.
- **Core Function**: dbSNP query interface.
- **Algorithm**: Uses VCF parsing.
- **Input Format**: Accepts VCF files.
- **Output**: Produces variant annotations.
- **Use Case**: Variant annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Data Quality**: Results depend on input quality.
- **Database Updates**: Requires regular updates.
- **Query Complexity**: May affect performance.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pydbsnp --help`
**Explanation:** Shows available options and usage instructions.

### Query variants
**Args:** `pydbsnp query -i variants.vcf -d dbsnp.vcf -o annotated.vcf`
**Explanation:** Annotates variants with dbSNP data.

### With parameters
**Args:** `pydbsnp query -i variants.vcf -p params.yaml -o annotated.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pydbsnp -v query -i variants.vcf -o annotated.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pydbsnp -t 4 query -i variants.vcf -o annotated.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Download dbSNP
**Args:** `pydbsnp download -o dbsnp.vcf`
**Explanation:** Downloads dbSNP database.

### Generate report
**Args:** `pydbsnp query -i variants.vcf -o annotated.vcf --report report.html`
**Explanation:** Generates HTML report.