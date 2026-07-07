---
name: reduce
category: population-genomics
description: Reduce is a tool for adding and correcting hydrogens in PDB files for structural biology.
tags: [reduce, population-genomics, pdb, hydrogen-addition]
author: oxo-call-community
source_url: "https://github.com/rlabduke/reduce/blob/v4.15/README.md"
---

## Concepts

- **Tool Overview**: reduce adds hydrogens.
- **Core Function**: Hydrogen addition.
- **Algorithm**: Uses structural methods.
- **Input Format**: Accepts PDB files.
- **Output**: Produces corrected PDB files.
- **Use Case**: Structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Structure Quality**: Affects correction.
- **Parameters**: Must be configured.
- **Runtime**: Correction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reduce --help`
**Explanation:** Shows available options and usage instructions.

### Add hydrogens
**Args:** `reduce add -i structure.pdb -o corrected_structure.pdb`
**Explanation:** Adds hydrogens to structure.

### With parameters
**Args:** `reduce add -i structure.pdb -p params.yaml -o corrected_structure.pdb`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reduce -v add -i structure.pdb -o corrected_structure.pdb`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reduce -t 4 add -i structure.pdb -o corrected_structure.pdb`
**Explanation:** Uses 4 threads for parallel processing.

### With pH value
**Args:** `reduce add -i structure.pdb -p 7.4 -o corrected_structure.pdb`
**Explanation:** Uses pH value for protonation.

### Generate report
**Args:** `reduce add -i structure.pdb -o corrected_structure.pdb --report report.html`
**Explanation:** Generates HTML report.