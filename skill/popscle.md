---
name: popscle
category: expression
description: popscle provides tools for single-cell genomics including Demuxlet.
tags: [popscle, expression, single-cell, demuxlet]
author: oxo-call-community
source_url: "https://github.com/statgen/popscle"
---

## Concepts

- **Tool Overview**: popscle analyzes single-cell data.
- **Core Function**: Demultiplexing and analysis.
- **Algorithm**: Uses Demuxlet/Freemuxlet methods.
- **Input Format**: Accepts BAM/VCF files.
- **Output**: Produces demultiplexed results.
- **Use Case**: Single-cell genomics, population analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Demultiplexing Accuracy**: May have assignment errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `popscle --help`
**Explanation:** Shows available options and usage instructions.

### Run Demuxlet
**Args:** `popscle demuxlet --sam input.bam --vcf genotypes.vcf --out demuxlet_result`
**Explanation:** Demultiplexes single-cell data.

### With parameters
**Args:** `popscle demuxlet --sam input.bam --vcf genotypes.vcf --params params.yaml --out demuxlet_result`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `popscle -v demuxlet --sam input.bam --vcf genotypes.vcf --out demuxlet_result`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `popscle -t 4 demuxlet --sam input.bam --vcf genotypes.vcf --out demuxlet_result`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `popscle demuxlet --sam input.bam --vcf genotypes.vcf --out result.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `popscle demuxlet --sam input.bam --vcf genotypes.vcf --out demuxlet_result --report report.html`
**Explanation:** Generates HTML report.