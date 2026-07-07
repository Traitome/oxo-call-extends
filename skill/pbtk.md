---
name: pbtk
category: qc
description: pbtk provides PacBio BAM toolkit utilities.
tags: [pbtk, qc, pacbio, bam]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbtk processes PacBio BAM files.
- **Core Function**: Provides BAM file utilities.
- **Algorithm**: Various BAM processing operations.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces processed BAM files.
- **Use Case**: BAM file processing, data conversion.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAM files require memory.
- **Format Compliance**: Requires PacBio-specific BAM format.
- **Dependency Management**: Requires proper installation.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbtk --help`
**Explanation:** Shows available options and usage instructions.

### Convert BAM
**Args:** `pbtk convert input.bam output.fastq`
**Explanation:** Converts BAM to FASTQ format.

### Filter reads
**Args:** `pbtk filter -q 30 input.bam output.bam`
**Explanation:** Filters reads by quality score.

### Verbose mode
**Args:** `pbtk -v convert input.bam output.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbtk -t 4 convert input.bam output.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbtk convert input.bam output.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate statistics
**Args:** `pbtk stats input.bam -o stats.txt`
**Explanation:** Generates BAM file statistics.