---
name: inforna
category: rna-analysis
description: RNA sequence design tool for target secondary structures
tags: [inforna, RNA-design, secondary-structure, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/INFO-RNA"
---

## Concepts

- **Tool Overview**: INFO-RNA (v2.1.2) is a tool for designing RNA sequences that fold into a specified secondary structure without pseudoknots.
- **Core Function**: Uses constraint-based optimization to generate RNA sequences with desired folding properties.
- **Input/Output**: Accepts secondary structure constraints in dot-bracket notation. Outputs candidate RNA sequences.
- **Algorithm**: Combines thermodynamic modeling with constraint satisfaction for sequence design.
- **Applications**: RNA aptamer design, ribozyme engineering, and RNA-based therapeutics development.

## Pitfalls

- **Structure Complexity**: Pseudoknots are not supported; must use pseudoknot-free structures.
- **Sequence Length**: Computational complexity increases with sequence length.
- **Thermodynamic Stability**: Designed sequences may require experimental validation.
- **Constraint Conflicts**: Conflicting constraints may result in no valid solution.
- **Energy Parameters**: Results depend on RNA folding energy parameters used.

## Examples

### Design RNA for target structure
**Args:** `inforna -s "((..))" -o designed_rna.fa`
**Explanation:** Designs RNA sequences that fold into a simple hairpin structure.

### Specify GC content
**Args:** `inforna -s "((....))" -g 0.5 -o designed_rna.fa`
**Explanation:** Designs sequences with 50% GC content for the target structure.

### Multiple structure constraints
**Args:** `inforna -s "((..))" "(.())" -o multi_structure.fa`
**Explanation:** Designs sequences compatible with multiple target structures.

### Set minimum free energy threshold
**Args:** `inforna -s "((....))" -e -10.0 -o stable_rna.fa`
**Explanation:** Ensures designed sequences have minimum free energy ≤ -10.0 kcal/mol.

### Output multiple candidates
**Args:** `inforna -s "((..))" -n 10 -o candidates.fa`
**Explanation:** Generates 10 candidate sequences for the target structure.

### Include sequence constraints
**Args:** `inforna -s "((....))" -c "NNGCNNN" -o constrained.fa`
**Explanation:** Designs sequences with specific positional constraints.