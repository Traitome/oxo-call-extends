---
name: revtrans
category: alignment
description: RevTrans performs reverse translation of peptide alignments to nucleotide sequences.
tags: [revtrans, alignment, reverse-translation, bioinformatics]
author: oxo-call-community
source_url: "http://www.cbs.dtu.dk/services/RevTrans-2.0/web/download.php"
---

## Concepts

- **Tool Overview**: revtrans reverse translates.
- **Core Function**: Peptide to nucleotide translation.
- **Algorithm**: Uses codon table methods.
- **Input Format**: Accepts peptide alignments.
- **Output**: Produces nucleotide alignments.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Codon Usage**: Affects translation.
- **Parameters**: Must be configured.
- **Runtime**: Translation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `revtrans -h`
**Explanation:** Shows available options and usage instructions.

### Reverse translate
**Args:** `revtrans -i peptide.fasta -o nucleotide.fasta`
**Explanation:** Reverse translates peptide alignment.

### With parameters
**Args:** `revtrans -i peptide.fasta -p params.txt -o nucleotide.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `revtrans -v -i peptide.fasta -o nucleotide.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `revtrans -t 4 -i peptide.fasta -o nucleotide.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With codon table
**Args:** `revtrans -i peptide.fasta -c table.txt -o nucleotide.fasta`
**Explanation:** Uses custom codon table.

### Generate report
**Args:** `revtrans -i peptide.fasta -o nucleotide.fasta --report report.html`
**Explanation:** Generates HTML report.