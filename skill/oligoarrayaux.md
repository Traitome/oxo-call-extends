---
name: oligoarrayaux
category: utility
description: OligoArrayAux is a subset of UNAFold for oligonucleotide design and analysis.
tags: [oligoarrayaux, utility, oligonucleotide-design, dna-folding]
author: oxo-call-community
source_url: "http://unafold.rna.albany.edu/?q=DINAMelt/OligoArrayAux"
---

## Concepts

- **Tool Overview**: OligoArrayAux provides tools for oligonucleotide analysis and design.
- **Core Function**: Analyzes oligonucleotide properties and secondary structures.
- **Algorithm**: Uses thermodynamic models for nucleic acid folding.
- **Input Format**: Accepts DNA/RNA sequences and oligonucleotide designs.
- **Output**: Produces melting temperatures and secondary structure predictions.
- **Use Case**: PCR primer design, microarray probe design, and antisense oligonucleotides.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Thermodynamic Models**: Results depend on model parameters.
- **Sequence Length**: May have limitations with very long sequences.
- **Memory Usage**: Complex analyses require memory.
- **Computational Cost**: Folding calculations can be intensive.
- **Validation**: Results should be experimentally validated.

## Examples

### Display help
**Args:** `oligoarrayaux --help`
**Explanation:** Shows available options and usage instructions.

### Calculate Tm
**Args:** `oligotm -i oligonucleotide.txt -o tm_result.txt`
**Explanation:** Calculates melting temperature.

### Secondary structure
**Args:** `hybrid-ss-min -i sequences.txt -o structures.txt`
**Explanation:** Predicts secondary structures.

### Oligo design
**Args:** `oligodesign -i target.fasta -o primers.txt`
**Explanation:** Designs oligonucleotides for target sequence.

### Batch processing
**Args:** `oligotm -d oligos/ -o results/`
**Explanation:** Processes multiple oligonucleotide files.

### Verbose mode
**Args:** `oligotm -i oligonucleotide.txt -v -o tm_result.txt`
**Explanation:** Runs with verbose output.

### Parameters
**Args:** `oligotm -i oligonucleotide.txt -s 50 -o tm_result.txt`
**Explanation:** Sets salt concentration to 50 mM.