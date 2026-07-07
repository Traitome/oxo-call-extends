---
name: rdock
category: genome-editing
description: rDock is a fast, versatile and open source program for docking ligands to proteins and nucleic acids.
tags: [rdock, genome-editing, docking, molecular-docking]
author: oxo-call-community
source_url: "https://rdock.github.io/documentation/"
---

## Concepts

- **Tool Overview**: rdock docks ligands.
- **Core Function**: Molecular docking.
- **Algorithm**: Uses docking methods.
- **Input Format**: Accepts molecular files.
- **Output**: Produces docking poses.
- **Use Case**: Drug discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large proteins require memory.
- **Protein Structure**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Docking may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rdock --help`
**Explanation:** Shows available options and usage instructions.

### Dock ligands
**Args:** `rdock dock -i ligand.smi -r protein.pdb -o poses.sdf`
**Explanation:** Docks ligands to protein.

### With parameters
**Args:** `rdock dock -i ligand.smi -p params.yaml -o poses.sdf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rdock -v dock -i ligand.smi -o poses.sdf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rdock -t 4 dock -i ligand.smi -o poses.sdf`
**Explanation:** Uses 4 threads for parallel processing.

### Score poses
**Args:** `rdock score -i poses.sdf -r protein.pdb -o scores.txt`
**Explanation:** Scores docking poses.

### Generate report
**Args:** `rdock dock -i ligand.smi -o poses.sdf --report report.html`
**Explanation:** Generates HTML report.