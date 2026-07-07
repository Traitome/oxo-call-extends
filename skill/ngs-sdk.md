---
name: ngs-sdk
category: utility
description: NCBI NGS SDK provides tools for accessing and processing sequencing data.
tags: [ngs-sdk, utility, ncbi, sequencing]
author: oxo-call-community
source_url: "https://github.com/ncbi/ngs"
---

## Concepts

- **Tool Overview**: NCBI NGS SDK provides APIs for reading and processing sequencing data.
- **Core Function**: Enables programmatic access to SRA and other sequencing data formats.
- **Algorithm**: Abstracts sequencing data access across different formats.
- **Input Format**: Accepts SRA files, BAM, FASTQ, and other sequencing formats.
- **Output**: Provides data access and processing capabilities.
- **Use Case**: Bioinformatics tool development, data processing pipelines, and SRA data access.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **API Changes**: Library API may change between versions.
- **Memory Usage**: Large datasets require memory.
- **Dependency**: Requires proper library linkage.
- **Build Requirements**: May require specific build tools.
- **Documentation**: Limited documentation for some features.

## Examples

### Display help
**Args:** `ngs-sdk --help`
**Explanation:** Shows available options and usage instructions.

### List SRA runs
**Args:** `ngs-sdk list SRP000001`
**Explanation:** Lists runs in SRA project.

### Download SRA data
**Args:** `ngs-sdk download SRR1234567 -o output/`
**Explanation:** Downloads SRA run to output directory.

### Convert SRA to FASTQ
**Args:** `ngs-sdk sra-to-fastq SRR1234567 -o reads.fastq`
**Explanation:** Converts SRA to FASTQ format.

### Validate SRA file
**Args:** `ngs-sdk validate SRR1234567.sra`
**Explanation:** Validates SRA file integrity.

### Extract reads
**Args:** `ngs-sdk extract SRR1234567.sra -r 1-1000 -o subset.fastq`
**Explanation:** Extracts subset of reads.

### Version info
**Args:** `ngs-sdk version`
**Explanation:** Shows version information.