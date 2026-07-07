---
name: openbabel
category: utility
description: Open Babel is a chemical toolbox for converting and analyzing chemical data formats.
tags: [openbabel, utility, chemistry, molecular-modeling]
author: oxo-call-community
source_url: "http://www.openbabel.org/"
---

## Concepts

- **Tool Overview**: Open Babel converts between chemical file formats.
- **Core Function**: Handles molecular structure data conversion.
- **Algorithm**: Uses chemistry libraries for format parsing.
- **Input Format**: Accepts various chemical formats (SMILES, PDB, Mol2, etc.).
- **Output**: Produces converted molecular structures.
- **Use Case**: Cheminformatics, drug discovery, and molecular modeling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Format Support**: Not all formats may be fully supported.
- **Memory Usage**: Large molecular datasets require memory.
- **Accuracy**: Conversion may lose information.
- **Dependency**: Requires chemistry libraries.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `obabel --help`
**Explanation:** Shows available options and usage instructions.

### Convert format
**Args:** `obabel input.sdf -O output.pdb`
**Explanation:** Converts SDF to PDB format.

### SMILES to 3D
**Args:** `obabel -:"CCO" -O ethanol.pdb --gen3d`
**Explanation:** Generates 3D structure from SMILES.

### Add hydrogens
**Args:** `obabel input.pdb -O output.pdb -h`
**Explanation:** Adds hydrogen atoms to structure.

### Filter molecules
**Args:** `obabel input.sdf -O filtered.sdf -s "MW < 500"`
**Explanation:** Filters molecules by molecular weight.

### Generate SMILES
**Args:** `obabel input.pdb -O output.smi`
**Explanation:** Generates SMILES string from structure.

### Batch conversion
**Args:** `obabel *.sdf -O converted/ --separate`
**Explanation:** Converts multiple files.