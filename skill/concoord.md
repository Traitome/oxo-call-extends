---
name: concoord
category: formatting
description: Generate protein conformations based on geometric restrictions
tags: [concoord, protein-structure, conformation, structural-biology, bioinformatics]
author: oxo-call-community
source_url: "https://www3.mpibpc.mpg.de/groups/de_groot/concoord"
---

## Concepts

- **Tool Overview**: CONCOORD is a method for generating protein conformations around a known structure based on geometric restrictions, useful for exploring conformational space.
- **Core Function**: Generates ensembles of protein conformations by applying geometric constraints to maintain structural integrity while exploring flexibility.
- **Algorithm**: Uses distance geometry and constraint-based modeling to generate physically realistic conformations.
- **Input**: Protein structure in PDB format.
- **Output**: Ensemble of conformations in PDB format.
- **Application**: Protein flexibility analysis, molecular dynamics initialization, and structure refinement.
- **Installation**: Install via bioconda: `conda install -c bioconda concoord`

## Pitfalls

- **Starting Structure**: Quality depends on accuracy of input structure.
- **Conformational Space**: May not sample all relevant conformations.
- **Geometric Constraints**: Overly restrictive constraints limit sampling.
- **Computational Cost**: Generating large ensembles requires significant time.
- **Validation**: Generated conformations should be validated against experimental data.

## Examples

### Generate conformations
**Args:** `concoord -i structure.pdb -o conformations.pdb -n 100`
**Explanation:** Generates 100 conformations around input structure.

### With custom constraints
**Args:** `concoord -i structure.pdb -c constraints.txt -o conformations.pdb`
**Explanation:** Uses custom geometric constraints for conformation generation.

### Limit conformational change
**Args:** `concoord -i structure.pdb -m 2.0 -o conformations.pdb`
**Explanation:** Limits maximum atomic displacement to 2.0 Angstroms.

### Display help
**Args:** `concoord --help`
**Explanation:** Shows all available options and usage information.