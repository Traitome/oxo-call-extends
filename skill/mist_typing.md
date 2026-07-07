---
name: mist_typing
category: variant-calling
description: MiST is a rapid, accurate and flexible (core-genome) multi-locus sequence typing (MLST) allele caller.
tags: [mist_typing, variant-calling]
author: oxo-call-community
source_url: "https://github.com/BioinformaticsPlatformWIV-ISP/MiST"
---

## Concepts

- **Tool Overview**: MiST v1.2.0 performs multi-locus sequence typing (MLST).
- **Core Function**: Calls MLST alleles from genome sequences.
- **MLST Analysis**: Identifies sequence types based on housekeeping genes.
- **Core-Genome MLST**: Supports core-genome MLST analysis.
- **Input/Output**: Accepts genome sequences; outputs MLST types.
- **Allele Calling**: Identifies alleles at specific loci.

## Pitfalls

- **Bacterial Specific**: Designed for bacterial MLST analysis.
- **Computational Resources**: Processing large genomes may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on input sequence quality.
- **Scheme Dependence**: Requires appropriate MLST scheme definitions.

## Examples

### Call MLST alleles
**Args:** `mist_typing -i genome.fasta -o results.txt`
**Explanation:** Calls MLST alleles from genome.

### With custom scheme
**Args:** `mist_typing -i genome.fasta -s scheme.def -o results.txt`
**Explanation:** Uses custom MLST scheme.

### Core-genome MLST
**Args:** `mist_typing -i genome.fasta -c -o results.txt`
**Explanation:** Performs core-genome MLST analysis.

### Batch processing
**Args:** `mist_typing -i fasta/ -o results/`
**Explanation:** Processes multiple genome files.

### Generate report
**Args:** `mist_typing -i genome.fasta -o results.txt -r report.html`
**Explanation:** Generates HTML analysis report.