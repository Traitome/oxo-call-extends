---
name: rasusa
category: alignment
description: RasUSA randomly subsamples sequencing reads or alignments to reduce dataset size.
tags: [rasusa, alignment, subsampling, sequencing]
author: oxo-call-community
source_url: "https://github.com/mbhall88/rasusa"
---

## Concepts

- **Tool Overview**: rasusa subsamples reads.
- **Core Function**: Read subsampling.
- **Algorithm**: Uses random sampling.
- **Input Format**: Accepts FASTQ/BAM files.
- **Output**: Produces subsampled files.
- **Use Case**: Data reduction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sampling Rate**: Affects results.
- **Parameters**: Must be configured.
- **Runtime**: Subsampling may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rasusa --help`
**Explanation:** Shows available options and usage instructions.

### Subsample reads
**Args:** `rasusa subsample -i reads.fastq -o subsampled.fastq -n 1000000`
**Explanation:** Subsamples to 1M reads.

### With parameters
**Args:** `rasusa subsample -i reads.fastq -p params.yaml -o subsampled.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rasusa -v subsample -i reads.fastq -o subsampled.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rasusa -t 4 subsample -i reads.fastq -o subsampled.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With coverage
**Args:** `rasusa subsample -i reads.fastq -c 30 -o subsampled.fastq`
**Explanation:** Subsamples to 30x coverage.

### Generate report
**Args:** `rasusa subsample -i reads.fastq -o subsampled.fastq --report report.html`
**Explanation:** Generates HTML report.