---
name: pal_finder
category: utility
description: Find microsatellite repeat elements from sequencing reads and design PCR primers to amplify them
tags: [pal_finder, utility]
author: oxo-call-community
source_url: "http://sourceforge.net/projects/palfinder/"
---

## Concepts
- **Tool Overview**: Finds microsatellite repeat elements directly from raw 454 or Illumina paired-end sequencing reads, and designs PCR primers to amplify these repeat loci in an automated fashion. Exact matches to repeats or 2-, 3-, 4-, 5-, and/or 6-mers are located and primer3 is then used to generate primer pairs to amplify regions containing microsatellite loci.
- **Core Function**: Processes bioinformatics data for utility tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda pal_finder`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
