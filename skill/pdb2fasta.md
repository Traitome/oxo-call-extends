---
name: pdb2fasta
category: formatting
description: pdb2fasta converts PDB structures to FASTA sequences.
tags: [pdb2fasta, formatting, pdb, fasta]
author: oxo-call-community
source_url: "https://github.com/kad-ecoli/pdb2fasta"
---

## Concepts

- **Tool Overview**: pdb2fasta converts PDB to FASTA.
- **Core Function**: Extracts sequences from PDB structures.
- **Algorithm**: Uses structure-to-sequence conversion.
- **Input Format**: Accepts PDB structure files.
- **Output**: Produces FASTA sequence files.
- **Use Case**: Structural biology, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large structures require memory.
- **Structure Quality**: Results depend on PDB quality.
- **Chain Selection**: May need chain specification.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pdb2fasta --help`
**Explanation:** Shows available options and usage instructions.

### Convert PDB
**Args:** `pdb2fasta -i structure.pdb -o sequences.fasta`
**Explanation:** Converts PDB to FASTA sequences.

### With chain
**Args:** `pdb2fasta -i structure.pdb -c A -o sequences.fasta`
**Explanation:** Extracts specific chain sequence.

### Verbose mode
**Args:** `pdb2fasta -v -i structure.pdb -o sequences.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pdb2fasta -t 4 -i structure.pdb -o sequences.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pdb2fasta -i structure.pdb -o sequences.txt --txt`
**Explanation:** Outputs in text format.

### Batch conversion
**Args:** `pdb2fasta -i structures/ -o sequences/`
**Explanation:** Converts multiple PDB files.