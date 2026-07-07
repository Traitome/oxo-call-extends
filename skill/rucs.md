---
name: rucs
category: primer_design
description: RUCS - A bioinformatics tool for designing PCR primers.
tags: ["rucs", "primer", "PCR", "design", "genome-editing"]
author: oxo-call-community
source_url: "https://cge.cbs.dtu.dk/services/rucs/instructions.php"
---

## Concepts

- **Tool Overview**: RUCS (v1.0.3) is a primer design tool developed by the Center for Genomic Epidemiology. It designs PCR primers for DNA amplification, with special focus on avoiding primer-dimer formation and optimizing specificity.
- **Core Function**: Designs forward and reverse primers for target DNA sequences, considering melting temperature, GC content, primer length, and potential secondary structures.
- **Algorithm**: Uses thermodynamic calculations to predict primer melting temperature, checks for primer-dimer and hairpin formation, and selects optimal primers based on multiple criteria.
- **Input Format**: FASTA format target sequences, or genomic coordinates with reference genome.
- **Output Format**: Primer sequences with melting temperature, GC content, and specificity metrics. Optional BED format for primer positions.
- **Use Case**: PCR primer design for cloning, sequencing, mutagenesis, and diagnostic assays.

## Pitfalls

- **Reference genome requirement**: For genomic primer design, requires indexed reference genome.
- **Specificity issues**: May not detect all potential off-target binding sites.
- **Thermodynamic assumptions**: Primer Tm calculations are estimates and may vary in practice.
- **Complex templates**: May struggle with highly repetitive or GC-rich sequences.
- **Parameter sensitivity**: Default parameters may need adjustment for specific applications.
- **Output interpretation**: Requires understanding of primer design principles to select best primers.

## Examples

### Basic primer design
**Args:** `rucs -i target.fasta -o primers.txt`
**Explanation:** `-i` input FASTA file with target sequence; `-o` output file with designed primers.

### Specify primer length
**Args:** `rucs -i target.fasta -o primers.txt -l 20-25`
**Explanation:** `-l` specifies primer length range (20-25 nucleotides).

### Set Tm range
**Args:** `rucs -i target.fasta -o primers.txt -t 55-65`
**Explanation:** `-t` sets melting temperature range in degrees Celsius.

### Design with reference genome
**Args:** `rucs -g genome.fasta -c chr1:1000-2000 -o primers.txt`
**Explanation:** `-g` reference genome; `-c` genomic coordinates. Designs primers for specific region.

### Avoid primer-dimer
**Args:** `rucs -i target.fasta -o primers.txt --strict`
**Explanation:** `--strict` enables stricter primer-dimer checking.

### Batch primer design
**Args:** `rucs -i targets.fasta -o primers.txt -b`
**Explanation:** `-b` batch mode for multiple target sequences in one FASTA file.

### Output BED format
**Args:** `rucs -i target.fasta -o primers.bed --bed`
**Explanation:** `--bed` outputs primer positions in BED format.
