---
name: ega2
category: utility
description: "EGA download client v2"
tags: [ega2, utility]
author: oxo-call-community
source_url: "https://ega-archive.org/download/downloader-quickguide-v2"
---

## Concepts
- **Tool Overview**: The most up-to-date download client for EGA can be found in the pyega3 package. However, that tool does not download a fairly large chunk of EGA files (those ending in .gpg rather than .cip), which limits its generic usefulness. This package attempts to provide the v2 Java client in a more useful manner than a simple .jar.
- **Core Function**: EGA download client v2
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda ega2`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
