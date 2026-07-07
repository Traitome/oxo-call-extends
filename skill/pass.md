---
name: pass
category: expression
description: PASS (Proteome Assembler with Short Sequence peptides) assembles proteomes from short sequences.
tags: [pass, expression, proteomics, peptide-assembly]
author: oxo-call-community
source_url: "https://github.com/BirolLab/PASS"
---

## Concepts

- **Tool Overview**: PASS assembles proteomes from short peptide sequences.
- **Core Function**: Assembles short sequences into complete proteins.
- **Algorithm**: Uses de novo assembly approach for peptides.
- **Input Format**: Accepts short peptide sequences in FASTA format.
- **Output**: Produces assembled proteome sequences.
- **Use Case**: Proteomics, peptide assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on input quality.
- **Overlap Requirements**: Needs sufficient overlaps for assembly.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pass --help`
**Explanation:** Shows available options and usage instructions.

### Assemble proteome
**Args:** `pass -i peptides.fasta -o proteome.fasta`
**Explanation:** Assembles peptides into proteins.

### With reference
**Args:** `pass -i peptides.fasta -r reference.fasta -o proteome.fasta`
**Explanation:** Uses reference for guided assembly.

### Verbose mode
**Args:** `pass -v -i peptides.fasta -o proteome.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pass -t 4 -i peptides.fasta -o proteome.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pass -i peptides.fasta -o proteome.json --json`
**Explanation:** Outputs in JSON format.

### Minimum length
**Args:** `pass -m 50 -i peptides.fasta -o proteome.fasta`
**Explanation:** Sets minimum output sequence length.