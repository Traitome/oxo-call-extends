---
name: picard-slim
category: formatting
description: picard-slim provides Java tools for working with NGS data in BAM format.
tags: [picard-slim, formatting, bam, ngs]
author: oxo-call-community
source_url: "http://broadinstitute.github.io/picard/"
---

## Concepts

- **Tool Overview**: picard-slim processes NGS data in BAM format.
- **Core Function**: BAM/SAM file manipulation tools.
- **Algorithm**: Uses Java-based processing methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces processed BAM/SAM results.
- **Use Case**: NGS data processing, BAM manipulation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAM files require memory.
- **File Quality**: Results depend on BAM quality.
- **Java Dependencies**: Requires Java runtime.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `picard-slim --help`
**Explanation:** Shows available options and usage instructions.

### Process BAM file
**Args:** `picard-slim -i input.bam -o output.bam`
**Explanation:** Processes BAM file.

### With parameters
**Args:** `picard-slim -i input.bam -p params.yaml -o output.bam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `picard-slim -v -i input.bam -o output.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `picard-slim -t 4 -i input.bam -o output.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `picard-slim -i input.bam -o output.sam --sam`
**Explanation:** Outputs in SAM format.

### Generate report
**Args:** `picard-slim -i input.bam -o output.bam --report report.html`
**Explanation:** Generates HTML report.