---
name: qsignature
category: variant-calling
description: QSignature detects potential sample mix-ups using distance measurements between SNP profiles.
tags: [qsignature, variant-calling, sample-mixup, snp]
author: oxo-call-community
source_url: "http://sourceforge.net/p/adamajava/wiki/Home/"
---

## Concepts

- **Tool Overview**: qsignature detects sample mix-ups.
- **Core Function**: Sample verification.
- **Algorithm**: Uses distance metrics.
- **Input Format**: Accepts SNP data.
- **Output**: Produces similarity scores.
- **Use Case**: Quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **SNP Coverage**: Must be sufficient.
- **Thresholds**: Must be set.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qsignature --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `qsignature analyze -i snp_data.vcf -o results.txt`
**Explanation:** Detects sample mix-ups.

### With parameters
**Args:** `qsignature analyze -i snp_data.vcf -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qsignature -v analyze -i snp_data.vcf -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qsignature -t 4 analyze -i snp_data.vcf -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Compare samples
**Args:** `qsignature compare -i sample1.vcf sample2.vcf -o comparison.txt`
**Explanation:** Compares two samples.

### Generate report
**Args:** `qsignature analyze -i snp_data.vcf -o results.txt --report report.html`
**Explanation:** Generates HTML report.