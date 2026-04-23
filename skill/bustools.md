---
name: bustools
category: expression
description: Program for manipulating BUS files for single cell RNA-Seq datasets
tags: [bustools, single-cell, rna-seq, bus, kallisto]
author: oxo-call-community
source_url: "https://github.com/BUStools/bustools"
---

## Concepts

- **Tool Overview**: Bustools manipulates BUS files produced by kallisto|bustools for single-cell RNA-seq.
- **Core Function**: Sorts, corrects, and counts BUS format barcoded UMI sequences.
- **BUS Format**: Binary format for efficient storage of barcoded UMI sequences.
- **Workflow**: Correct barcodes → sort → count → generate gene-count matrix.
- **Input**: BUS files from kallisto bus mode.
- **Installation**: Install via bioconda: `conda install -c bioconda bustools`

## Pitfalls

- **BUS Format**: Requires BUS format input from kallisto bus mode.
- **Whitelist**: Barcode correction requires valid barcode whitelist.
- **Memory Usage**: Large datasets require significant memory for sorting.
- **T2G File**: Must provide transcript-to-gene mapping for counting.

## Examples

### Sort BUS file
**Args:** `bustools sort -T tmp/ -t 8 -o sorted.bus output.bus`
**Explanation:** Sorts BUS file by barcode, UMI, and equivalence class.

### Correct barcodes
**Args:** `bustools correct -w whitelist.txt -o corrected.bus sorted.bus`
**Explanation:** Corrects barcodes using provided whitelist.

### Count UMIs to gene matrix
**Args:** `bustools count -o genes -g t2g.txt -e matrix.ec -t 8 --genecounts corrected.bus`
**Explanation:** Generates gene-count matrix from corrected BUS file.

### Capture output from kallisto
**Args:** `kallisto bus -i index.idx -o output/ -x 10xv3 reads.fq && bustools sort -o sorted.bus output/output.bus`
**Explanation:** Runs kallisto in bus mode and sorts the output.

### Inspect BUS file
**Args:** `bustools inspect output.bus`
**Explanation:** Displays summary statistics of BUS file contents.

### Merge multiple BUS files
**Args:** `bustools merge -o merged.bus file1.bus file2.bus`
**Explanation:** Merges multiple BUS files into one.
