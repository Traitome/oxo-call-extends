---
name: rnastructure
category: utility
description: Complete package for RNA/DNA secondary structure prediction, partition function, bimolecular structures, oligo binding affinity (siRNA design), and constrained folding with chemical/enzymatic/SHAPE/NMR mapping data.
tags: ["rnastructure", "secondary-structure", "partition-function", "shape", "sirna", "bimolecular"]
author: oxo-call-community
source_url: "https://rna.urmc.rochester.edu/Overview/index.html"
---

## Concepts

- **Tool Overview**: RNAstructure (v6.6, Mathews lab / U Rochester) is a complete C++/Java package for RNA and DNA secondary structure prediction and analysis. It includes algorithms for MFE prediction, partition function / base-pairing probabilities, bimolecular structures, oligo binding affinity (siRNA design), two-sequence joint prediction, and constrained folding with chemical/enzymatic mapping, SHAPE, and NMR data.
- **Core Function**: A set of command-line tools (`Fold`, `partition`, `MaxExpect`, `OligoWalk`, `ProbKnot`, `FoldAsymmetric`, `ScorePseudoknot`) plus a Java GUI for interactive analysis. Each tool addresses one specific task; pipelines are typically composed with shell scripts or Snakemake.
- **Algorithm**: The Mathews lab's re-implementation of the Zuker algorithm (MFE) and the McCaskill partition function, with extensions: `Fold` for single-sequence MFE; `partition` for base-pairing probabilities; `MaxExpect` for maximum-expected-accuracy structures; `OligoWalk` for siRNA binding-affinity scanning; `ProbKnot` for heuristic pseudoknot prediction; constrained folding via `--SHAPE` or `--chem` data files.
- **Input Format**: A single FASTA file with one sequence per record, or a SEQ file (RNAstructure's native format, header + sequence). Chemical mapping is a two-column text file: `position reactivity` (similar to SHAPE). SHAPE data uses the same format. The Java GUI accepts the same inputs plus a CT (connectivity table) file.
- **Output Format**: A CT (connectivity table) file is the canonical output — it lists every nucleotide, its base-pairing partner, and a free-energy annotation. CT files can be visualized with `draw` or converted to dot-bracket with the `ct2dot` companion. The `partition` tool emits a sav (Save file) with the partition function; `MaxExpect` emits a CT.
- **Use Case**: SHAPE-constrained structure prediction (the canonical use case for SHAPE-MaP, in vivo icLASER, and in vivo DMS data), siRNA design (OligoWalk scans a 19–23 nt oligo against a target mRNA and reports binding free energy), bimolecular RNA-RNA duplex prediction (miRNA-mRNA, riboswitch aptamer-expression platform), and pseudoknot prediction with `ProbKnot`.

## Pitfalls

- **CRITICAL — SHAPE data must be 1-indexed, NOT 0-indexed**: RNAstructure uses 1-indexed positions in the `--SHAPE` file; a 0-indexed file silently applies all reactivity to the wrong nucleotides. The SHAPE file format is `position<TAB>reactivity`, with the first base at position 1.
- **CRITICAL — DNA mode is required for DNA sequences**: The default is RNA; for DNA sequences (e.g., aptamer DNAs), pass `--DNA` or use the `Fold --dna` variant. Mixing DNA and RNA in the same input file is not supported.
- **`partition` writes a `sav` file that other tools need**: After running `partition seq.fa sav.txt`, you must run `MaxExpect --probfile=sav.txt seq.fa mea.ct` to get a structure with base-pairing probabilities. There is no single tool that does both.
- **No automatic temperature or ion concentration adjustment**: Default is 37 °C and 1 M NaCl. For in-cell conditions (e.g., 25 °C and 150 mM KCl), pass `--temperature 25.0` and `--sodium 0.15`.
- **ProbKnot is a heuristic, not exact**: It is fast (O(n²)) and handles long sequences (> 5000 nt), but it can miss real pseudoknots and report false positives. For publication-quality pseudoknot prediction, use `HotKnots` or `IPKnot`.
- **OligoWalk is slow for long targets**: A 1500-nt target with a 21-nt oligo at every position takes ~30 minutes; restrict the search to the 3' UTR with `--target-region 1-1500` to speed it up.

## Examples

### Single-sequence MFE folding
**Args:** `Fold seq.fa seq.ct`
**Explanation:** `Fold` reads `seq.fa` and writes the MFE structure in CT format to `seq.ct`. No flags needed for the most common case. Output `seq.ct` can be visualized with `draw seq.ct` (the Java GUI) or converted to dot-bracket with `ct2dot seq.ct 1 seq.db`.

### Partition function and base-pairing probabilities
**Args:** `partition seq.fa sav.txt && MaxExpect --probfile=sav.txt seq.fa mea.ct`
**Explanation:** Two-step: `partition` computes the base-pairing probabilities and writes them to `sav.txt` (a binary save file); `MaxExpect` reads the save file and emits the maximum-expected-accuracy structure in CT format. The `sav.txt` file is also the input to the GUI's "Show Probabilities" view.

### SHAPE-constrained folding
**Args:** `Fold seq.fa seq_shape.ct --SHAPE shape.txt`
**Explanation:** `--SHAPE shape.txt` provides a two-column `position<TAB>reactivity` file; the algorithm uses the reactivity as a soft constraint (Deigan et al. 2009) on the MFE prediction. Output `seq_shape.ct` has a structure informed by the SHAPE data. The reactivity normalization is assumed (top 2% / bottom 8%); raw values should be normalized upstream.

### siRNA binding-affinity scan (OligoWalk)
**Args:** `OligoWalk target.fa sirna_results.txt --length 21 --start 1500 --stop 2000`
**Explanation:** `--length 21` is the oligo length (typical for siRNA), `--start 1500 --stop 2000` scans the 3' UTR region (positions 1500–2000 of the target). Output `sirna_results.txt` is a TSV with the oligo sequence, target position, binding free energy, and accessibility score. The first few rows are the strongest binders.

### Bimolecular duplex (miRNA-mRNA seed)
**Args:** `FoldAsymmetric --A "UGAGGUAGUAGGUUGUAUAGUU" --B "AACUAUACAACCUACUACCUCA" duplex.ct`
**Explanation:** `--A` is the shorter RNA (miRNA), `--B` is the longer RNA (mRNA target). `FoldAsymmetric` predicts the MFE bimolecular structure; output `duplex.ct` shows the duplex and any intramolecular base pairs in each sequence. Use this for miRNA target validation.

### Predict pseudoknots with ProbKnot
**Args:** `ProbKnot seq.fa seq_pk.ct`
**Explanation:** `ProbKnot` runs a heuristic pseudoknot prediction on a single sequence and writes a CT file. For publication-quality predictions, also try `HotKnots` and compare the structures. `ProbKnot` is the only one in the package that supports pseudoknots.

### Two-sequence joint prediction
**Args:** `Fold --sequence seq1.fa --paired seq2.fa joint.ct`
**Explanation:** Predicts a common secondary structure for two unaligned sequences; much more accurate than single-sequence prediction when the sequences are homologs. Output is a CT with two sequences and their consensus structure.
