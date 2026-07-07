---
name: rdkit
category: utility
description: RDKit is a collection of cheminformatics and machine-learning software written in C++ and Python.
tags: [rdkit, utility, cheminformatics, machine-learning]
author: oxo-call-community
source_url: "https://www.rdkit.org"
---

## Concepts

- **Tool Overview**: rdkit analyzes molecules.
- **Core Function**: Cheminformatics.
- **Algorithm**: Uses chemical methods.
- **Input Format**: Accepts molecular files.
- **Output**: Produces molecular data.
- **Use Case**: Drug discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large molecules require memory.
- **Molecule Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rdkit --help`
**Explanation:** Shows available options and usage instructions.

### Analyze molecules
**Args:** `rdkit analyze -i molecules.smi -o analysis.txt`
**Explanation:** Analyzes molecular properties.

### With parameters
**Args:** `rdkit analyze -i molecules.smi -p params.yaml -o analysis.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rdkit -v analyze -i molecules.smi -o analysis.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rdkit -t 4 analyze -i molecules.smi -o analysis.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Fingerprint generation
**Args:** `rdkit fingerprint -i molecules.smi -o fingerprints.txt`
**Explanation:** Generates molecular fingerprints.

### Generate report
**Args:** `rdkit analyze -i molecules.smi -o analysis.txt --report report.html`
**Explanation:** Generates HTML report.