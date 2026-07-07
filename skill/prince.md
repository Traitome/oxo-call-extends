---
name: prince
category: utility
description: prince estimates VNTR copy number from NGS data.
tags: [prince, utility, vntr, copy-number]
author: oxo-call-community
source_url: "https://github.com/WGS-TB/PythonPrince"
---

## Concepts

- **Tool Overview**: prince analyzes tandem repeats.
- **Core Function**: VNTR copy number estimation.
- **Algorithm**: Uses read depth methods.
- **Input Format**: Accepts BAM/FASTQ files.
- **Output**: Produces copy number estimates.
- **Use Case**: Repeat expansion disorders, population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Repeat Complexity**: May have estimation errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prince --help`
**Explanation:** Shows available options and usage instructions.

### Estimate VNTR
**Args:** `prince -i aligned.bam -o vntr_results.txt`
**Explanation:** Estimates VNTR copy number from sequencing data.

### With parameters
**Args:** `prince -i aligned.bam -p params.yaml -o vntr_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prince -v -i aligned.bam -o vntr_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prince -t 4 -i aligned.bam -o vntr_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prince -i aligned.bam -o vntr_results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `prince -i aligned.bam -o vntr_results.txt --report report.html`
**Explanation:** Generates HTML report.