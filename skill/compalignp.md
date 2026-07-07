---
name: compalignp
category: alignment
description: Compute fractional identity between trusted and test alignments
tags: [compalignp, alignment-comparison, benchmarking, bioinformatics, validation]
author: oxo-call-community
source_url: "http://www.biophys.uni-duesseldorf.de/bralibase/"
---

## Concepts

- **Tool Overview**: compalignp is a tool for computing fractional "identity" scores between a trusted (reference) alignment and a test alignment, useful for benchmarking alignment algorithms.
- **Core Function**: Compares two multiple sequence alignments to assess the quality and accuracy of the test alignment against a trusted reference.
- **Algorithm**: Calculates identity metrics by comparing aligned positions between reference and test alignments.
- **Input**: Two multiple sequence alignments in standard formats (FASTA, CLUSTAL, etc.).
- **Output**: Fractional identity scores and alignment quality metrics.
- **Application**: Alignment algorithm benchmarking, method validation, and quality assessment.
- **Installation**: Install via bioconda: `conda install -c bioconda compalignp`

## Pitfalls

- **Reference Quality**: Results depend on accuracy of trusted alignment.
- **Sequence Identity**: Must use same sequences in both alignments.
- **Alignment Format**: Requires compatible alignment formats.
- **Gap Treatment**: Gap handling may affect identity calculations.
- **Interpretation**: Identity scores are relative to reference quality.

## Examples

### Compare alignments
**Args:** `compalignp -t test.aln -r reference.aln -o results.txt`
**Explanation:** Computes identity between test and reference alignments.

### With detailed output
**Args:** `compalignp -t test.aln -r reference.aln -v -o results.txt`
**Explanation:** Generates verbose output with detailed metrics.

### Batch comparison
**Args:** `compalignp -t *.aln -r reference.aln -o batch_results.txt`
**Explanation:** Compares multiple test alignments against reference.

### Display help
**Args:** `compalignp --help`
**Explanation:** Shows all available options and usage information.