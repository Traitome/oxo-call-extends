---
name: pbh5tools
category: qc
description: pbh5tools provides utilities for interrogating PacBio HDF5 files.
tags: [pbh5tools, qc, pacbio, hdf5]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbh5tools"
---

## Concepts

- **Tool Overview**: pbh5tools analyzes PacBio HDF5 files.
- **Core Function**: Interrogates and processes HDF5 data.
- **Algorithm**: Uses HDF5 file operations.
- **Input Format**: Accepts cmp.h5, bas.h5 files.
- **Output**: Produces extracted data and reports.
- **Use Case**: PacBio data analysis, quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large HDF5 files require memory.
- **File Format**: Requires PacBio-specific HDF5 format.
- **Dependency Management**: Requires HDF5 libraries.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbh5tools --help`
**Explanation:** Shows available options and usage instructions.

### Extract reads
**Args:** `pbh5tools fasta input.bas.h5 -o reads.fasta`
**Explanation:** Extracts reads in FASTA format.

### Get statistics
**Args:** `pbh5tools stats input.bas.h5 -o stats.txt`
**Explanation:** Generates statistics from HDF5 file.

### Verbose mode
**Args:** `pbh5tools -v fasta input.bas.h5 -o reads.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbh5tools -t 4 fasta input.bas.h5 -o reads.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbh5tools fastq input.bas.h5 -o reads.fastq`
**Explanation:** Outputs in FASTQ format.

### Convert format
**Args:** `pbh5tools convert input.bas.h5 -o output.bam`
**Explanation:** Converts HDF5 to BAM format.