---
name: py_fasta_validator
category: formatting
description: py_fasta_validator validates FASTA files and returns non-zero exit codes for invalid files.
tags: [py_fasta_validator, formatting, fasta, validation]
author: oxo-call-community
source_url: "https://github.com/linsalrob/py_fasta_validator"
---

## Concepts

- **Tool Overview**: py_fasta_validator checks FASTA validity.
- **Core Function**: FASTA file validation.
- **Algorithm**: Uses format checking.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces validation status.
- **Use Case**: Quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Format Strictness**: May reject valid variants.
- **Encoding Issues**: May fail on unusual characters.
- **Runtime**: Validation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `py_fasta_validator --help`
**Explanation:** Shows available options and usage instructions.

### Validate FASTA
**Args:** `py_fasta_validator -i genome.fasta`
**Explanation:** Validates FASTA file format.

### With parameters
**Args:** `py_fasta_validator -i genome.fasta -p params.yaml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `py_fasta_validator -v -i genome.fasta`
**Explanation:** Runs with verbose output.

### Check multiple files
**Args:** `py_fasta_validator -i file1.fasta file2.fasta file3.fasta`
**Explanation:** Validates multiple FASTA files.

### Output report
**Args:** `py_fasta_validator -i genome.fasta -o report.txt`
**Explanation:** Outputs validation report.

### Generate HTML report
**Args:** `py_fasta_validator -i genome.fasta --report report.html`
**Explanation:** Generates HTML report.