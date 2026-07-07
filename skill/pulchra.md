---
name: pulchra
category: utility
description: pulchra reconstructs and refines all-atom protein models from reduced representations.
tags: [pulchra, utility, protein-structure, all-atom-modeling]
author: oxo-call-community
source_url: "https://www.pirx.com/pulchra/"
---

## Concepts

- **Tool Overview**: pulchra builds protein structures.
- **Core Function**: All-atom reconstruction.
- **Algorithm**: Uses geometry optimization.
- **Input Format**: Accepts reduced models.
- **Output**: Produces full atom models.
- **Use Case**: Protein modeling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large proteins require memory.
- **Data Quality**: Results depend on input quality.
- **Structure Complexity**: May affect accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pulchra --help`
**Explanation:** Shows available options and usage instructions.

### Reconstruct structure
**Args:** `pulchra -i input.pdb -o output.pdb`
**Explanation:** Reconstructs all-atom model.

### With parameters
**Args:** `pulchra -i input.pdb -p params.txt -o output.pdb`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pulchra -v -i input.pdb -o output.pdb`
**Explanation:** Runs with verbose output.

### Refinement mode
**Args:** `pulchra -r -i input.pdb -o output.pdb`
**Explanation:** Performs structure refinement.

### Output format
**Args:** `pulchra -i input.pdb -o output.pdb --mmcif`
**Explanation:** Outputs in mmCIF format.

### Generate report
**Args:** `pulchra -i input.pdb -o output.pdb --report report.html`
**Explanation:** Generates HTML report.