---
name: primerclip
category: alignment
description: primerclip is a primer trimming tool for fast alignment-based primer trimming.
tags: [primerclip, alignment, trimming, amplicon]
author: oxo-call-community
source_url: "https://github.com/swiftbiosciences/primerclip"
---

## Concepts

- **Tool Overview**: primerclip trims primers from sequencing reads.
- **Core Function**: Primer trimming.
- **Algorithm**: Uses alignment-based methods.
- **Input Format**: Accepts FASTQ/BAM files.
- **Output**: Produces trimmed reads.
- **Use Case**: Amplicon sequencing, target enrichment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Primer Specificity**: May have false trimming.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `primerclip --help`
**Explanation:** Shows available options and usage instructions.

### Trim primers
**Args:** `primerclip -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims primers from sequencing reads.

### With parameters
**Args:** `primerclip -i reads.fastq -p params.yaml -o trimmed.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `primerclip -v -i reads.fastq -o trimmed.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `primerclip -t 4 -i reads.fastq -o trimmed.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `primerclip -i reads.fastq -o trimmed.bam --bam`
**Explanation:** Outputs in BAM format.

### Generate report
**Args:** `primerclip -i reads.fastq -o trimmed.fastq --report report.html`
**Explanation:** Generates HTML report.