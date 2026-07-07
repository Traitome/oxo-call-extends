---
name: rrikindp
category: utility
description: RRIkinDP — evaluation of thermodynamic and kinetic features of RNA-RNA interactions by computing barrier energies for the best direct path on a state space of intermediate interactions.
tags: ["rrikindp", "rri-kindp", "rna-rna-interaction", "kinetics", "thermodynamics", "rna-folding", "intarna", "viennarna"]
author: oxo-call-community
source_url: "https://github.com/mwaldl/RRIkinDP"
---

## Concepts

- **Tool Overview**: RRIkinDP (RNA-RNA Interaction kinetic DP, v0.0.2, Waldl et al.) is a Python/C++ tool for evaluating the thermodynamic and kinetic features of RNA-RNA interactions. It takes two RNA sequences and their full interaction structure, generates the state space of all intermediate interactions (from single base-pair interactions up to the full input interaction), and computes the barrier energy for the best direct path from a given start interaction to the full input interaction.
- **Core Function**: Builds the state space of intermediate interactions (an explicit graph of partial duplexes with their free energies), then runs a dynamic-programming search for the lowest-barrier pathway from a start state to the full interaction. The output is the barrier energy, the corresponding pathway, and the energy of each intermediate state. InteRNA / ViennaRNA are used for free-energy evaluation.
- **Algorithm**: (1) Generate all valid sub-interactions of the full interaction; (2) compute the free energy of each sub-interaction with InteRNA; (3) build the state graph; (4) find the best direct path (minimum barrier energy) from the start to the full interaction. The barrier energy is the maximum energy along the path minus the energy of the start state.
- **Input Format**: (1) Two RNA sequences in FASTA format (one file each, or a multi-FASTA); (2) the full interaction structure in a dot-bracket-interaction format (the standard InteRNA/ViennaRNA interaction-DB format, e.g., `((((...))))....((..))`); (3) the start interaction in the same format. InteRNA must be run first to produce the interaction, or it can be supplied manually.
- **Output Format**: A JSON or TSV file with the pathway: `start_state, intermediate_states, full_state, barrier_energy, path_energies`. Visualization of the state graph and the best path is supported via matplotlib/seaborn (PNG/SVG).
- **Use Case**: Modeling the kinetics of RNA-RNA interaction formation (e.g., miRNA–mRNA, snRNA–pre-mRNA, riboswitches), studying the folding pathway of a duplex, comparing the barrier energies of competing interactions, and predicting the most likely kinetic intermediate in a co-transcriptional RNA-RNA interaction.

## Pitfalls

- **CRITICAL — InteRNA is a hard dependency**: RRIkinDP uses InteRNA (v3.4.1) and ViennaRNA (v2.6.0–2.7.x) for free-energy evaluation. They must be installed (e.g., `conda install -c bioconda intarna viennarna`); missing libraries cause the tool to crash with a linker error.
- **CRITICAL — The full interaction and the start interaction must be SUB-INTERACTIONS of each other**: The start state must be reachable from the full interaction by removing base pairs (i.e., a sub-interaction). A start state that is not a sub-interaction produces an empty state graph and a misleading barrier energy of 0.
- **The state space can be exponential in the number of base pairs**: An interaction with 50 base pairs has up to 2^50 sub-interactions. The tool prunes the state space by energy threshold, but a permissive threshold can exhaust memory. Use a strict energy threshold for large interactions.
- **Barrier energy is path-DEPENDENT, not state-dependent**: Two different pathways from the same start to the same end can have different barrier energies. The "best" pathway is the one with the lowest barrier; downstream kinetics interpretations must use this best-pathway barrier, not a random pathway.
- **The start interaction defaults to the empty interaction (no base pairs)**: A user who supplies only the full interaction gets the barrier from the empty state — a sensible default for the de novo folding case. For a different start, supply `--start` explicitly.
- **Visualization is in the form of a single combined plot**: The default matplotlib output is one PNG with both the state graph and the best path highlighted. For a publication figure, generate the state graph and the path separately with `--plot-state-graph` and `--plot-path`.

## Examples

### Basic RRIkinDP run
**Args:** `rrikindp --seq1 mir21.fa --seq2 target.fa --interaction "((((....))))....(((...)))" --out pathway.json`
**Explanation:** `--seq1` and `--seq2` are the two RNA FASTA files, `--interaction` is the full interaction in dot-bracket-interaction format, `--out` is the output JSON. The barrier energy and the best pathway are written to `pathway.json`.

### Specify a start interaction
**Args:** `rrikindp --seq1 mir21.fa --seq2 target.fa --interaction "((((....))))....(((...)))" --start "((....))" --out pathway.json`
**Explanation:** `--start` is the start interaction (a sub-interaction of the full). The barrier is computed from this start, not from the empty state. Useful for modeling the kinetics from a pre-formed seed duplex.

### Set an energy threshold for the state space
**Args:** `rrikindp --seq1 mir21.fa --seq2 target.fa --interaction "((((....))))....(((...)))" --energy-threshold -5.0 --out pathway.json`
**Explanation:** `--energy-threshold` is in kcal/mol; sub-interactions with free energy above the threshold are pruned. Lower (more negative) thresholds produce smaller state spaces and faster runs. Default is 0.0 (no pruning).

### Generate a path visualization
**Args:** `rrikindp --seq1 mir21.fa --seq2 target.fa --interaction "((((....))))....(((...)))" --plot-path pathway.png --out pathway.json`
**Explanation:** `--plot-path` writes a PNG of the best pathway on the state graph. Useful for figure generation in publications.

### Multi-threading
**Args:** `rrikindp --seq1 mir21.fa --seq2 target.fa --interaction "((((....))))....(((...)))" --threads 8 --out pathway.json`
**Explanation:** `--threads` enables parallel state-graph generation. Recommended for large interactions (>30 bp) and relaxed energy thresholds.

### Read interactions from an InteRNA output
**Args:** `intarna --query mir21.fa --target target.fa --out interactions.tsv && rrikindp --intarna-output interactions.tsv --top 3 --out pathways.json`
**Explanation:** The InteRNA output is read directly; the top-3 interactions are evaluated for kinetics. Avoids hand-typing the interaction strings. Use `--top N` to limit to the N most stable interactions.
