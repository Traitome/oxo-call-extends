---
name: pychopper
category: utility
description: pychopper identifies, orients and rescues full length cDNA reads from nanopore sequencing data.
tags: [pychopper, utility, nanopore, cdna-processing]
author: oxo-call-community
source_url: "https://github.com/epi2me-labs/pychopper"
---

## Concepts

- **Tool Overview**: pychopper processes cDNA reads.
- **Core Function**: cDNA read processing.
- **Algorithm**: Uses sequence analysis.
- **Input Format**: Accepts FASTQ reads.
- **Output**: Produces processed reads.
- **Use Case**: Nanopore sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Adapter Sequences**: Must be correctly specified.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pychopper --help`
**Explanation:** Shows available options and usage instructions.

### Process cDNA reads
**Args:** `pychopper -i reads.fastq -o processed.fastq -b barcodes.fastq`
**Explanation:** Processes and demultiplexes cDNA reads.

### With parameters
**Args:** `pychopper -i reads.fastq -p params.yaml -o processed.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pychopper -v -i reads.fastq -o processed.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pychopper -t 4 -i reads.fastq -o processed.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Rescale quality
**Args:** `pychopper --rescale -i reads.fastq -o processed.fastq`
**Explanation:** Rescales quality scores.

### Generate report
**Args:** `pychopper -i reads.fastq -o processed.fastq --report report.html`
**Explanation:** Generates HTML report.