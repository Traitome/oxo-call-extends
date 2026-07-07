---
name: melt
category: utility
description: Nucleotide melting temperature calculator for PCR primer design.
tags: [melt, primer-design, biochemistry]
author: oxo-call-community
source_url: "https://github.com/eclarke/melt"
---

## Concepts

- **Tool Overview**: Melt calculates melting temperature of DNA sequences.
- **Core Function**: Tm calculation for oligonucleotides.
- **Nearest Neighbor**: Uses nearest-neighbor thermodynamics.
- **Salt Adjustment**: Accounts for salt concentration.
- **Primer Design**: Assists in PCR primer optimization.
- **Installation**: `conda install -c bioconda melt`

## Pitfalls

- **Sequence Length**: Limited accuracy for very short/long sequences.
- **Salt Concentration**: Requires accurate salt concentration input.
- **Assumptions**: Based on ideal PCR conditions.
- **Hairpin Formation**: Doesn't account for secondary structure.
- **Dimer Formation**: Doesn't predict primer-dimer interactions.
- **Ambiguity Codes**: May not handle ambiguous bases well.

## Examples

### Calculate Tm
**Args:** `melt ATGCCGTAATGCG`
**Explanation:** Calculates melting temperature for sequence.

### With salt concentration
**Args:** `melt -s 50 ATGCCGTAATGCG`
**Explanation:** Calculates Tm with 50mM salt.

### Primer pair
**Args:** `melt -p ATGCCGTAATGCG CGATTACGGCTA`
**Explanation:** Calculates Tm for primer pair.

### Batch mode
**Args:** `melt -f primers.txt`
**Explanation:** Processes multiple sequences from file.

### Help documentation
**Args:** `melt --help`
**Explanation:** Displays available options.
