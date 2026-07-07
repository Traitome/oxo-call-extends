---
name: privateer
category: alignment
description: privateer validates, refines, and analyzes carbohydrate structures.
tags: [privateer, alignment, carbohydrates, structure-analysis]
author: oxo-call-community
source_url: "https://www.ccp4.ac.uk/html/privateer.html"
---

## Concepts

- **Tool Overview**: privateer analyzes carbohydrate structures.
- **Core Function**: Structure validation.
- **Algorithm**: Uses structural analysis methods.
- **Input Format**: Accepts PDB/mmCIF files.
- **Output**: Produces validation reports.
- **Use Case**: Structural biology, glycobiology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Data Quality**: Results depend on input quality.
- **Structure Complexity**: May have validation issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `privateer --help`
**Explanation:** Shows available options and usage instructions.

### Validate structure
**Args:** `privateer -i structure.pdb -o validation.txt`
**Explanation:** Validates carbohydrate structure.

### With parameters
**Args:** `privateer -i structure.pdb -p params.yaml -o validation.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `privateer -v -i structure.pdb -o validation.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `privateer -t 4 -i structure.pdb -o validation.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `privateer -i structure.pdb -o validation.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `privateer -i structure.pdb -o validation.txt --report report.html`
**Explanation:** Generates HTML report.