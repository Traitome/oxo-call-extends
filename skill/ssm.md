---
name: ssm
category: structure-analysis
description: Secondary-structure matching tool for fast protein structure alignment.
tags: [ssm, protein-structure, alignment, bioinformatics]
author: oxo-call-community
source_url: "https://www.ccp4.ac.uk"
---

## Concepts

- **Tool Overview**: ssm (v1.4) is a fast protein structure alignment tool that compares protein structures based on secondary structure elements.
- **Core Function**: Aligns protein structures by matching secondary structure elements (helices, strands) and their spatial arrangements.
- **Algorithm**: Uses graph-based approach to match secondary structure patterns between proteins.
- **Input/Output**: Input: PDB format protein structures; Output: Alignment scores, RMSD values, and superposed structures.
- **Applications**: Protein structure comparison, fold recognition, and evolutionary analysis.
- **Installation**: `conda install -c bioconda ssm` or part of CCP4 suite.

## Pitfalls

- **Structure Quality**: Low-resolution or incomplete structures affect alignment accuracy.
- **Secondary Structure Prediction**: Incorrect secondary structure assignments lead to poor alignments.
- **Flexibility**: Highly flexible regions can cause misalignment.
- **Domain Boundaries**: Multi-domain proteins may require domain splitting before alignment.
- **Sequence Identity**: Very low sequence identity makes structural alignment more challenging.
- **Output Format**: Default output may need conversion for downstream visualization tools.

## Examples

### Display help
**Args:** `ssm -h`
**Explanation:** Shows available options and usage information.

### Basic structure alignment
**Args:** `ssm structure1.pdb structure2.pdb`
**Explanation:** Align two protein structures.

### Multiple structure alignment
**Args:** `ssm -m structure1.pdb structure2.pdb structure3.pdb`
**Explanation:** Align multiple protein structures together.

### Output superposed structure
**Args:** `ssm -o aligned.pdb structure1.pdb structure2.pdb`
**Explanation:** Output superposed structure in PDB format.

### Include sequence alignment
**Args:** `ssm -s structure1.pdb structure2.pdb`
**Explanation:** Generate sequence alignment alongside structural alignment.

### RMSD calculation
**Args:** `ssm -r structure1.pdb structure2.pdb`
**Explanation:** Calculate RMSD between two structures.

### Verbose output
**Args:** `ssm -v structure1.pdb structure2.pdb`
**Explanation:** Run with detailed output including alignment statistics.

### Compare against database
**Args:** `ssm -d pdb_database/ query.pdb`
**Explanation:** Compare query structure against PDB database.
