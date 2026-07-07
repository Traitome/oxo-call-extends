---
name: pypints
category: alignment
description: PINTS identifies transcription start sites from nascent transcript sequencing data.
tags: [pypints, alignment, transcription, tss]
author: oxo-call-community
source_url: "https://pints.yulab.org"
---

## Concepts

- **Tool Overview**: pypints identifies TSS peaks.
- **Core Function**: Peak calling.
- **Algorithm**: Uses statistical modeling.
- **Input Format**: Accepts BAM/BED files.
- **Output**: Produces TSS peaks.
- **Use Case**: Transcription analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Threshold Selection**: Affects peak calling.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pypints --help`
**Explanation:** Shows available options and usage instructions.

### Call peaks
**Args:** `pypints call -i aligned.bam -o peaks.bed`
**Explanation:** Identifies transcription start sites.

### With parameters
**Args:** `pypints call -i aligned.bam -p params.yaml -o peaks.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pypints -v call -i aligned.bam -o peaks.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pypints -t 4 call -i aligned.bam -o peaks.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Filter peaks
**Args:** `pypints filter -i peaks.bed -q 0.05 -o filtered.bed`
**Explanation:** Filters peaks by significance.

### Generate report
**Args:** `pypints call -i aligned.bam -o peaks.bed --report report.html`
**Explanation:** Generates HTML report.