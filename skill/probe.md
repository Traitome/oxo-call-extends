---
name: probe
category: utility
description: probe evaluates and visualizes protein interatomic packing.
tags: [probe, utility, protein-structure, visualization]
author: oxo-call-community
source_url: "http://kinemage.biochem.duke.edu/software/probe/"
---

## Concepts

- **Tool Overview**: probe analyzes protein structures.
- **Core Function**: Interatomic packing evaluation.
- **Algorithm**: Uses geometric analysis methods.
- **Input Format**: Accepts PDB files.
- **Output**: Produces packing reports.
- **Use Case**: Protein structure analysis, validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Data Quality**: Results depend on input quality.
- **Structure Complexity**: May have analysis issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `probe --help`
**Explanation:** Shows available options and usage instructions.

### Analyze structure
**Args:** `probe -i protein.pdb -o packing.txt`
**Explanation:** Evaluates interatomic packing in protein structure.

### With parameters
**Args:** `probe -i protein.pdb -p params.txt -o packing.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `probe -v -i protein.pdb -o packing.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `probe -t 4 -i protein.pdb -o packing.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `probe -i protein.pdb -o packing.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `probe -i protein.pdb -o packing.txt --report report.html`
**Explanation:** Generates HTML report.