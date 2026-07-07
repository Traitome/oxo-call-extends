---
name: piawka
category: population-genomics
description: piawka calculates population statistics from VCF files.
tags: [piawka, population-genomics, vcf, statistics]
author: oxo-call-community
source_url: "https://github.com/novikovalab/piawka"
---

## Concepts

- **Tool Overview**: piawka calculates population statistics.
- **Core Function**: VCF-based population statistics.
- **Algorithm**: Uses AWK-based calculations.
- **Input Format**: Accepts VCF files.
- **Output**: Produces population statistics results.
- **Use Case**: Population genetics, VCF analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large VCF files require memory.
- **Data Quality**: Results depend on VCF quality.
- **Ploidy Handling**: Requires proper ploidy configuration.
- **Runtime**: Calculation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piawka --help`
**Explanation:** Shows available options and usage instructions.

### Calculate statistics
**Args:** `piawka -i input.vcf -o stats_results.txt`
**Explanation:** Calculates population statistics from VCF.

### With parameters
**Args:** `piawka -i input.vcf -p params.yaml -o stats_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piawka -v -i input.vcf -o stats_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piawka -t 4 -i input.vcf -o stats_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `piawka -i input.vcf -o stats_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `piawka -i input.vcf -o stats_results.txt --report report.html`
**Explanation:** Generates HTML report.