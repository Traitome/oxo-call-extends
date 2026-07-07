---
name: tedna
category: assembly
description: TEDNA - Targeted EDNA assembly tool for assembling specific target regions from sequencing data.
tags: [tedna, targeted-assembly, edna, target-region, assembly]
author: oxo-call-community
source_url: "https://github.com/readsii/TEDNA"
---

## Concepts

- **Tool Overview**: TEDNA (Targeted EDNA) - A tool for assembling specific target regions from environmental DNA or targeted sequencing data.
- **Core Function**: Performs targeted assembly of specific genomic regions from complex metagenomic or sequencing datasets.
- **Input**: Mixed sequencing reads (FASTQ) and target region definitions.
- **Output**: Assembled contigs for target regions.
- **Installation**: `pip install tedna` or `conda install -c bioconda tedna`
- **Use Case**: Assembling specific genes or regions from complex environmental samples.

## Pitfalls

- **Target Definition**: Requires accurate target region definitions for effective assembly.
- **Mixed Samples**: Complex mixtures may require additional preprocessing.

## Examples

### Assemble target regions
**Args:** `tedna -i reads.fastq -t targets.fasta -o assembly/`
**Explanation:** Assemble target regions from input reads.
