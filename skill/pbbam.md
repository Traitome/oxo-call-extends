---
name: pbbam
category: qc
description: pbBAM provides a C++ library for reading and writing PacBio BAM files.
tags: [pbbam, qc, pacbio, bam]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbam"
---

## Concepts

- **Tool Overview**: pbBAM is a C++ library for BAM file operations.
- **Core Function**: Reads and writes PacBio BAM files.
- **Algorithm**: Uses optimized BAM file handling.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces BAM files and provides library APIs.
- **Use Case**: PacBio sequencing data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAM files require memory.
- **Format Compliance**: Requires PacBio-specific BAM format.
- **Dependency Management**: Requires C++ build system.
- **Runtime**: Processing large files may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbindex --help`
**Explanation:** Shows available options and usage instructions.

### Index BAM file
**Args:** `pbindex input.bam`
**Explanation:** Creates index for BAM file.

### Merge BAM files
**Args:** `pbmerge -o merged.bam input1.bam input2.bam`
**Explanation:** Merges multiple BAM files.

### Verbose mode
**Args:** `pbindex -v input.bam`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `pbmerge -o merged.bam --format bam input1.bam`
**Explanation:** Specifies output format.

### Filter reads
**Args:** `pbfilter -q 30 -o filtered.bam input.bam`
**Explanation:** Filters reads by quality score.

### Generate statistics
**Args:** `pbstats input.bam -o stats.txt`
**Explanation:** Generates BAM file statistics.