---
name: cryfa
category: utility
description: A secure encryption tool for genomic data with compression
tags: [cryfa, utility, FASTA, encryption, security, genomic-data]
author: oxo-call-community
source_url: "https://github.com/smortezah/cryfa"
---

## Concepts

- **Tool Overview**: cryfa (v2.1+) is an ultra-fast secure encryption tool for genomic data using AES-128 encryption with shuffling and optional compression.
- **Core Function**: Encrypts FASTA, FASTQ, BAM, SAM, and VCF files with authenticated encryption, providing confidentiality, integrity, and authenticity.
- **Input/Output**: Input: FASTA, FASTQ, BAM, SAM, VCF files. Output: Encrypted/compressed binary file (stdout).
- **Three Phases**: (1) Packing: compacts FASTA/FASTQ by factor of 3, (2) Shuffling: randomizes symbol order, (3) Encryption: AES-128 with password-dependent IV.
- **Resistance**: Protects against known-plaintext attacks and low-complexity attacks common in genomic data.
- **Installation**: `conda install -c bioconda cryfa` or build from source.

## Pitfalls

- **Key File**: Must provide a key file with `-k` flag; use `keygen` to generate strong passwords.
- **File Size**: Maximum supported file size is 64 GB; split larger files before encryption.
- **Format Detection**: Automatically detects input format by content, not file extension.
- **Pipe Support**: Uses stdout, enabling easy integration with pipelines.
- **Decryption**: Use `-d` flag for decryption; output goes to stdout.

## Examples

### Encrypt FASTQ file
**Args:** `-k pass.txt reads.fastq > encrypted.cryfa`
**Explanation:** Encrypt and compact a FASTQ file using password from pass.txt. Output to stdout.

### Decrypt file
**Args:** `-k pass.txt -d encrypted.cryfa > decrypted.fastq`
**Explanation:** Decrypt and unpack a cryfa encrypted file back to original format.

### Encrypt without compaction
**Args:** `-k pass.txt -f input.vcf > encrypted.vcf.cryfa`
**Explanation:** Encrypt a VCF file without compression (shuffle and encrypt only).

### Multi-threaded encryption
**Args:** `-k pass.txt -t 8 large_genome.fasta > encrypted.cryfa`
**Explanation:** Use 8 threads for faster encryption of large files.

### Encrypt with verbose output
**Args:** `-k pass.txt -v reads.fastq > encrypted.cryfa`
**Explanation:** Show detailed progress information during encryption.

### Stop shuffling (encrypt only)
**Args:** `-k pass.txt -s input.fasta > encrypted.cryfa`
**Explanation:** Encrypt without shuffling phase for faster processing.

### Generate strong key
**Args:** `keygen > strong_password.txt`
**Explanation:** Generate a cryptographically strong password for use with cryfa.

### Encrypt via pipe
**Args:** `cat reads.fastq | cryfa -k pass.txt > encrypted.cryfa`
**Explanation:** Read input from stdin and encrypt to stdout for pipeline integration.
