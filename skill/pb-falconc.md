---
name: pb-falconc
category: qc
description: pb-falconc provides C utilities for PacBio assembly.
tags: [pb-falconc, qc, pacbio, assembly]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pb-falconc provides assembly utilities.
- **Core Function**: Supports PacBio assembly workflows.
- **Algorithm**: Various C-based utilities for assembly.
- **Input Format**: Accepts assembly data.
- **Output**: Produces processed assembly data.
- **Use Case**: Genome assembly, data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Dependency Management**: Requires C libraries.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbipa --help`
**Explanation:** Shows available options and usage instructions.

### Index assembly
**Args:** `pbipa index assembly.fasta`
**Explanation:** Creates index for assembly.

### Process reads
**Args:** `pbipa process reads.fastq -o processed/`
**Explanation:** Processes sequencing reads.

### Verbose mode
**Args:** `pbipa -v index assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbipa -t 8 process reads.fastq -o processed/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pbipa process reads.fastq -o processed.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate statistics
**Args:** `pbipa stats assembly.fasta -o stats.txt`
**Explanation:** Generates assembly statistics.