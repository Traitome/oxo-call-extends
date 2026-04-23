---
name: biobb_structure_checking
category: utility
description: BioBB structure checking for MD simulation setup
tags: [bioexcel, structure-checking, md-setup, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_structure_checking"
---

## Concepts
- **Tool Overview**: biobb_structure_checking performs quality checking of 3D structures to facilitate MD simulation setup. It detects and fixes structure errors.
- **Checking Features**: Model/chain selection, alternative location handling, missing side chains, backbone breaks, amide assignments, incorrect chirality.
- **Fixing Capabilities**: Adds disulfide bonds, hydrogen atoms, reconstructs missing atoms, fixes structural issues.
- **Applications**: MD simulation preparation, structure validation, PDB file quality assessment.

## Pitfalls
- **Structure Source**: Works with PDB and user-provided structures; quality varies by source.
- **Manual Review**: Automated fixes should be reviewed for biological correctness.

## Examples
### Check structure
**Args:** `biobb_structure_checking check --input structure.pdb --output report.json`
**Explanation:** Checks structure for issues and generates quality report.

### Fix structure issues
**Args:** `biobb_structure_checking fix --input structure.pdb --output fixed.pdb --fix-missing-sidechains --fix-amide`
**Explanation:** Fixes missing side chains and amide assignments automatically.
