---
name: strike
category: alignment
description: A program to evaluate protein multiple sequence alignments using a single protein structure.
tags: [strike, protein-alignment, structure-validation, bioinformatics]
author: oxo-call-community
source_url: "http://www.tcoffee.org/Projects/strike/index.html"
---

## Concepts

- **Tool Overview**: strike (v1.2) is a tool for evaluating protein multiple sequence alignments using structural information from a single protein structure.
- **Core Function**: Validates and scores multiple sequence alignments based on structural constraints.
- **Algorithm**: Uses protein structure information to assess alignment quality and identify problematic regions.
- **Input/Output**: Input: Multiple sequence alignment (FASTA/Clustal), protein structure (PDB); Output: Alignment quality scores.
- **Applications**: Alignment validation, protein structure analysis, evolutionary studies.
- **Installation**: `conda install -c bioconda strike` or download from T-Coffee website.

## Pitfalls

- **Structure Quality**: Poor quality structures affect evaluation accuracy.
- **Alignment Format**: Requires specific alignment format.
- **Sequence Identity**: Low sequence identity alignments are hard to evaluate.
- **Missing Residues**: Missing residues in structure affect mapping.
- **Memory Requirements**: Large alignments require significant memory.
- **Computational Time**: Evaluation of large alignments can be slow.

## Examples

### Display help
**Args:** `strike --help`
**Explanation:** Shows available options and usage information.

### Basic alignment evaluation
**Args:** `strike -i alignment.fasta -s structure.pdb -o results.txt`
**Explanation:** Evaluate alignment using protein structure.

### With multiple structures
**Args:** `strike -i alignment.fasta -s struct1.pdb struct2.pdb -o results.txt`
**Explanation:** Use multiple structures for evaluation.

### Verbose mode
**Args:** `strike -i alignment.fasta -s structure.pdb -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strike -i alignment.fasta -s structure.pdb -o results.txt --plot`
**Explanation:** Generate visualization of alignment quality.

### Custom parameters
**Args:** `strike -i alignment.fasta -s structure.pdb -o results.txt -c 0.9`
**Explanation:** Minimum confidence threshold of 0.9.

### Batch processing
**Args:** `strike -i alignments/ -s structure.pdb -o results/`
**Explanation:** Process multiple alignments together.

### Filter by quality
**Args:** `strike -i alignment.fasta -s structure.pdb -o results.txt -q 20`
**Explanation:** Filter low-quality alignment regions.

### Generate report
**Args:** `strike -i alignment.fasta -s structure.pdb -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
