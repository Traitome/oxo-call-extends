---
name: pbcoretools
category: qc
description: pbcoretools provides CLI tools and add-ons for PacBio's core APIs.
tags: [pbcoretools, qc, pacbio, cli-tools]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbcoretools extends PacBio core APIs.
- **Core Function**: Provides CLI tools for PacBio data processing.
- **Algorithm**: Various data processing algorithms.
- **Input Format**: Accepts PacBio sequencing data.
- **Output**: Produces processed data and reports.
- **Use Case**: PacBio data analysis, quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Format**: Requires PacBio-specific formats.
- **Dependency Management**: Requires pbcore library.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbcoretools --help`
**Explanation:** Shows available options and usage instructions.

### Convert data
**Args:** `pbcoretools convert input.bam output.fastq`
**Explanation:** Converts BAM to FASTQ.

### Validate data
**Args:** `pbcoretools validate input.subreads.bam`
**Explanation:** Validates PacBio data format.

### Verbose mode
**Args:** `pbcoretools -v convert input.bam output.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbcoretools -t 4 convert input.bam output.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbcoretools convert --format fasta input.bam output.fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `pbcoretools report input.bam -o report.html`
**Explanation:** Generates HTML report.