---
name: read-it-and-keep
category: utility
description: Read-It-And-Keep removes contamination from sequencing reads while preserving biological signals.
tags: [read-it-and-keep, utility, contamination-removal, quality-control]
author: oxo-call-community
source_url: "https://github.com/GenomePathogenAnalysisService/read-it-and-keep"
---

## Concepts

- **Tool Overview**: read-it-and-keep removes contamination.
- **Core Function**: Contamination removal.
- **Algorithm**: Uses filtering methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces clean reads.
- **Use Case**: Quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Contamination Database**: Must be up-to-date.
- **Parameters**: Must be configured.
- **Runtime**: Filtering may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `read-it-and-keep --help`
**Explanation:** Shows available options and usage instructions.

### Remove contamination
**Args:** `read-it-and-keep remove -i reads.fastq -o clean_reads.fastq`
**Explanation:** Removes contamination.

### With parameters
**Args:** `read-it-and-keep remove -i reads.fastq -p params.yaml -o clean_reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `read-it-and-keep -v remove -i reads.fastq -o clean_reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `read-it-and-keep -t 4 remove -i reads.fastq -o clean_reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `read-it-and-keep remove -i reads.fastq -d contamination_db.fasta -o clean_reads.fastq`
**Explanation:** Uses contamination database.

### Generate report
**Args:** `read-it-and-keep remove -i reads.fastq -o clean_reads.fastq --report report.html`
**Explanation:** Generates HTML report.