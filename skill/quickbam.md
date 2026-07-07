---
name: quickbam
category: formatting
description: QuickBAM provides parallel BAM file access API for high throughput sequence analysis informatics.
tags: [quickbam, formatting, bam, parallel]
author: oxo-call-community
source_url: "https://gitlab.com/yiq/quickbam/-/tree/master/"
---

## Concepts

- **Tool Overview**: quickbam provides BAM access.
- **Core Function**: Parallel BAM processing.
- **Algorithm**: Uses multi-threading.
- **Input Format**: Accepts BAM files.
- **Output**: Produces processed data.
- **Use Case**: High-throughput sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAMs require memory.
- **Index Files**: Must be present.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quickbam --help`
**Explanation:** Shows available options and usage instructions.

### Process BAM
**Args:** `quickbam process -i input.bam -o output.bam`
**Explanation:** Processes BAM file in parallel.

### With parameters
**Args:** `quickbam process -i input.bam -p params.yaml -o output.bam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quickbam -v process -i input.bam -o output.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quickbam -t 4 process -i input.bam -o output.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Filter reads
**Args:** `quickbam filter -i input.bam -q 30 -o filtered.bam`
**Explanation:** Filters reads by quality.

### Generate report
**Args:** `quickbam process -i input.bam -o output.bam --report report.html`
**Explanation:** Generates HTML report.