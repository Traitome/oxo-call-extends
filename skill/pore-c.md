---
name: pore-c
category: programming
description: pore-c processes Pore-C concatemers for 3D genome analysis.
tags: [pore-c, programming, nanopore, 3d-genome]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/pore-c"
---

## Concepts

- **Tool Overview**: pore-c analyzes Pore-C data.
- **Core Function**: Concatemer processing.
- **Algorithm**: Uses nanopore-specific methods.
- **Input Format**: Accepts BAM/FASTQ files.
- **Output**: Produces 3D genome interactions.
- **Use Case**: 3D genomics, chromatin structure.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Complexity**: May have steep learning curve.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pore-c --help`
**Explanation:** Shows available options and usage instructions.

### Process Pore-C data
**Args:** `pore-c process -i reads.fastq -o output/`
**Explanation:** Processes Pore-C concatemers.

### With parameters
**Args:** `pore-c process -i reads.fastq -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pore-c -v process -i reads.fastq -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pore-c -t 4 process -i reads.fastq -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pore-c process -i reads.fastq -o output.bam --bam`
**Explanation:** Outputs in BAM format.

### Generate report
**Args:** `pore-c process -i reads.fastq -o output/ --report report.html`
**Explanation:** Generates HTML report.