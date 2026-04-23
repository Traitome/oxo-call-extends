---
name: ega-cryptor
category: population-genomics
description: "EGA Cryptor v2.0.0 is a tool designed to encrypt files compliant with the European Genome-phenome Archive (EGA)"
tags: [ega-cryptor, population-genomics]
author: oxo-call-community
source_url: "https://ega-archive.org/submission/data/file-preparation/egacryptor/"
---

## Concepts
- **Tool Overview**: The EGACryptor v.2.0.0 is a JAVA-based application which enables submitters to produce EGA compliant encrypted files along with files for the encrypted and unencrypted md5sum for each file to be submitted. The application will generate an output folder that will by default mirror the directory structure containing the original files. This output folder can subsequently be uploaded to the EGA FTP staging area via an FTP or Aspera client.
- **Core Function**: EGA Cryptor v2.0.0 is a tool designed to encrypt files compliant with the European Genome-phenome Archive (EGA)
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda ega-cryptor`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
