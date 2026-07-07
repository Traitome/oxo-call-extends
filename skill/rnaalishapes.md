---
name: rnaalishapes
category: alignment
description: RNAalishapes predicts RNA secondary structures from multiple sequence alignments using shape abstraction.
tags: [rnaalishapes, alignment, rna-secondary-structure, shape-abstraction, msa]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/rnaalishapes"
---

## Concepts

- **Tool Overview**: RNAalishapes predicts RNA secondary structures with shape abstraction.
- **Core Function**: Structure prediction from aligned RNA sequences.
- **Algorithm**: Uses abstract shape-based dynamic programming to reduce folding space.
- **Input Format**: Accepts CLUSTALW, FASTA, or Stockholm multiple sequence alignments.
- **Output**: Produces abstract shape structures and consensus secondary structures.
- **Use Case**: Comparative RNA structure prediction for ncRNAs.

## Pitfalls

- **No Pseudoknots**: RNAalishapes does not model pseudoknots at all.
- **MSA Required**: Single-sequence input is not supported; must provide a multiple sequence alignment.
- **Sequence Length**: Computational complexity grows with alignment length; large RNAs (>1000 nt) may be slow.
- **Abstract Shapes**: Default shape abstraction may miss detailed structural variations.
- **Vienna RNA Package**: Requires Vienna RNA Package libraries (RNAlib) at build time.
- **Suboptimals**: By default, only optimal shape is reported; use `-s` for suboptimal shape enumeration.

## Examples

### Display help
**Args:** `RNAalishapes --help`
**Explanation:** Shows all available flags and abstract shape levels.

### Predict structure from MSA
**Args:** `RNAalishapes msa_alignment.fasta`
**Explanation:** Reads FASTA MSA; outputs abstract structure to stdout in dot-bracket notation.

### Specify shape abstraction level
**Args:** `RNAalishapes --shapeLevel 5 msa_alignment.fasta`
**Explanation:** `--shapeLevel 5` sets the shape abstraction granularity (1=most abstract, 5=most detailed).

### With suboptimal structures
**Args:** `RNAalishapes -s 10 msa_alignment.fasta`
**Explanation:** `-s 10` reports up to 10 suboptimal shape structures in the output.

### Save to file
**Args:** `RNAalishapes msa_alignment.fasta -o structure_out.txt`
**Explanation:** `-o` writes the predicted structure to a file instead of stdout.

### Specify energy parameters
**Args:** `RNAalishapes --temperature 37.0 msa_alignment.fasta`
**Explanation:** `--temperature 37.0` sets folding temperature in Celsius (default 37.0).

### With Vienna RNA compatibility
**Args:** `RNAalishapes --viennaOut msa_alignment.fasta`
**Explanation:** `--viennaOut` emits Vienna-format output with paired/unpaired positions for downstream tools.