---
name: bamhash
category: formatting
description: BamHash - Hash BAM and FASTQ files to verify data integrity
tags: [bamhash, formatting, FASTQ, BAM, data-integrity, checksum]
author: oxo-call-community
source_url: "https://github.com/DecodeGenetics/BamHash"
---

## Concepts

- **Tool Overview**: BamHash generates cryptographic hashes for BAM and FASTQ files to verify data integrity and detect corruption. Version 2.0.
- **Core Function**: Computes hash values for sequencing data files to ensure data integrity.
- **Hash Generation**: Creates unique hash signatures for BAM and FASTQ files.
- **Integrity Verification**: Compares computed hashes against expected values to detect corruption.
- **FASTQ Support**: Handles both raw FASTQ reads and aligned BAM files.
- **Input/Output**: Accepts BAM or FASTQ files, outputs hash values and verification results.
- **Installation**: `conda install -c bioconda bamhash`.

## Pitfalls

- **File Size**: Very large files may take time to hash.
- **Memory Usage**: Large BAM files may require significant memory.
- **Hash Algorithm**: Different hash algorithms produce different results. Use consistent algorithm.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Hash BAM file
**Args:** `bamhash -i input.bam -o hash.txt`
**Explanation:** Computes hash for BAM file.

### Hash FASTQ file
**Args:** `bamhash -i reads.fastq -o hash.txt`
**Explanation:** Computes hash for FASTQ file.

### Verify hash
**Args:** `bamhash -i input.bam --verify hash.txt`
**Explanation:** Verifies BAM file against previously computed hash.

### Use SHA256 algorithm
**Args:** `bamhash -i input.bam -o hash.txt --algorithm sha256`
**Explanation:** Uses SHA256 algorithm for hash computation.

### Hash multiple files
**Args:** `bamhash -i sample1.bam sample2.bam -o hashes.txt`
**Explanation:** Computes hashes for multiple BAM files.

### Include read groups
**Args:** `bamhash -i input.bam -o hash.txt --include-rg`
**Explanation:** Includes read group information in hash computation.

### Display help
**Args:** `bamhash --help`
**Explanation:** Shows all available command-line options and usage information.