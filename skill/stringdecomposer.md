---
name: stringdecomposer
category: utility
description: A tool for decomposing strings into a set of given monomers.
tags: [stringdecomposer, string-analysis, bioinformatics, utility]
author: oxo-call-community
source_url: "https://github.com/ablab/stringdecomposer"
---

## Concepts

- **Tool Overview**: stringdecomposer (v1.1.2) is a tool for decomposing biological sequences into a set of given monomers or building blocks.
- **Core Function**: Breaks down sequences into constituent monomers for analysis.
- **Algorithm**: Uses pattern matching to decompose sequences into predefined monomers.
- **Input/Output**: Input: Sequence file (FASTA/FASTQ); Output: Decomposition results with monomer counts.
- **Applications**: Sequence analysis, motif discovery, compositional analysis.
- **Installation**: `conda install -c bioconda stringdecomposer` or download from GitHub.

## Pitfalls

- **Monomer Set**: Requires predefined monomer set for decomposition.
- **Sequence Quality**: Low-quality sequences affect decomposition accuracy.
- **Ambiguity**: Ambiguous monomers may produce multiple decompositions.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Decomposition of large sequences can be slow.
- **Format Requirements**: Requires specific input format.

## Examples

### Display help
**Args:** `stringdecomposer --help`
**Explanation:** Shows available options and usage information.

### Basic decomposition
**Args:** `stringdecomposer -i sequence.fasta -m monomers.txt -o results.txt`
**Explanation:** Decompose sequence using predefined monomers.

### With custom monomers
**Args:** `stringdecomposer -i sequence.fasta -m custom_monomers.txt -o results.txt`
**Explanation:** Use custom monomer set for decomposition.

### Verbose mode
**Args:** `stringdecomposer -i sequence.fasta -m monomers.txt -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `stringdecomposer -i sequence.fasta -m monomers.txt -o results.txt --stats`
**Explanation:** Generate statistics about monomer composition.

### Batch processing
**Args:** `stringdecomposer -i sequences/ -m monomers.txt -o results/`
**Explanation:** Process multiple sequence files together.

### Filter by length
**Args:** `stringdecomposer -i sequence.fasta -m monomers.txt -o results.txt -l 100`
**Explanation:** Minimum sequence length of 100.

### Include ambiguous
**Args:** `stringdecomposer -i sequence.fasta -m monomers.txt -o results.txt --ambiguous`
**Explanation:** Include ambiguous decompositions.

### Generate report
**Args:** `stringdecomposer -i sequence.fasta -m monomers.txt -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
