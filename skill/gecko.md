---
name: gecko
category: comparative-genomics
description: Pairwise genome comparison software for detecting High-scoring Segment Pairs (HSPs).
tags: [gecko, genome-comparison, HSP, synteny, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/otorreno/gecko"
---

## Concepts
- **Genome Comparison**: Performs pairwise comparison of genome sequences.
- **High-scoring Segment Pairs**: Identifies HSPs representing conserved genomic regions.
- **Synteny Detection**: Detects syntenic regions between genomes.
- **Alignment Scoring**: Uses scoring matrices for sequence comparison.
- **Segment Identification**: Identifies homologous segments between genomes.

## Pitfalls
- **Genome Size**: Performance may degrade with very large genomes.
- **Sequence Divergence**: May miss highly diverged regions.
- **Memory Usage**: Requires significant memory for large genome comparisons.
- **Parameter Sensitivity**: HSP detection depends on scoring parameters.
- **Output Size**: Large comparisons can generate massive output files.

## Examples
### Compare two genomes
**Args:** `gecko compare -a genome1.fasta -b genome2.fasta -o comparison.txt`
**Explanation:** Compares two genomes and outputs HSPs.

### With custom scoring matrix
**Args:** `gecko compare -a genome1.fasta -b genome2.fasta -m scoring_matrix.txt -o comparison.txt`
**Explanation:** Uses custom scoring matrix for HSP detection.

### Filter by segment length
**Args:** `gecko compare -a genome1.fasta -b genome2.fasta -l 1000 -o comparison.txt`
**Explanation:** Filters HSPs to include only segments longer than 1000bp.

### Generate dot plot
**Args:** `gecko dotplot -a genome1.fasta -b genome2.fasta -o dotplot.png`
**Explanation:** Generates a dot plot visualization of genome alignment.

### Find syntenic blocks
**Args:** `gecko synteny -a genome1.fasta -b genome2.fasta -o synteny.txt`
**Explanation:** Identifies syntenic blocks between two genomes.