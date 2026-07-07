---
name: tcoffee
category: alignment
description: T-Coffee - Multiple Sequence Alignment tool for proteins, DNA, and RNA sequences with consistency-based scoring.
tags: [tcoffee, multiple-sequence-alignment, msa, phylogenetics, dna-alignment, protein-alignment, rna-alignment]
author: oxo-call-community
source_url: "https://tcoffee.org/Projects/tcoffee/index.html"
---

## Concepts

- **Tool Overview**: T-Coffee (v13.46+) - A versatile multiple sequence alignment package using consistency-based scoring. Can align Protein, DNA, and RNA sequences and combine multiple alignment methods.
- **Core Function**: Uses progressive alignment with consistency scoring from pairwise alignments to produce high-quality MSAs. Supports combining outputs from Clustal, MAFFT, Probcons, Muscle into unified alignments via M-Coffee.
- **Modes**: Multiple modes - Default (balanced), Fast (quickaln), Accurate (high accuracy for proteins), Regressive (large datasets), R-Coffee (RNA with secondary structure), Expresso (with structure), M-Coffee (meta-aligner).
- **Installation**: `conda install -c bioconda t-coffee` or download from GitHub `https://github.com/cbcrg/tcoffee`
- **Output Formats**: Aln (ClustalW), FASTA, PIR, MSF, and HTML with color-coded reliability scores (TCS index).
- **Key Feature**: The TCS (Transitive Consistency Score) colors the alignment - red bits are reliable, green/blue are unreliable.

## Pitfalls

- **Memory Limit**: Default mode limited to ~50 sequences; above this switches to heuristic DPA (Double Progressive Alignment) mode.
- **Slow for Large Datasets**: Default accurate mode is computationally intensive. Use `-mode quickaln` or `-reg` for large datasets.
- **Format Requirements**: Input sequences must be in FASTA, Swiss-Prot, or PIR format. Mixed formats not supported.
- **Dependencies**: Some modes require third-party aligners (MAFFT, Muscle, Probcons) for M-Coffee or Expresso.
- **HTML Output**: The color-coded HTML output requires JavaScript-enabled browsers for proper display.
- **Version Compatibility**: Some older parameter files and flags may be deprecated in newer versions.

## Examples

### Basic protein alignment
**Args:** `t_coffee sequences.fasta`
**Explanation:** Basic protein sequence alignment using default mode. Generates .aln, .dnd (guide tree), and .html output files.

### Fast alignment
**Args:** `t_coffee sequences.fasta -mode quickaln`
**Explanation:** Quick alignment mode for rapid results with moderate accuracy. Suitable for large datasets.

### High accuracy protein alignment
**Args:** `t_coffee sequences.fasta -mode accurate`
**Explanation:** Most accurate mode for protein sequences using exhaustive alignment computation.

### Large dataset with regressive algorithm
**Args:** `t_coffee -seq large_dataset.fasta -reg`
**Explanation:** Use regressive algorithm optimized for very large sequence datasets. Suitable for hundreds to thousands of sequences.

### RNA alignment with secondary structure
**Args:** `t_coffee rna_sequences.fasta -mode rcoffee`
**Explanation:** R-Coffee mode incorporates RNA secondary structure information for more accurate alignments.

### Combine multiple aligners (M-Coffee)
**Args:** `t_coffee sequences.fasta -mode mcoffee`
**Explanation:** M-Coffee combines ClustalW, MAFFT, Muscle, and Probcons into a single consistency-based alignment.

### Structure-based alignment (Expresso)
**Args:** `t_coffee sequences.fasta -mode expresso`
**Explanation:** Expresso uses structural information to guide alignment, fetching PDB structures automatically.

### Convert alignment format
**Args:** `t_coffee -other_pg seq_reformat -in alignment.aln -output fasta_aln`
**Explanation:** Reformat alignment between formats using T-Coffee's seq_reformat utility.

### Evaluate alignment quality
**Args:** `t_coffee -other_pg tcs -seq sequences.fasta -aln alignment.aln`
**Explanation:** Evaluate alignment reliability using the TCS (Transitive Consistency Score) method.
