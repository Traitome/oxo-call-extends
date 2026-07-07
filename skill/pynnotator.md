---
name: pynnotator
category: annotation
description: PyNnotator is a Python framework for annotating VCF files using multiple annotation tools.
tags: [pynnotator, annotation, vcf, variant-annotation]
author: oxo-call-community
source_url: "http://github.com/raonyguimaraes/pynnotator"
---

## Concepts

- **Tool Overview**: pynnotator annotates VCF files.
- **Core Function**: Variant annotation.
- **Algorithm**: Uses multiple annotation sources.
- **Input Format**: Accepts VCF files.
- **Output**: Produces annotated VCF.
- **Use Case**: Variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large VCFs require memory.
- **Annotation Sources**: Must be configured.
- **Network Access**: May need internet.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pynnotator --help`
**Explanation:** Shows available options and usage instructions.

### Annotate VCF
**Args:** `pynnotator annotate -i variants.vcf -o annotated.vcf`
**Explanation:** Annotates VCF with multiple tools.

### With parameters
**Args:** `pynnotator annotate -i variants.vcf -p params.yaml -o annotated.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pynnotator -v annotate -i variants.vcf -o annotated.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pynnotator -t 4 annotate -i variants.vcf -o annotated.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Filter annotations
**Args:** `pynnotator filter -i annotated.vcf -q PASS -o filtered.vcf`
**Explanation:** Filters annotations by quality.

### Generate report
**Args:** `pynnotator annotate -i variants.vcf -o annotated.vcf --report report.html`
**Explanation:** Generates HTML report.