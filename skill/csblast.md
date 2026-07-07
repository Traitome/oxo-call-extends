---
name: csblast
category: alignment
description: Context-specific extension of BLAST that significantly improves sensitivity and alignment quality.
tags: [csblast, alignment, protein-sequence, homology-search]
author: oxo-call-community
source_url: "http://wwwuser.gwdg.de/~compbiol/data/csblast/"
---

## Concepts

- **Tool Overview**: csblast (v2.2.3+) is a context-specific extension of the BLAST algorithm that improves alignment sensitivity and quality by incorporating context information from multiple sequence alignments.
- **Core Function**: Performs protein sequence similarity searches with enhanced accuracy through context-specific scoring matrices derived from multiple sequence alignments.
- **Input/Output**: Input: FASTA query sequences, FASTA database. Output: Alignment results in BLAST format, including E-values and bit scores.
- **Algorithm**: Extends BLAST by using position-specific scoring matrices (PSSMs) and context-aware substitution scores to improve detection of remote homologs.
- **Key Features**: Improved sensitivity for distant homologs, context-specific scoring, supports PSI-BLAST-like iterations.
- **Installation**: `conda install -c bioconda csblast`

## Pitfalls

- **Memory Usage**: May require significant memory for large databases or complex queries.
- **Computational Time**: Context-specific scoring can be computationally intensive.
- **Database Format**: Requires formatted databases similar to BLAST.
- **Parameter Tuning**: Optimal performance may require parameter adjustment.
- **Version Compatibility**: Output formats may differ from standard BLAST.

## Examples

### Basic sequence search
**Args:** `csblast -i query.fasta -d database.fasta -o results.txt`
**Explanation:** Search query sequence against a database using context-specific scoring.

### Search with iterations
**Args:** `csblast -i query.fasta -d database.fasta -o results.txt -num_iterations 3`
**Explanation:** Perform 3 iterations of context-specific search to improve sensitivity.

### Display help
**Args:** `csblast --help`
**Explanation:** Shows available options and parameters.