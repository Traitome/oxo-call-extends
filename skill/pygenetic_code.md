---
name: pygenetic_code
category: programming
description: pygenetic_code translates DNA sequences using NCBI translation tables and genetic codes.
tags: [pygenetic_code, programming, translation, codon-table]
author: oxo-call-community
source_url: "https://github.com/linsalrob/genetic_codes"
---

## Concepts

- **Tool Overview**: pygenetic_code translates sequences.
- **Core Function**: DNA to protein translation.
- **Algorithm**: Uses codon tables.
- **Input Format**: Accepts DNA sequences.
- **Output**: Produces protein sequences.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Genetic Code**: Must select correct code.
- **Frame Shifts**: Affect translation.
- **Ambiguous Bases**: May cause errors.
- **Stop Codons**: May truncate sequences.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pygenetic_code --help`
**Explanation:** Shows available options and usage instructions.

### Translate sequence
**Args:** `pygenetic_code translate -i dna.fasta -o protein.fasta`
**Explanation:** Translates DNA to protein.

### With parameters
**Args:** `pygenetic_code translate -i dna.fasta -p params.yaml -o protein.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pygenetic_code -v translate -i dna.fasta -o protein.fasta`
**Explanation:** Runs with verbose output.

### Specify genetic code
**Args:** `pygenetic_code translate -i dna.fasta -c 11 -o protein.fasta`
**Explanation:** Uses NCBI genetic code 11.

### List codes
**Args:** `pygenetic_code list`
**Explanation:** Lists available genetic codes.

### Generate report
**Args:** `pygenetic_code translate -i dna.fasta -o protein.fasta --report report.html`
**Explanation:** Generates HTML report.