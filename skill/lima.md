---
name: lima
category: qc
description: lima - The PacBio Barcode Demultiplexer
tags: [lima, qc]
author: oxo-call-community
source_url: "https://lima.how"
---

## Concepts

- **Tool Overview**: lima v2.13.0 - lima - The PacBio Barcode Demultiplexer.
- **Core Function**: lima - The PacBio Barcode Demultiplexer
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda lima`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Demultiplex reads
**Args:** `lima input.bam barcodes.fasta output.bam`
**Explanation:** Demultiplexes PacBio CCS reads by barcode sequences.

