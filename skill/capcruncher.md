---
name: capcruncher
category: epigenomics
description: End-to-end solution for processing Capture-C, Tri-C and Tiled-C data
tags: [capcruncher, capture-c, hi-c, chromatin, 3c]
author: oxo-call-community
source_url: "https://github.com/sims-lab/CapCruncher"
---

## Concepts

- **Tool Overview**: CapCruncher processes Capture-C and related chromatin conformation data.
- **Core Function**: Aligns, filters, and analyzes Capture-C, Tri-C, and Tiled-C data.
- **Input**: FASTQ files from Capture-C experiments.
- **Output**: Interaction matrices and filtered read pairs.
- **Workflow**: Demultiplex → Trim → Align → Filter → Count interactions.
- **Installation**: Install via bioconda: `conda install -c bioconda capcruncher`

## Pitfalls

- **Reference Required**: Requires reference genome index.
- **Restriction Enzyme**: Must specify restriction enzyme used in protocol.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Process Capture-C data
**Args:** `capcruncher pipeline -i reads.fq -r reference.fa -e DpnII -o results/`
**Explanation:** Processes Capture-C data with DpnII restriction enzyme.

### Trim and align
**Args:** `capcruncher trim -i reads.fq -o trimmed.fq && capcruncher align -i trimmed.fq -r reference.fa -o aligned.bam`
**Explanation:** Trims adapters and aligns reads separately.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
