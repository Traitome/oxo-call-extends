---
name: promod3
category: population-genomics
description: promod3 performs protein structure prediction and refinement.
tags: [promod3, population-genomics, protein-structure, modeling]
author: oxo-call-community
source_url: "https://openstructure.org/promod3/"
---

## Concepts

- **Tool Overview**: promod3 predicts protein structures.
- **Core Function**: Protein structure modeling.
- **Algorithm**: Uses homology modeling methods.
- **Input Format**: Accepts FASTA/PDB files.
- **Output**: Produces structural models.
- **Use Case**: Structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex structures require memory.
- **Data Quality**: Results depend on template quality.
- **Model Accuracy**: May have structural errors.
- **Runtime**: Modeling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `promod3 --help`
**Explanation:** Shows available options and usage instructions.

### Predict structure
**Args:** `promod3 -i sequence.fasta -o model.pdb`
**Explanation:** Predicts protein structure.

### With parameters
**Args:** `promod3 -i sequence.fasta -p params.yaml -o model.pdb`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `promod3 -v -i sequence.fasta -o model.pdb`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `promod3 -t 4 -i sequence.fasta -o model.pdb`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `promod3 -i sequence.fasta -o model.cif --mmcif`
**Explanation:** Outputs in mmCIF format.

### Generate report
**Args:** `promod3 -i sequence.fasta -o model.pdb --report report.html`
**Explanation:** Generates HTML report.