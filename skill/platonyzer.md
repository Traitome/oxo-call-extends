---
name: platonyzer
category: utility
description: platonyzer creates restraints for metal sites.
tags: [platonyzer, utility, metal-sites, restraints]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/platonyzer"
---

## Concepts

- **Tool Overview**: platonyzer creates metal site restraints.
- **Core Function**: Metal site restraint generation.
- **Algorithm**: Uses structural analysis methods.
- **Input Format**: Accepts PDB structure files.
- **Output**: Produces restraint definitions.
- **Use Case**: Protein structure refinement, crystallography.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Data Quality**: Results depend on structure quality.
- **Restraint Accuracy**: May have restraint errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `platonyzer --help`
**Explanation:** Shows available options and usage instructions.

### Process structure
**Args:** `platonyzer -i structure.pdb -o restraints.txt`
**Explanation:** Creates restraints for metal sites.

### With parameters
**Args:** `platonyzer -i structure.pdb -p params.yaml -o restraints.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `platonyzer -v -i structure.pdb -o restraints.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `platonyzer -t 4 -i structure.pdb -o restraints.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `platonyzer -i structure.pdb -o restraints.cif --cif`
**Explanation:** Outputs in CIF format.

### Generate report
**Args:** `platonyzer -i structure.pdb -o restraints.txt --report report.html`
**Explanation:** Generates HTML report.