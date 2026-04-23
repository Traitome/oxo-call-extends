---
name: blosum
category: utility
description: Easy access to BLOSUM substitution matrices without dependencies
tags: [blosum, substitution-matrix, protein, scoring]
author: oxo-call-community
source_url: "https://github.com/not-a-feature/blosum"
---

## Concepts

- **Tool Overview**: blosum provides easy access to BLOSUM (BLOcks SUbstitution Matrices) for protein alignment scoring.
- **Core Function**: Reads and provides BLOSUM matrices for protein sequence comparison.
- **Matrices**: Includes BLOSUM45, BLOSUM50, BLOSUM62, BLOSUM80, BLOSUM90, and others.
- **No Dependencies**: Lightweight Python module with no third-party dependencies.
- **Application**: Protein alignment scoring and sequence comparison.
- **Installation**: Install via bioconda: `conda install -c bioconda blosum`

## Pitfalls

- **Matrix Selection**: Choose appropriate BLOSUM matrix based on sequence divergence.
- **Scoring Convention**: Positive scores indicate conservative substitutions.
- **Gap Penalties**: BLOSUM matrices do not include gap penalties.
- **Python Module**: Primarily a Python library, not a command-line tool.

## Examples

### Import BLOSUM62 in Python
**Args:** `from blosum import BLOSUM62; print(BLOSUM62[('A','A')])`
**Explanation:** Imports BLOSUM62 matrix and prints score for alanine-alanine match.

### Use BLOSUM80 for close homologs
**Args:** `from blosum import BLOSUM80; score = BLOSUM80[('W','W')]`
**Explanation:** Uses BLOSUM80 matrix suitable for closely related sequences.

### Use BLOSUM45 for distant homologs
**Args:** `from blosum import BLOSUM45; score = BLOSUM45[('D','E')]`
**Explanation:** Uses BLOSUM45 matrix suitable for distantly related sequences.

### List available matrices
**Args:** `import blosum; print(dir(blosum))`
**Explanation:** Lists all available BLOSUM matrices in the module.
