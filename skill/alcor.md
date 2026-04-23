---
name: alcor
category: utility
description: Alignment-free toolkit for simulation, mapping, and visualization of low-complexity regions in FASTA data
tags: [low-complexity, simulation, masking, visualization, alignment-free]
author: oxo-call-community
source_url: "https://github.com/cobilab/alcor"
---

## Concepts

- **Tool Overview**: AlcoR is an alignment-free toolkit for simulating, mapping, masking, and visualizing low-complexity regions (LCRs) in biological sequence data.
- **Core Function**: Identifies and characterizes low-complexity regions in DNA and protein sequences without requiring sequence alignment.
- **Input/Output**: Input: FASTA sequences. Output: LCR annotations, masked sequences, simulation data, visualization plots.
- **Four Modes**: Simulate (generate LCR sequences), Map (identify LCRs), Mask (replace LCRs), Visualize (plot LCR distribution).
- **Installation**: Install via bioconda: `conda install -c bioconda alcor`

## Pitfalls

- **LCR Definition**: Different applications may require different LCR definitions - adjust parameters accordingly.
- **Sequence Type**: Parameters differ between DNA and protein sequences - specify correct type.
- **Masking Impact**: Masking LCRs may remove biologically relevant regions - review before downstream analysis.
- **Simulation Fidelity**: Simulated LCRs may not capture all biological complexity - use as approximation only.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available modes and options for AlcoR.

### Map low-complexity regions
**Args:** `map -i sequences.fasta -o lcr_annotations.tsv`
**Explanation:** Identifies and maps low-complexity regions in input sequences.

### Mask LCRs in sequences
**Args:** `mask -i sequences.fasta -o masked.fasta`
**Explanation:** Replaces low-complexity regions with N/X characters.

### Simulate LCR sequences
**Args:** `simulate -l 1000 -n 50 -o simulated_lcrs.fasta`
**Explanation:** Generates 50 simulated sequences of 1000bp with embedded LCRs.

### Visualize LCR distribution
**Args:** `visualize -i sequences.fasta -o lcr_plot.png`
**Explanation:** Creates visualization of LCR distribution across sequences.

### Set LCR detection threshold
**Args:** `map -i sequences.fasta -t 0.8 -o lcr.tsv`
**Explanation:** Uses 0.8 complexity threshold for LCR detection.

### Map protein sequences
**Args:** `map -i proteins.fasta --protein -o protein_lcr.tsv`
**Explanation:** Maps LCRs in amino acid sequences with protein-specific parameters.

### Mask with soft masking
**Args:** `mask -i sequences.fasta --soft-mask -o soft_masked.fasta`
**Explanation:** Uses lowercase characters for soft masking instead of N/X.
