---
name: reaper
category: qc
description: REAPER is a tool for demultiplexing, trimming and filtering sequencing data for quality control.
tags: [reaper, qc, demultiplexing, trimming]
author: oxo-call-community
source_url: "https://www.ebi.ac.uk/~stijn/reaper/reaper.html"
---

## Concepts

- **Tool Overview**: reaper processes reads.
- **Core Function**: Read processing.
- **Algorithm**: Uses filtering methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces clean reads.
- **Use Case**: Quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects processing.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reaper --help`
**Explanation:** Shows available options and usage instructions.

### Process reads
**Args:** `reaper process -i reads.fastq -o clean_reads.fastq`
**Explanation:** Processes sequencing reads.

### With parameters
**Args:** `reaper process -i reads.fastq -p params.yaml -o clean_reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reaper -v process -i reads.fastq -o clean_reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reaper -t 4 process -i reads.fastq -o clean_reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Trim reads
**Args:** `reaper trim -i reads.fastq -q 20 -o trimmed_reads.fastq`
**Explanation:** Trims low-quality bases.

### Generate report
**Args:** `reaper process -i reads.fastq -o clean_reads.fastq --report report.html`
**Explanation:** Generates HTML report.