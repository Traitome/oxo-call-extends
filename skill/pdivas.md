---
name: pdivas
category: variant-calling
description: PDIVAS predicts pathogenicity of deep-intronic variants causing aberrant splicing.
tags: [pdivas, variant-calling, splicing, pathogenicity]
author: oxo-call-community
source_url: "https://github.com/shiro-kur/PDIVAS"
---

## Concepts

- **Tool Overview**: PDIVAS predicts variant pathogenicity.
- **Core Function**: Analyzes deep-intronic splicing variants.
- **Algorithm**: Uses deep learning prediction model.
- **Input Format**: Accepts VCF variant files.
- **Output**: Produces pathogenicity predictions.
- **Use Case**: Clinical genetics, variant interpretation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large VCF files require memory.
- **Variant Type**: Designed for intronic variants.
- **Splicing Context**: Requires proper annotation.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pdivas --help`
**Explanation:** Shows available options and usage instructions.

### Predict pathogenicity
**Args:** `pdivas -i variants.vcf -o predictions.txt`
**Explanation:** Predicts pathogenicity of variants.

### With annotation
**Args:** `pdivas -i variants.vcf -a annotation.gtf -o predictions.txt`
**Explanation:** Uses gene annotation for prediction.

### Verbose mode
**Args:** `pdivas -v -i variants.vcf -o predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pdivas -t 4 -i variants.vcf -o predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pdivas -i variants.vcf -o predictions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pdivas -i variants.vcf -o predictions.txt --report report.html`
**Explanation:** Generates HTML report.