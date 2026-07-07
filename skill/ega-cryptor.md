---
name: ega-cryptor
category: utility
description: "EGA Cryptor v2.0.0 is a tool designed to encrypt files compliant with the European Genome-phenome Archive (EGA)"
tags: [ega-cryptor, utility, encryption, data-security, EGA]
author: oxo-call-community
source_url: "https://ega-archive.org/submission/data/file-preparation/egacryptor/"
---

## Concepts

- **Tool Overview**: EGA Cryptor is a Java-based encryption tool for preparing files for submission to the European Genome-phenome Archive (EGA).
- **Core Function**: Encrypts sensitive genomic data files according to EGA standards, generating encrypted files with MD5 checksums.
- **Input/Output**: Input: Genomic data files (FASTQ, BAM, VCF, etc.). Output: Encrypted files (.gpg), MD5 checksum files.
- **Algorithm**: Uses GPG encryption with EGA-specific key management and file handling protocols.
- **Key Features**: EGA-compliant encryption, directory structure preservation, MD5 checksum generation, batch processing, FTP/Aspera upload compatibility.
- **Installation**: `conda install -c bioconda ega-cryptor` or download from EGA website

## Pitfalls

- **Java Requirement**: Requires Java Runtime Environment (JRE) to be installed.
- **Encryption Keys**: Requires proper EGA encryption keys and certificates.
- **File Size**: Large files require significant disk space for encrypted output.
- **Memory Usage**: Java application may require substantial RAM for large files.
- **Security**: Encryption keys must be kept secure and not shared.

## Examples

### Encrypt single file
**Args:** `ega-cryptor encrypt input.fastq`
**Explanation:** Encrypts a single file for EGA submission.

### Encrypt directory
**Args:** `ega-cryptor encrypt -r /path/to/data/`
**Explanation:** Recursively encrypts all files in directory.

### Specify output directory
**Args:** `ega-cryptor encrypt input.fastq -o /encrypted/output/`
**Explanation:** Specifies custom output directory for encrypted files.

### Generate checksums only
**Args:** `ega-cryptor checksum input.fastq`
**Explanation:** Generates MD5 checksum without encryption.

### Batch encryption
**Args:** `ega-cryptor encrypt -r data/ -o encrypted/ --threads 4`
**Explanation:** Encrypts directory with 4 parallel threads.