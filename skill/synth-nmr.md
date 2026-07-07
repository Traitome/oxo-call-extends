---
name: synth-nmr
category: structural-biology
description: NMR spectroscopy calculations for protein structures.
tags: [synth-nmr, nmr, protein-structure, biophysics]
author: oxo-call-community
source_url: "https://github.com/elkins/synth-nmr"
---

## Concepts

- **Tool Overview**: synth-nmr (v0.10.0) performs NMR spectroscopy calculations for proteins.
- **Core Function**: Calculates NMR parameters from protein structures.
- **Algorithm**: Uses quantum mechanics for NMR property prediction.
- **Input/Output**: Input: PDB structure; Output: NMR parameters.
- **Applications**: Protein structure validation, NMR data interpretation.
- **Installation**: `conda install -c bioconda synth-nmr` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large structures require significant memory.
- **Computational Time**: Calculations can be computationally intensive.
- **Parameter Tuning**: Incorrect parameters affect accuracy.
- **Structure Quality**: Requires high-quality PDB structures.
- **Force Field**: Depends on appropriate force field selection.
- **Solvent Effects**: May require explicit solvent modeling.

## Examples

### Display help
**Args:** `synth-nmr --help`
**Explanation:** Shows available options and usage information.

### Basic NMR calculation
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt`
**Explanation:** Calculate NMR parameters from protein structure.

### With force field
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt -f amber14`
**Explanation:** Use specific force field for calculations.

### Verbose mode
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt --stats`
**Explanation:** Generate statistics about calculations.

### Batch processing
**Args:** `for f in structures/*.pdb; do synth-nmr -i $f -o results/${f%.pdb}.txt; done`
**Explanation:** Process multiple structures.

### Include solvent
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt --solvent`
**Explanation:** Include solvent effects in calculations.

### Include dynamics
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt --dynamics`
**Explanation:** Include dynamic effects.

### Generate report
**Args:** `synth-nmr -i protein.pdb -o nmr_parameters.txt --report`
**Explanation:** Generate comprehensive NMR report.
