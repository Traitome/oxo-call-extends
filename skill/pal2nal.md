---
name: pal2nal
category: alignment
description: pal2nal converts protein sequence alignments into codon alignments.
tags: [pal2nal, alignment, codon, protein]
author: oxo-call-community
source_url: "http://www.bork.embl.de/pal2nal/"
---

## Concepts

- **Tool Overview**: pal2nal converts protein alignments to codon alignments.
- **Core Function**: Maps protein alignments back to DNA sequences.
- **Algorithm**: Uses codon mapping and gap handling.
- **Input Format**: Accepts protein alignment and corresponding DNA sequences.
- **Output**: Produces codon-based alignments.
- **Use Case**: Molecular evolution, codon usage analysis, and phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Frame Shifts**: May have issues with frame shifts.
- **Stop Codons**: May introduce premature stop codons.
- **Sequence Length**: Requires matching sequence lengths.
- **Ambiguities**: May handle ambiguous bases differently.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pal2nal.pl --help`
**Explanation:** Shows available options and usage instructions.

### Convert alignment
**Args:** `pal2nal.pl protein.aln dna.fasta -output fasta > codon.aln`
**Explanation:** Converts protein alignment to codon alignment.

### Output format
**Args:** `pal2nal.pl protein.aln dna.fasta -output paml > codon.aln`
**Explanation:** Outputs in PAML format.

### Codon table
**Args:** `pal2nal.pl protein.aln dna.fasta -codontable 11 > codon.aln`
**Explanation:** Uses alternative codon table.

### Verbose mode
**Args:** `pal2nal.pl -v protein.aln dna.fasta > codon.aln`
**Explanation:** Runs with verbose output.

### Remove gaps
**Args:** `pal2nal.pl protein.aln dna.fasta -nogap > codon.aln`
**Explanation:** Removes gap-only positions.

### Clean output
**Args:** `pal2nal.pl protein.aln dna.fasta -clean > codon.aln`
**Explanation:** Removes ambiguous sites.