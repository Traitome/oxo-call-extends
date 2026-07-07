---
name: tmscoring
category: analysis
description: TM-scoring - Tool for calculating Template Modeling score for protein structure comparison.
tags: [tmscoring, tm-score, protein-structure, structure-comparison, similarity]
author: oxo-call-community
source_url: "https://github.com/compbio/tmscoring"
---

## Concepts

- **Tool Overview**: TM-scoring - A tool for calculating the Template Modeling (TM) score to measure protein structure similarity.
- **Core Function**: Computes TM-score, RMSD, and other structural similarity metrics between protein structures.
- **Input**: Protein structure files (PDB), alignment information.
- **Output**: TM-score, RMSD, alignment quality metrics.
- **Installation**: `pip install tmscoring` or `conda install -c bioconda tmscoring`
- **Use Case**: Protein structure comparison, fold recognition, structural genomics.

## Pitfalls

- **Structure Quality**: Results depend on structure resolution and completeness.
- **Alignment**: Requires proper structural alignment for accurate scoring.

## Examples

### Calculate TM-score
**Args:** `tmscoring -p1 structure1.pdb -p2 structure2.pdb -o tm_score.txt`
**Explanation:** Calculate TM-score between two protein structures.

### Batch comparison
**Args:** `tmscoring -i structures.list -o comparison_results/`
**Explanation:** Compare multiple protein structures against reference.
