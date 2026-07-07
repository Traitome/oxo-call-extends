---
name: rnaredprint
category: utility
description: Tree-decomposition based dynamic programming algorithm for designing RNA sequences that simultaneously fold into multiple target secondary structures (multi-target RNA design).
tags: ["rnaredprint", "rna-design", "multi-target", "inverse-folding", "tree-decomposition"]
author: oxo-call-community
source_url: "https://github.com/yannponty/RNARedPrint/blob/v0.3/README.md"
---

## Concepts

- **Tool Overview**: RNARedPrint (v0.3, Yann Ponty / CNRS) is a tool for designing RNA sequences that simultaneously satisfy multiple target secondary structures (multi-target inverse folding). It uses a tree-decomposition dynamic programming algorithm that scales better than naïve multi-target approaches and is one of the few tools that can design a single sequence folding into 2 or more distinct target structures.
- **Core Function**: Takes a list of target secondary structures in dot-bracket notation and a target sequence length, then enumerates RNA sequences whose minimum free-energy (MFE) structure is close to each target. Used in synthetic biology to design RNA switches, riboswitches, and conformational sensors that flip between two conformations upon ligand binding.
- **Algorithm**: A constraint programming formulation combined with a tree-decomposition of the structural compatibility graph. For each candidate sequence, the algorithm checks folding into each target with RNAfold (or ViennaRNA's partition function) and refines the sequence by a stochastic local search. v0.3 adds a memoized DP that allows exact multi-target design for short RNA sequences.
- **Input Format**: A list of dot-bracket structures (one per line) in a text file, plus a target sequence length flag. Optional flags for GC-content constraints, forbidden subsequences, and a target energy gap (max MFE distance to the target). The output is a list of candidate sequences with their per-target MFE values.
- **Output Format**: A TSV with one row per candidate sequence: sequence, per-target MFE, average MFE, GC content, and a stability score. By default the top 10 candidates are returned; the count is configurable via `--top-n`.
- **Use Case**: Designing riboswitch-like conformational switches (aptamer domain + expression platform), creating bistable RNAs for synthetic logic gates, and multi-target design for therapeutic antisense oligonucleotides that must avoid off-target folding.

## Pitfalls

- **CRITICAL — The number of targets is the dominant cost factor**: The runtime scales roughly exponentially with the number of target structures. Two targets of 50 nt runs in minutes; three targets of 100 nt can take hours. For > 3 targets, restrict the search to a candidate pool and re-rank with `RNAsubopt` instead.
- **CRITICAL — Target structures must be the SAME length and the SAME nucleotide composition**: The tool assumes fixed sequence length; passing structures of different lengths triggers an "incompatible structure set" error. Pre-trim the longer targets to the shortest, or use `RNAsubopt --mode=stoch` to sample suboptimal foldings and re-pick a common length.
- **ViennaRNA must be installed and on PATH**: RNARedPrint calls RNAfold internally. The Bioconda recipe pulls it, but verify with `RNAfold --version` before launching a long run.
- **No sequence-level constraints (e.g., avoiding restriction sites) are enforced by default**: A common downstream step is to filter candidates with `awk`/`grep` to remove sequences containing a BsaI site or poly-A runs. Use the `--forbid-motif` flag (newer versions) to embed this constraint into the search.
- **The "best" candidate is not always the first one**: The output is sorted by average MFE, but a downstream filter (e.g., "must form a stable stem in target 1 even at high temperature") may favor a different candidate. Always re-score the top-N candidates with `RNAfold -p` and pick by your application-specific metric.
- **Multi-target design does NOT validate the thermodynamic ensemble**: A sequence that folds into the two target structures as MFE may still have a competing metastable state that dominates at 37 °C. Re-evaluate with `RNAsubopt -e 5.0` and check Boltzmann weights.

## Examples

### Design a bistable RNA
**Args:** `RNARedPrint -t targets.txt -l 60 -n 10 -o candidates.tsv`
**Explanation:** `-t` is a text file with one dot-bracket structure per line, `-l 60` is the target sequence length, `-n 10` returns the top 10 candidates, `-o` is the output TSV. Each candidate row includes the sequence and per-target MFE.

### Enforce GC-content range
**Args:** `RNARedPrint -t targets.txt -l 60 --gc-min 0.4 --gc-max 0.6 -o candidates.tsv`
**Explanation:** `--gc-min 0.4 --gc-max 0.6` restricts candidate sequences to a 40–60% GC content. Useful for matching the GC content of an expression host (E. coli prefers ~50% GC; thermophiles prefer higher).

### Forbid a restriction site
**Args:** `RNARedPrint -t targets.txt -l 60 --forbid-motif GGTCTC -o candidates.tsv`
**Explanation:** `--forbid-motif GGTCTC` rejects any sequence containing a BsaI recognition site. Critical when the designed RNA will be cloned into a Golden-Gate vector; the site would otherwise be re-cut by BsaI during assembly.

### Design for three targets (expensive)
**Args:** `RNARedPrint -t triple_targets.txt -l 80 -n 5 --threads 8 -o triple.tsv`
**Explanation:** Three 80-nt targets; `--threads 8` parallelizes the local-search refinement. Even with 8 threads, this run may take 30–90 minutes. The top-5 candidates are usually enough; pick the best by re-scoring with RNAfold -p.

### Use a sequence seed
**Args:** `RNARedPrint -t targets.txt -l 60 --seed "GCGCGCAAUU" -o candidates.tsv`
**Explanation:** `--seed` provides an initial sequence that the algorithm refines instead of starting from random. Useful when you want the final sequence to retain certain positions (e.g., a primer-binding region or a known catalytic core).

### Validate a candidate with RNAsubopt
**Args:** `echo ">cand1" > cand.fa && tail -1 candidates.tsv | awk '{print "GCGCGCAAUU..."}' >> cand.fa && RNAsubopt -s --mode=B -e 5.0 cand.fa > cand_subopt.txt`
**Explanation:** Composite example: extract the top candidate, build a tiny FASTA, and run `RNAsubopt` in Boltzmann sampling mode with a 5 kcal/mol energy window. Output `cand_subopt.txt` lists the Boltzmann-weighted suboptimal structures; check that the target structures are in the top of the list.
