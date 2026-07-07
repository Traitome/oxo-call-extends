---
name: qiskit-xyz2pdb
category: formatting
description: Qiskit-xyz2pdb converts XYZ molecular structure files to PDB format.
tags: [qiskit-xyz2pdb, formatting, molecular-structure, conversion]
author: oxo-call-community
source_url: "https://github.com/thepineapplepirate/qiskit-xyz2pdb"
---

## Concepts

- **Tool Overview**: qiskit-xyz2pdb converts file formats.
- **Core Function**: Format conversion.
- **Algorithm**: Uses file parsing.
- **Input Format**: Accepts XYZ files.
- **Output**: Produces PDB files.
- **Use Case**: Structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Input Format**: Must be XYZ.
- **Output Format**: Must be correct.
- **Runtime**: Conversion may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qiskit-xyz2pdb --help`
**Explanation:** Shows available options and usage instructions.

### Convert file
**Args:** `qiskit-xyz2pdb convert -i input.xyz -o output.pdb`
**Explanation:** Converts XYZ to PDB.

### With parameters
**Args:** `qiskit-xyz2pdb convert -i input.xyz -p params.yaml -o output.pdb`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qiskit-xyz2pdb -v convert -i input.xyz -o output.pdb`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qiskit-xyz2pdb -t 4 convert -i input.xyz -o output.pdb`
**Explanation:** Uses 4 threads for parallel processing.

### Batch conversion
**Args:** `qiskit-xyz2pdb batch -i input_dir/ -o output_dir/`
**Explanation:** Converts multiple files.

### Generate report
**Args:** `qiskit-xyz2pdb convert -i input.xyz -o output.pdb --report report.html`
**Explanation:** Generates HTML report.