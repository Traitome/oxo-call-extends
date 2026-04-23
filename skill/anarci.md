---
name: anarci
category: annotation
description: ANARCI - Antibody Numbering and Antigen Receptor Classification for antibody and T-cell receptor sequences
tags: [antibody, numbering, immunoglobulin, tcr, imgt, kabat, chothia]
author: oxo-call-community
source_url: "https://github.com/oxpig/ANARCI"
---

## Concepts

- **Tool Overview**: ANARCI classifies and numbers antibody and T-cell receptor (TCR) amino acid variable domain sequences using multiple numbering schemes. Version 2024.05.21.
- **Numbering Schemes**: Supports IMGT (128 positions, all receptor types), Chothia (IG only), Kabat (IG only), Martin/Enhanced Chothia (IG only), AHo (149 positions, all types), Wolfguy (IG only).
- **Receptor Types**: Identifies and numbers heavy chains (H), light chains (kappa/L, lambda), TCR alpha (A), and TCR beta (B) chains.
- **Species Detection**: Automatically detects species from V/J germline alignment. Supports human, mouse, rat, rabbit, pig, rhesus monkey.
- **Germline Assignment**: Optional `--assign_germline` identifies most similar V and J germline genes with identity percentages.
- **HMM-Based**: Uses profile Hidden Markov Models for accurate chain type classification and domain boundary detection.
- **Batch Processing**: Accepts single sequences on command line or FASTA files for batch processing.

## Pitfalls

- **Input Format**: Requires amino acid sequences (protein), not nucleotide. Convert DNA sequences before running ANARCI.
- **Species Annotation**: ANARCI determines species from germline alignment for numbering purposes, but is not recommended as primary species annotation tool.
- **Non-Standard Species**: Species like alpaca VHH may number correctly but species annotation may be inaccurate.
- **Partial Sequences**: Sequences missing framework regions may fail to number correctly. Ensure input includes complete variable domain.
- **HMMER Dependency**: Requires HMMER 3.3.2 for HMM profile searches. Must be installed and in PATH.
- **Output Interpretation**: Different numbering schemes have different insertion position conventions. Understand chosen scheme before interpreting results.

## Examples

### Number single antibody sequence
**Args:** `ANARCI -i EVQLQQSGAEVVRSGASVKLSCTASGFNIKDYYIHWVKQRPEKGLEWIGWIDPEIGDTEYVPKFQGKATMTADTSSNTAYLQLSSLTSEDTAVYYCNAGHDYDRGRFPYWGQGTLVTVSA`
**Explanation:** Numbers a single heavy chain variable domain sequence using default IMGT scheme. Outputs numbered sequence to stdout.

### Number FASTA file of sequences
**Args:** `ANARCI -i antibodies.fasta --outfile numbered.txt`
**Explanation:** Numbers all sequences in FASTA file. Writes results to numbered.txt instead of stdout. Useful for batch processing.

### Use Kabat numbering scheme
**Args:** `ANARCI -i antibodies.fasta -s kabat --outfile kabat_numbered.txt`
**Explanation:** Uses Kabat numbering scheme instead of default IMGT. Kabat is the classic scheme with A-Z insertion positions. Primarily for IG sequences.

### Assign germline genes
**Args:** `ANARCI -i antibodies.fasta --assign_germline --outfile germline_assigned.txt`
**Explanation:** Identifies most similar V and J germline genes for each sequence. Reports gene identifiers and sequence identity percentages. Useful for antibody engineering.

### Output CSV format
**Args:** `ANARCI -i antibodies.fasta --csv --outfile output.csv`
**Explanation:** Outputs results in CSV format with separate files per chain type. Easier to parse programmatically for downstream analysis pipelines.

### Use AHo numbering scheme
**Args:** `ANARCI -i antibodies.fasta -s aho --outfile aho_numbered.txt`
**Explanation:** Uses AHo numbering scheme (149 possible positions, no insertions). Useful for structural comparisons as all positions are structurally equivalent.

### Number TCR sequences
**Args:** `ANARCI -i tcr_sequences.fasta --outfile tcr_numbered.txt`
**Explanation:** ANARCI automatically detects and numbers TCR alpha and beta chains. Uses IMGT scheme (default) which supports all receptor types.

### Specify output file for specific scheme
**Args:** `ANARCI -i antibodies.fasta -s chothia --outfile chothia_results.txt -r martin --outfile martin_results.txt`
**Explanation:** Numbers sequences with multiple schemes in one run. Compare numbering across schemes for the same sequences.