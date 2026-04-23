---
name: carna
category: alignment
description: Constraint-based alignment of RNA ensembles considering secondary structure
tags: [carna, rna, alignment, secondary-structure]
author: oxo-call-community
source_url: "https://www.bioinf.uni-leipzig.de/~will/Software/CARNA/"
---

## Concepts

- **Tool Overview**: CARNA aligns RNA sequences considering secondary structure constraints.
- **Core Function**: Aligns RNA molecules using both sequence and structure information.
- **Algorithm**: Constraint-based alignment incorporating base pairing constraints.
- **Input**: RNA sequences in FASTA format with optional structure annotation.
- **Output**: Structure-aware multiple RNA alignment.
- **Application**: Non-coding RNA analysis and structural alignment.
- **Installation**: Install via bioconda: `conda install -c bioconda carna`

## Pitfalls

- **Structure Input**: Providing structure constraints improves alignment quality.
- **Sequence Length**: Very long RNAs may be slow to align.
- **Memory Usage**: Large RNA ensembles require significant memory.

## Examples

### Align RNA sequences
**Args:** `carna -i sequences.fa -o alignment.sto`
**Explanation:** Aligns RNA sequences with structure-aware algorithm.

### With structure constraints
**Args:** `carna -i sequences.fa -s structures.stk -o alignment.sto`
**Explanation:** Uses structure constraints for improved RNA alignment.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
