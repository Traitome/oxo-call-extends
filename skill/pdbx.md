---
name: pdbx
category: formatting
description: pdbx provides Python parser for mmCIF protein structure format.
tags: [pdbx, formatting, mmcif, protein, structure]
author: oxo-call-community
source_url: "https://mmcif.wwpdb.org/docs/sw-examples/python/html/index.html"
---

## Concepts

- **Tool Overview**: pdbx parses mmCIF structures.
- **Core Function**: Reads and writes mmCIF format files.
- **Algorithm**: Uses Python-based parsing.
- **Input Format**: Accepts mmCIF structure files.
- **Output**: Produces parsed structure data.
- **Use Case**: Structural biology, protein analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Format Compliance**: Requires valid mmCIF format.
- **Python Version**: Requires Python 3 environment.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pdbx --help`
**Explanation:** Shows available options and usage instructions.

### Parse mmCIF
**Args:** `pdbx -i structure.cif -o parsed.json`
**Explanation:** Parses mmCIF structure file.

### Convert format
**Args:** `pdbx -i structure.cif -o structure.pdb`
**Explanation:** Converts mmCIF to PDB format.

### Verbose mode
**Args:** `pdbx -v -i structure.cif -o parsed.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pdbx -t 4 -i structure.cif -o parsed.json`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pdbx -i structure.cif -o parsed.xml --xml`
**Explanation:** Outputs in XML format.

### Validate structure
**Args:** `pdbx validate -i structure.cif`
**Explanation:** Validates mmCIF structure.