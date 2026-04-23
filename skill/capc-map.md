---
name: capc-map
category: epigenomics
description: Analysis software for Capture-C chromatin conformation data
tags: [capc-map, capture-c, chromatin, 3c, conformation]
author: oxo-call-community
source_url: "https://github.com/cbrackley/capC-MAP"
---

## Concepts

- **Tool Overview**: capC-MAP analyzes Capture-C data to map chromatin interactions.
- **Core Function**: Identifies significant chromatin interactions from Capture-C data.
- **Input**: FASTQ files from Capture-C experiments.
- **Output**: Interaction matrices and significant interaction calls.
- **Application**: Chromatin conformation and enhancer-promoter mapping.
- **Installation**: Install via bioconda: `conda install -c bioconda capc-map`

## Pitfalls

- **Restriction Enzyme**: Must specify restriction enzyme used in protocol.
- **Reference Genome**: Requires matching reference genome.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Analyze Capture-C data
**Args:** `capC-MAP -1 R1.fq -2 R2.fq -r reference.fa -e DpnII -o results/`
**Explanation:** Processes Capture-C data with DpnII restriction enzyme.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
