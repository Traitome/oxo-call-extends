---
name: predictosaurus
category: variant-calling
description: predictosaurus performs uncertainty-aware haplotype-based variant effect prediction.
tags: [predictosaurus, variant-calling, effect-prediction, haplotype]
author: oxo-call-community
source_url: "https://github.com/fxwiegand/predictosaurus"
---

## Concepts

- **Tool Overview**: predictosaurus predicts variant effects.
- **Core Function**: Variant effect prediction.
- **Algorithm**: Uses haplotype-based methods.
- **Input Format**: Accepts VCF files.
- **Output**: Produces effect predictions.
- **Use Case**: Variant annotation, clinical genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Prediction Accuracy**: May have false positives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `predictosaurus --help`
**Explanation:** Shows available options and usage instructions.

### Predict variant effects
**Args:** `predictosaurus -i variants.vcf -o effects.txt`
**Explanation:** Predicts effects of genetic variants.

### With parameters
**Args:** `predictosaurus -i variants.vcf -p params.yaml -o effects.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `predictosaurus -v -i variants.vcf -o effects.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `predictosaurus -t 4 -i variants.vcf -o effects.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `predictosaurus -i variants.vcf -o effects.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `predictosaurus -i variants.vcf -o effects.txt --report report.html`
**Explanation:** Generates HTML report.