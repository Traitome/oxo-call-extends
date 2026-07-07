---
name: starcatpy
category: rna-seq
description: Implements *CellAnnotator (aka *CAT/starCAT), annotating scRNA-Seq with predefined gene expression programs.
tags: [starcatpy, single-cell, rna-seq, cell-annotation]
author: oxo-call-community
source_url: "https://github.com/immunogenomics/starCAT"
---

## Concepts

- **Tool Overview**: starcatpy (v1.0.10) is a tool for annotating single-cell RNA sequencing data using predefined gene expression signatures.
- **Core Function**: Automatically assigns cell types based on similarity to reference gene expression programs.
- **Algorithm**: Uses weighted gene expression similarity scoring to match cells to known cell type signatures.
- **Input/Output**: Input: scRNA-Seq count matrix; Output: Cell type annotations with confidence scores.
- **Reference Signatures**: Supports custom gene expression signatures and built-in reference datasets.
- **Installation**: `conda install -c bioconda starcatpy` or `pip install starcatpy`.

## Pitfalls

- **Reference Quality**: Poor quality reference signatures lead to incorrect cell type assignments.
- **Batch Effects**: Batch effects between reference and query data affect annotation accuracy.
- **Marker Specificity**: Non-specific marker genes may produce ambiguous annotations.
- **Confidence Threshold**: Incorrect threshold settings affect sensitivity/specificity.
- **Normalization**: Improper data normalization affects similarity scoring.
- **Memory Requirements**: Large datasets may require significant memory.

## Examples

### Display help
**Args:** `starcatpy --help`
**Explanation:** Shows available options and usage information.

### Basic cell annotation
**Args:** `starcatpy -i counts.h5ad -o annotations.txt`
**Explanation:** Annotate cells in AnnData object using default signatures.

### With custom signatures
**Args:** `starcatpy -i counts.h5ad -s signatures.gmt -o annotations.txt`
**Explanation:** Use custom gene signatures for cell annotation.

### Confidence filtering
**Args:** `starcatpy -i counts.h5ad -o annotations.txt -c 0.7`
**Explanation:** Filter annotations with confidence below 0.7.

### Output probabilities
**Args:** `starcatpy -i counts.h5ad -o probabilities.txt --probabilities`
**Explanation:** Output probability scores for all cell types.

### Batch correction
**Args:** `starcatpy -i counts.h5ad -o annotations.txt --batch-correct`
**Explanation:** Apply batch effect correction before annotation.

### Verbose mode
**Args:** `starcatpy -i counts.h5ad -o annotations.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Save plot
**Args:** `starcatpy -i counts.h5ad -o annotations.txt --plot umap.png`
**Explanation:** Generate visualization of annotated cells.

### Multiple datasets
**Args:** `starcatpy -i sample1.h5ad sample2.h5ad -o annotations/`
**Explanation:** Process multiple datasets together.
