---
name: rastair
category: variant-calling
description: Rastair performs fast and flexible extraction of methylation information from BAM files.
tags: [rastair, variant-calling, methylation, bam]
author: oxo-call-community
source_url: "https://docs.rastair.com"
---

## Concepts

- **Tool Overview**: rastair extracts methylation.
- **Core Function**: Methylation extraction.
- **Algorithm**: Uses BAM parsing.
- **Input Format**: Accepts BAM files.
- **Output**: Produces methylation data.
- **Use Case**: Epigenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAMs require memory.
- **BAM Quality**: Affects extraction.
- **Parameters**: Must be configured.
- **Runtime**: Extraction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rastair --help`
**Explanation:** Shows available options and usage instructions.

### Extract methylation
**Args:** `rastair extract -i aligned.bam -o methylation.txt`
**Explanation:** Extracts methylation information.

### With parameters
**Args:** `rastair extract -i aligned.bam -p params.yaml -o methylation.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rastair -v extract -i aligned.bam -o methylation.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rastair -t 4 extract -i aligned.bam -o methylation.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With regions
**Args:** `rastair extract -i aligned.bam -r regions.bed -o methylation.txt`
**Explanation:** Extracts specific regions.

### Generate report
**Args:** `rastair extract -i aligned.bam -o methylation.txt --report report.html`
**Explanation:** Generates HTML report.