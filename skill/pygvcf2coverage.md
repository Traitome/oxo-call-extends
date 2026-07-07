---
name: pygvcf2coverage
category: formatting
description: pygvcf2coverage extracts coverage information from gVCF files.
tags: [pygvcf2coverage, formatting, vcf, coverage]
author: oxo-call-community
source_url: "https://github.com/varda/varda2_preprocessing"
---

## Concepts

- **Tool Overview**: pygvcf2coverage extracts coverage.
- **Core Function**: Coverage extraction from gVCF.
- **Algorithm**: Uses VCF parsing.
- **Input Format**: Accepts gVCF files.
- **Output**: Produces coverage data.
- **Use Case**: Coverage analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Format Requirements**: Must be gVCF format.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pygvcf2coverage --help`
**Explanation:** Shows available options and usage instructions.

### Extract coverage
**Args:** `pygvcf2coverage -i input.gvcf -o coverage.txt`
**Explanation:** Extracts coverage from gVCF file.

### With parameters
**Args:** `pygvcf2coverage -i input.gvcf -p params.yaml -o coverage.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pygvcf2coverage -v -i input.gvcf -o coverage.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pygvcf2coverage -t 4 -i input.gvcf -o coverage.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Bed region
**Args:** `pygvcf2coverage -i input.gvcf -b regions.bed -o coverage.txt`
**Explanation:** Extracts coverage for specific regions.

### Generate report
**Args:** `pygvcf2coverage -i input.gvcf -o coverage.txt --report report.html`
**Explanation:** Generates HTML report.