---
name: chisel
category: single-cell
description: Copy-number Haplotype Inference in Single-cell by Evolutionary Links
tags: [chisel, single-cell, copy-number, haplotype, dna-sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/raphael-group/chisel"
---

## Concepts

- **Tool Overview**: CHISEL infers allele- and haplotype-specific copy numbers in individual cells from low-coverage single-cell DNA sequencing data.
- **Core Function**: Uses evolutionary links between cells to accurately reconstruct copy number profiles at the haplotype level.
- **Algorithm**: Integrates single-cell sequencing data with population allele frequencies to resolve haplotype-specific copy numbers.
- **Input**: Low-coverage single-cell DNA sequencing data and variant calls.
- **Output**: Haplotype-specific copy number profiles for each cell.
- **Application**: Cancer genomics, single-cell sequencing analysis, and copy number variation studies.
- **Installation**: Install via bioconda: `conda install -c bioconda chisel`

## Pitfalls

- **Coverage Requirements**: Designed for low-coverage data but requires sufficient depth for reliable inference.
- **Variant Quality**: Depends on accurate variant calling and phasing information.
- **Computational Time**: May be computationally intensive for large cell populations.
- **Memory Usage**: Requires significant memory for large datasets.
- **Evolutionary Model**: Assumes cells are related through an evolutionary tree.

## Examples

### Run CHISEL analysis
**Args:** `chisel -i bam_files/ -v variants.vcf -o results/`
**Explanation:** Runs copy number inference on single-cell data.

### With phasing information
**Args:** `chisel -i bam_files/ -v variants.vcf -p phasing.txt -o results/`
**Explanation:** Uses pre-computed phasing information for improved accuracy.

### Specify ploidy
**Args:** `chisel -i bam_files/ -v variants.vcf -p 2 -o results/`
**Explanation:** Specifies expected ploidy for copy number inference.

### Display help
**Args:** `chisel --help`
**Explanation:** Shows all available options and usage information.