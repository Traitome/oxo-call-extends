---
name: popdel
category: variant-calling
description: popdel detects structural deletions in population-scale WGS data.
tags: [popdel, variant-calling, structural-variation, population]
author: oxo-call-community
source_url: "https://github.com/kehrlab/PopDel"
---

## Concepts

- **Tool Overview**: popdel calls structural deletions.
- **Core Function**: Population-scale deletion detection.
- **Algorithm**: Uses paired-end read mapping methods.
- **Input Format**: Accepts BAM/SAM alignment files.
- **Output**: Produces VCF with deletion calls.
- **Use Case**: Population genetics, structural variation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Detection Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `popdel --help`
**Explanation:** Shows available options and usage instructions.

### Call deletions
**Args:** `popdel call -i alignment.bam -o deletions.vcf`
**Explanation:** Detects structural deletions from WGS data.

### With parameters
**Args:** `popdel call -i alignment.bam -p params.yaml -o deletions.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `popdel -v call -i alignment.bam -o deletions.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `popdel -t 4 call -i alignment.bam -o deletions.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `popdel call -i alignment.bam -o deletions.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `popdel call -i alignment.bam -o deletions.vcf --report report.html`
**Explanation:** Generates HTML report.