---
name: purple-bio
category: utility
description: purple-bio picks unique relevant peptides for viral experiments and epitope prediction.
tags: [purple-bio, utility, peptide-selection, viral-research]
author: oxo-call-community
source_url: "https://gitlab.com/HartkopfF/Purple"
---

## Concepts

- **Tool Overview**: purple-bio selects peptides.
- **Core Function**: Peptide selection.
- **Algorithm**: Uses sequence analysis.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces selected peptides.
- **Use Case**: Viral epitope research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Peptide Length**: Affects selection.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `purple-bio --help`
**Explanation:** Shows available options and usage instructions.

### Select peptides
**Args:** `purple-bio -i sequences.fasta -o selected_peptides.txt`
**Explanation:** Selects unique relevant peptides.

### With parameters
**Args:** `purple-bio -i sequences.fasta -p params.yaml -o selected_peptides.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `purple-bio -v -i sequences.fasta -o selected_peptides.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `purple-bio -t 4 -i sequences.fasta -o selected_peptides.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Peptide length
**Args:** `purple-bio -i sequences.fasta -l 9-11 -o selected_peptides.txt`
**Explanation:** Selects peptides of specific length range.

### Generate report
**Args:** `purple-bio -i sequences.fasta -o selected_peptides.txt --report report.html`
**Explanation:** Generates HTML report.