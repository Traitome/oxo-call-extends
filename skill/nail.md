---
name: nail
category: alignment
description: NAIL - Profile Hidden Markov Model biological sequence alignment tool
tags: [nail, alignment, phmm, hmm, sequence, profile-alignment]
author: oxo-call-community
source_url: "https://github.com/TravisWheelerLab/nail"
---

## Concepts

- **Tool Overview**: NAIL v0.5.0 (Nested Alignment through Iterative Learning) is a profile Hidden Markov Model (pHMM) alignment tool for sensitive biological sequence homology detection and alignment.
- **Core Function**: Aligns query sequences against profile HMMs to find remote homologs with higher sensitivity than simple sequence comparison methods. Useful for finding divergent but functionally related sequences.
- **Algorithm**: Uses iterative profile HMM construction and stochastic context-free grammars for improved alignment accuracy. Incorporates structural predictions for enhanced sensitivity.
- **Input Format**: Accepts query sequences in FASTA format and profile HMM files in standard HMMER format (or can build profiles from input sequences).
- **Output**: Produces alignments in multiple formats (Stockholm, FASTA-aln, A2M) with per-residue scores and alignment confidence estimates.
- **Use Case**: Detecting remote homology in protein families, improving alignments for highly divergent sequences, and building custom profile databases for specialized gene families.

## Pitfalls

- **Profile Quality**: Alignment accuracy depends heavily on the quality of the input profile HMM. Poorly constructed profiles produce unreliable alignments.
- **Computational Time**: Profile-based alignment is slower than direct BLAST searches. For very large queries, consider pre-filtering.
- **Sequence Weighting**: Profile construction uses sequence weighting algorithms. Skewed sequence sampling affects profile quality.
- **Insertion/Deletion Modeling**: Overly aggressive indel modeling may produce unrealistic alignments in highly divergent regions.
- **E-value Calibration**: E-value calculations assume specific sequence distributions. Unusual composition may affect reliability.
- **Format Compatibility**: Ensure HMM profiles are in HMMER3 format for full compatibility.

## Examples

### Align sequences to profile
**Args:** `-i sequences.fasta -p profile.hmm -o alignments.sthlm`
**Explanation:** Standard alignment workflow. Aligns query sequences against the provided profile HMM.

### Build profile from sequences
**Args:** `-i input.fasta -o new_profile.hmm --build`
**Explanation:** Builds a new profile HMM from input sequences before alignment.

### Specify alignment format
**Args:** `-i queries.fa -p ref.hmm -o results.fa -F fasta`
**Explanation:** Outputs alignments in FASTA alignment format instead of default Stockholm.

### Adjust E-value threshold
**Args:** `-i reads.fasta -p profile.hmm -o hits.txt -E 0.001`
**Explanation:** Sets E-value threshold for reporting alignments. Lower values increase stringency.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.
