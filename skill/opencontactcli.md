---
name: opencontactcli
category: alignment
description: OpenContactCLI identifies potential peptide biomimetics from protein interaction structures.
tags: [opencontactcli, alignment, protein-interaction, drug-design]
author: oxo-call-community
source_url: "https://github.com/galaxyproteomics/OpenContact"
---

## Concepts

- **Tool Overview**: OpenContactCLI analyzes protein-protein interactions.
- **Core Function**: Identifies contact points for peptide mimetic design.
- **Algorithm**: Uses geometric and chemical analysis of protein interfaces.
- **Input Format**: Accepts PDB structure files.
- **Output**: Produces contact maps and potential peptide candidates.
- **Use Case**: Drug discovery, peptide design, and protein engineering.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Structure Quality**: Results depend on PDB structure quality.
- **Memory Usage**: Large structures require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **False Positives**: May predict false interaction sites.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `opencontactcli --help`
**Explanation:** Shows available options and usage instructions.

### Analyze interaction
**Args:** `opencontactcli -i complex.pdb -o contacts.txt`
**Explanation:** Analyzes protein-protein interactions.

### With chain selection
**Args:** `opencontactcli -i complex.pdb -A A -B B -o contacts.txt`
**Explanation:** Specifies chains for analysis.

### Output format
**Args:** `opencontactcli -i complex.pdb -o contacts.json --json`
**Explanation:** Outputs in JSON format.

### Verbose mode
**Args:** `opencontactcli -i complex.pdb -v -o contacts.txt`
**Explanation:** Runs with verbose output.

### Distance cutoff
**Args:** `opencontactcli -i complex.pdb -d 5.0 -o contacts.txt`
**Explanation:** Sets distance cutoff to 5.0 Angstroms.

### Batch processing
**Args:** `opencontactcli batch -d pdbs/ -o results/`
**Explanation:** Processes multiple PDB files.