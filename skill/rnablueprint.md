---
name: rnablueprint
category: formatting
description: RNAblueprint uniformly samples RNA/DNA sequences compatible with multiple structural and sequence constraints.
tags: [rnablueprint, formatting, rna-design, sequence-constraint, inverse-folding]
author: oxo-call-community
source_url: "https://viennarna.github.io/RNAblueprint"
---

## Concepts

- **Tool Overview**: RNAblueprint solves RNA sequence design with structural constraints.
- **Core Function**: Samples RNA/DNA sequences compatible with multiple constraints.
- **Algorithm**: Uses constraint-based inverse folding with ViennaRNA energy model.
- **Input Format**: Accepts constraint files (dot-bracket, IUPAC, sequence patterns).
- **Output**: Produces designed RNA/DNA sequences satisfying all constraints.
- **Use Case**: RNA sequence design, synthetic biology, riboswitch engineering.

## Pitfalls

- **Library vs CLI**: RNAblueprint is a C++ library; access via `libRNAblueprint` API or Python bindings.
- **Constraint Conflicts**: Over-constrained designs may have no valid solutions; check feasibility first.
- **Energy Model**: Default uses ViennaRNA; requires ViennaRNA to be installed.
- **Sequence Type**: Supports both RNA and DNA; specify alphabet explicitly in constraints.
- **Uniform Sampling**: Default samples uniformly from feasible space; biased sampling available via API.
- **Build Dependencies**: Requires C++ compiler, CMake, and ViennaRNA development headers.

## Examples

### Display help
**Args:** `RNAblueprint --help`
**Explanation:** Shows CLI options for sequence sampling and constraint specification.

### Sample from constraint file
**Args:** `RNAblueprint -c constraints.txt -n 10 -o designed.fasta`
**Explanation:** `-c` specifies constraint file; `-n 10` generates 10 sequences; `-o` writes FASTA output.

### With dot-bracket structure
**Args:** `RNAblueprint -s "(((...)))" -n 5 -o designed.fasta`
**Explanation:** `-s` provides a dot-bracket secondary structure constraint directly on command line.

### With sequence pattern
**Args:** `RNAblueprint -s "(((...)))" -p "NNNAUGNNN" -o designed.fasta`
**Explanation:** `-p` adds an IUPAC sequence pattern constraint (e.g., AUG start codon).

### With fixed positions
**Args:** `RNAblueprint -s "(((...)))" -f "ACGU_____" -o designed.fasta`
**Explanation:** `-f` specifies fixed bases at certain positions; underscores allow any nucleotide.

### Verbose mode
**Args:** `RNAblueprint -c constraints.txt -n 10 -v -o designed.fasta`
**Explanation:** `-v` enables verbose output showing sampling statistics and constraint satisfaction.

### Python API
**Args:** `python -c "import RNAblueprint; bp = RNAblueprint.Blueprint(); print(bp.sample('(((...)))', n=5))"`
**Explanation:** Imports the `RNAblueprint` Python binding to programmatically sample sequences from a Python script.