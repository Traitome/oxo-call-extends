---
name: pyclone
category: variant-calling
description: PyClone is a probabilistic model for inferring clonal population structure from deep NGS sequencing data.
tags: [pyclone, variant-calling, clonal-analysis, cancer-genomics]
author: oxo-call-community
source_url: "https://github.com/Roth-Lab/pyclone/"
---

## Concepts

- **Tool Overview**: pyclone infers clonal structure.
- **Core Function**: Clonal population inference.
- **Algorithm**: Uses Bayesian probabilistic model.
- **Input Format**: Accepts variant allele frequencies.
- **Output**: Produces clonal assignments.
- **Use Case**: Cancer sequencing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Sample Heterogeneity**: Affects inference.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyclone --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pyclone run -i variants.tsv -o results/`
**Explanation:** Runs clonal inference on variant data.

### With parameters
**Args:** `pyclone run -i variants.tsv -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyclone -v run -i variants.tsv -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyclone -t 4 run -i variants.tsv -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Bootstrap analysis
**Args:** `pyclone bootstrap -i variants.tsv -n 100 -o bootstrap/`
**Explanation:** Performs bootstrap analysis.

### Generate report
**Args:** `pyclone run -i variants.tsv -o results/ --report report.html`
**Explanation:** Generates HTML report.