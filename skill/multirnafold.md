---
name: multirnafold
category: utility
description: RNA/DNA secondary structure prediction for multiple interacting strands using ViennaRNA package.
tags: [multirnafold, rna-structure, secondary-structure, bioinformatics, viennarna, rna-folding]
author: oxo-call-community
source_url: "https://www.tbi.univie.ac.at/RNA/RNAfold"
---

## Concepts

- **Tool Overview**: MultiRNAfold (part of ViennaRNA package) predicts secondary structures for multiple interacting RNA or DNA strands, computing minimum free energy (MFE) structures and base pairing probabilities.
- **Core Function**: Calculates MFE structures and partition function for RNA/DNA complexes where multiple strands can form interconnected structures. Handles input sequences concatenated with '&' separator.
- **Algorithm**: Uses dynamic programming with Turner 2004 energy parameters for RNA or Matthews model for DNA. Computes full ensemble properties including base pairing probability matrices.
- **Input Format**: Reads sequences from stdin or files in FASTA format. Multiple strands specified by concatenating with '&' character (e.g., "GGGAAACCC&CCCAAAGGG").
- **Output**: Produces MFE structure in dot-bracket notation, ensemble free energy, and PostScript files for structure visualization and dot plots of base pairing probabilities.
- **Applications**: RNA-RNA interaction prediction, riboswitch modeling, DNA aptamer structure prediction, siRNA design, and CRISPR guide RNA accessibility analysis.

## Pitfalls

- **Strand Concatenation**: Input sequences must be concatenated with exactly '&' with no spaces. "RNA1&RNA2" works but "RNA1 & RNA2" fails. Check for invisible spaces in pasted sequences.
- **Sequence Alphabet**: For DNA prediction, use 'T' not 'U'. The tool auto-converts T→U internally for RNA parameters but DNA parameters require explicit DNA alphabet.
- **Long Sequences**: Computational complexity is O(n^3) for partition function. Sequences over ~1000 nt become very slow. For long RNAs, consider fragmenting and analyzing domain-by-domain.
- **Temperature Settings**: Default temperature is 37°C. Use `--temp` to change for thermophilic organisms or specialized applications. Energy parameters are only validated for 0-100°C range.
- **Dangling Ends**: Default dangling end treatment (dangles=2) may not match experimental conditions. Use `-d 1` or `-d 0` for more restrictive models in constrained structures.
- **Output File Overwriting**: PostScript output files (ss.ps, dp.ps) are overwritten without warning if they already exist. Back up existing files before re-running.

## Examples

### Predict MFE structure for two interacting RNAs
**Args:** `echo "GGGAAACCC&GGGUUUCCC" | multirnafold`
**Explanation:** Predicts the minimum free energy structure for two RNA strands forming a complex. Output includes dot-bracket structure, MFE value in kcal/mol, and PostScript structure plot.

### Compute partition function and base pairing probabilities
**Args:** `echo "AUCG&CGUA" | multirnafold -p -o rna_complex`
**Explanation:** The `-p` flag computes partition function to obtain base pairing probabilities. Output includes ensemble free energy, frequency of MFE structure in ensemble, and a dot plot showing probability values.

### Process multiple sequence pairs from file
**Args:** `multirnafold -j 4 < sequence_pairs.txt`
**Explanation:** Reads multiple sequence pairs from input file and processes them in parallel using 4 threads. Each line should contain one sequence pair with '&' separator.

### Use custom temperature for thermophilic organism
**Args:** `echo "CCCGGG&CCCGGG" | multirnafold --temp 50`
**Explanation:** Sets temperature to 50°C for predicting structures in thermophilic organisms. Energy parameters are interpolated within the valid range (0-100°C).

### Generate unannotated structure plot
**Args:** `multirnafold --noconv --auto-id --id-prefix "myRNA" -i input.fa`
**Explanation:** Uses automatic ID generation with custom prefix and no nucleotide conversion. Reads from FASTA file and outputs files named myRNA_0001_ss.ps, myRNA_0002_ss.ps, etc.

### Produce CSV output for downstream analysis
**Args:** `echo "ACGU&UGCA" | multirnafold --csv`
**Explanation:** Generates machine-readable CSV output with MFE, ensemble energy, and per-residue pairing probabilities. Useful for integrating with Python/R pipelines.
