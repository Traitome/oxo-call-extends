---
name: rnasketch
category: utility
description: RNAsketch library (v1.5, ViennaRNA) for designing RNA sequences that satisfy a target secondary structure, with pluggable backends (ViennaRNA, NUPACK, Hotknots, pKiss) and integration with RNAblueprint/RNARedPrint.
tags: ["rnasketch", "rna-design", "inverse-folding", "vienna", "nupack", "hotknots"]
author: oxo-call-community
source_url: "https://github.com/ViennaRNA/RNAsketch"
---

## Concepts

- **Tool Overview**: RNAsketch (v1.5, ViennaRNA group) is a C++/Python library for designing RNA sequences that satisfy a target secondary structure, with pluggable backends that call the underlying inverse-folding engines: ViennaRNA's RNAinverse, NUPACK's design, Hotknots (for pseudoknots), and pKiss. It also serves as the "glue" between RNAblueprint (multi-target design) and the various design engines.
- **Core Function**: Takes a target secondary structure (dot-bracket or bp file) and a target length, then enumerates RNA sequences that fold into the target as the MFE structure. The default backend is ViennaRNA; pass `--engine nupack` or `--engine hotknots` for different energy models or to allow pseudoknots.
- **Algorithm**: Wraps the inverse-folding engine (RNAinverse's adaptive walk, NUPACK's random search, Hotknots' heuristic) in a uniform Python/C++ API. RNAsketch adds: sequence-level constraints (avoid motifs, GC content), automatic re-runs on failure, and a unified output format. The ViennaRNA backend is the most reliable; NUPACK is faster for long sequences; Hotknots is the only one that supports pseudoknots.
- **Input Format**: A target structure in dot-bracket notation (e.g., `(((...)))` for a hairpin) or a base-pair list. The target sequence length is auto-derived from the structure unless `--length` is passed. Optional flags: `--engine`, `--gc-min`, `--gc-max`, `--forbid-motif`, `--max-attempts`.
- **Output Format**: A list of candidate sequences (one per line) with the corresponding MFE structure and a stability score. The default is the top 10 candidates; the count is configurable via `--top-n`. JSON output is available via `--output-format json`.
- **Use Case**: Designing siRNA/miRNA hairpins for RNAi, creating ribozymes with a target structure, designing structural RNAs (aptamers, riboswitches) with forbidden-sequence constraints, and producing candidate sequences for downstream multi-target design with RNAblueprint.

## Pitfalls

- **CRITICAL — The default engine (ViennaRNA) does NOT support pseudoknots**: If the target structure contains pseudoknot notation (`[`, `]`, `{`, `}`, `a`, `b`, ...), RNAinverse will fail or silently produce a sequence that does not fold into the target. Pass `--engine hotknots` or `--engine pkiss` for pseudoknot-aware design.
- **CRITICAL — NUPACK must be installed separately for the nupack backend**: The `nupack` Python package is on PyPI but the binaries are not; on Linux you need a working NUPACK installation. Verify with `python -c "import nupack"` before passing `--engine nupack`.
- **No automatic re-design on failure**: If the engine fails to find a sequence within `--max-attempts` (default 100), the run exits with an error. For stubborn targets, raise `--max-attempts` to 1000 or try a different engine.
- **The "best" sequence is not always the first one**: The output is sorted by MFE distance to the target, but a sequence with a 1 kcal/mol penalty and a forbidden motif absent is preferable to a 0.5 kcal/mol penalty with the motif present. Always re-filter the output by your application-specific constraints.
- **Sequence constraints are applied AFTER design, not during**: The `--forbid-motif` flag rejects candidates that contain the motif, but does not guide the inverse-folding search. For strict constraint satisfaction, embed the constraints into the design (not yet supported in v1.5; available in the master branch).
- **Long target structures (> 500 nt) are slow**: The ViennaRNA inverse-folding algorithm is O(n²) per iteration and may need thousands of iterations for a 500-nt target. For very long RNAs (full mRNAs), restrict to functional domains (e.g., the aptamer or expression platform) rather than the full sequence.

## Examples

### Basic inverse-folding design
**Args:** `RNAsketch --target "(((...)))" --length 30 --engine vienna --top-n 10 -o candidates.fa`
**Explanation:** `--target` is the dot-bracket structure (a hairpin in this case), `--length 30` is the target sequence length, `--engine vienna` selects the ViennaRNA backend. Output `candidates.fa` contains 10 candidate sequences that fold into the target.

### Design with GC-content constraint
**Args:** `RNAsketch --target "(((...)))" --length 50 --gc-min 0.4 --gc-max 0.6 --engine vienna -o candidates.fa`
**Explanation:** `--gc-min 0.4 --gc-max 0.6` constrains the candidate sequences to 40–60% GC content. Useful when designing RNAs for expression in E. coli (prefers ~50% GC) or for PCR amplification (avoids extreme GC).

### Use the NUPACK backend
**Args:** `RNAsketch --target "(((...)))" --length 80 --engine nupack -o candidates.fa`
**Explanation:** `--engine nupack` switches to the NUPACK design backend, which is faster than ViennaRNA for sequences > 200 nt and uses a different energy model. Requires NUPACK installed separately.

### Design a pseudoknotted structure
**Args:** `RNAsketch --target "(((..[[..)))..]].." --length 40 --engine hotknots -o candidates.fa`
**Explanation:** `--target` contains the pseudoknot notation `[[...]]`; `--engine hotknots` (or `pkiss`) is required because ViennaRNA cannot design into pseudoknotted structures. Output sequences fold into the pseudoknot as MFE.

### Avoid a restriction site
**Args:** `RNAsketch --target "(((...)))" --length 50 --forbid-motif GGTCTC --engine vienna -o candidates.fa`
**Explanation:** `--forbid-motif GGTCTC` rejects any sequence containing a BsaI site; the final candidate list is re-checked. Critical when the designed RNA will be assembled via Golden Gate.

### Design for multiple targets (RNAblueprint glue)
**Args:** `RNAsketch --target targets.yaml --length 80 --engine vienna -o candidates.fa`
**Explanation:** `targets.yaml` is a multi-target file (one target per line) that invokes the RNAblueprint glue layer in RNAsketch. The output sequence is a single RNA that folds into each target as a (locally) optimal structure. See the ViennaRNA documentation for the YAML schema.

### JSON output with full metadata
**Args:** `RNAsketch --target "(((...)))" --length 50 --engine vienna --output-format json -o candidates.json`
**Explanation:** `--output-format json` writes a structured document with each candidate's sequence, MFE structure, MFE energy, and constraint-satisfaction status. Easier to parse for downstream filtering.
