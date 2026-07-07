---
name: rnashapes
category: utility
description: RNAshapes abstraction maps RNA secondary structures to a tree-like domain of abstract shapes, preserving nesting/adjacency but ignoring helix lengths; used for fast shape-based structure analysis and prediction.
tags: ["rnashapes", "rna-shapes", "abstraction", "secondary-structure", "dynamic-programming"]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/fold-grammars"
---

## Concepts

- **Tool Overview**: RNAshapes (v3.4.0, Bielefeld / Giegerich et al.) is a tool and library for RNA secondary structure analysis and prediction using "abstract shapes" — a domain of tree-like structural descriptors that preserve the nesting and adjacency of helices and loops but abstract away exact helix lengths. It avoids the exponential blow-up of enumerating all suboptimal structures.
- **Core Function**: Takes an RNA sequence and reports the Boltzmann-weighted abstract shapes (e.g., `[[]]`, `[[][]]`, `[[[][]]]`) of the structure ensemble, optionally with a probability threshold. It can also enumerate suboptimal structures that map to a chosen shape. The output is far more compact than `RNAsubopt` and is the basis for the `RNAlyzable` and `kissing loop` analyses in the Giegerich group.
- **Algorithm**: Shape abstraction is built into the dynamic programming of RNA folding: during the partition-function fold, the DP is annotated with shape identifiers, and equivalent structures (same shape) are merged. This is faster than folding + post-hoc shape abstraction. The shapes are drawn from a five-level hierarchy (no abstractions `[1-5]`) parameterized by an abstracting shape grammar.
- **Input Format**: A single FASTA file (one or more sequences) or a single sequence via stdin. Optional flags select the shape level (`-s 1` to `-s 5`, with `1` being the most abstract and `5` being the most detailed), an energy range (`-e 5.0` kcal/mol), and a probability threshold (`-p 0.01`).
- **Output Format**: Plain-text report with the shape ID, the probability in the Boltzmann ensemble, the count of concrete structures mapping to that shape, and a representative structure. The most probable shape is listed first. Output to stdout by default; `--xml` or `--json` for machine-readable output.
- **Use Case**: Quickly identifying the dominant secondary structure families of an RNA (e.g., is this riboswitch a hairpin or a three-way junction?), comparing the shape ensemble of two related RNAs, and feeding shape-annotated structures into the `knotinframe` or `pyle` family of tools.

## Pitfalls

- **CRITICAL — Shape level 1 is the most abstract, not the most detailed**: The `-s` flag is INVERTED relative to most users' intuition: `-s 1` collapses all loops into a generic `[]` (very abstract), `-s 5` distinguishes hairpin loops from internal loops (detailed). Default is `-s 5`. If your output looks like a single `[]` for everything, you probably meant `-s 5`.
- **CRITICAL — Probabilities sum to ≤ 1, not necessarily = 1**: The reported probability of each shape is the Boltzmann probability of the structure ensemble falling into that shape; the unaccounted probability corresponds to structures that do not map to any of the listed shapes (e.g., at the requested energy range cutoff). To get the full partition function, raise the energy range to `-e 100`.
- **ViennaRNA's RNAfold is a runtime dependency**: RNAshapes calls RNAfold internally. The Bioconda recipe pulls it; verify with `RNAfold --version` before launching a run.
- **Shape IDs are stable across runs**: The ID `[[]]` always means "hairpin inside a hairpin" (nested hairpins). Stable IDs are critical for downstream shape-comparison tools; do not parse the dot-bracket representation when an ID is sufficient.
- **Very long sequences (> 5000 nt) are slow**: The shape-annotated partition function is O(n³) in sequence length; the practical limit is ~3000 nt. For longer sequences (e.g., full mRNAs), use `RNAfold -p` and post-process with `RNAshapes --mode=abstract`.
- **`--keep` must be used to preserve suboptimal structures**: By default only the MFE structure is reported per shape; pass `--keep` to retain the suboptimals, useful for downstream `pyle` analyses.

## Examples

### Compute the shape ensemble of a sequence
**Args:** `RNAshapes -s 5 -p 0.001 input.fa`
**Explanation:** `-s 5` is the most detailed shape level, `-p 0.001` keeps only shapes with probability ≥ 0.001. Output lists each shape with its ID, probability, and a representative dot-bracket structure.

### Use a more abstract shape level
**Args:** `RNAshapes -s 2 -p 0.01 input.fa`
**Explanation:** `-s 2` collapses simple internal loops and bulges, useful when you want to know the overall topology (e.g., is it a multi-branch loop with three arms or five?). Probability threshold `0.01` filters to common shapes.

### Restrict the energy range
**Args:** `RNAshapes -s 5 -e 3.0 -p 0.01 input.fa`
**Explanation:** `-e 3.0` keeps only structures within 3.0 kcal/mol of the MFE, dramatically reducing the output for long sequences. Use this for a quick sanity check before running the full partition function.

### XML output for downstream parsing
**Args:** `RNAshapes -s 5 --xml -p 0.01 input.fa > shapes.xml`
**Explanation:** `--xml` writes a machine-readable XML document with one `<shape>` element per reported shape, including the probability, count, and a representative dot-bracket structure. Easier to parse with `xmlstarlet` or Python's `xml.etree`.

### Compare shapes between two sequences
**Args:** `RNAshapes -s 5 -p 0.01 seq1.fa > s1.shapes; RNAshapes -s 5 -p 0.01 seq2.fa > s2.shapes; comm -12 <(awk '{print $1}' s1.shapes | sort -u) <(awk '{print $1}' s2.shapes | sort -u)`
**Explanation:** Composite example: compute shapes for two related RNAs, then use `comm` to find the shape IDs common to both. A high overlap suggests shared structural topology; a low overlap suggests structural divergence.

### Use shape abstraction as a post-processor for RNAfold
**Args:** `RNAfold -p --noLP < input.fa > fold.out && grep -v "^>" fold.out | awk '/[{}]/' | RNAshapes -s 5 --mode=abstract > abstract.shapes`
**Explanation:** Composite example: first run RNAfold's partition function, then pipe the structure to RNAshapes in `--mode=abstract` to obtain shape IDs. Useful when the input is already folded by a different tool (e.g., RNAstructure, NUPACK).

### Restrict to a specific shape
**Args:** `RNAshapes -s 5 -P "[[][][]]" -p 0.01 input.fa`
**Explanation:** `-P` (or `--shape`) restricts the search to a specific shape ID, e.g., `[[][]]` (a three-way junction with two internal loops). Useful when you have a prior on the topology and want to know how likely it is.
