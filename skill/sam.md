---
name: sam
category: alignment
description: Sequence Alignment and Modeling System (SAM)
tags: ["sam", "alignment", "protein structure", "sequence analysis"]
author: oxo-call-community
source_url: "https://compbio.soe.ucsc.edu/sam2src/"
---

## Concepts

- **Tool Overview**: SAM (Sequence Alignment and Modeling System, v3.5) is a suite of tools for sequence alignment, protein structure prediction, and sequence analysis.
- **Core Function**: Provides tools for sequence alignment, profile construction, homology detection, and protein structure prediction.
- **Algorithm**: Implements hidden Markov models (HMMs) for profile-based sequence alignment and homology detection.
- **Input Format**: FASTA sequences, profile HMMs, alignment files.
- **Output Format**: Sequence alignments, profile HMMs, homology search results, structure predictions.
- **Use Case**: Protein sequence analysis, homology detection, structure prediction, evolutionary studies.

## Pitfalls

- **Memory requirements**: Large sequence databases require significant memory.
- **Database formatting**: Requires properly formatted sequence databases.
- **Parameter tuning**: HMM parameters may require adjustment for optimal results.
- **Computational time**: Comprehensive searches can be time-consuming.
- **Format compatibility**: Some alignment formats may not be supported.
- **False positives**: May identify spurious homologies in low-complexity regions.

## Examples

### Build profile HMM
**Args:** `sam build -o profile.hmm -f sequences.fasta`
**Explanation:** `-o` output HMM; `-f` input sequences.

### Search database
**Args:** `sam search -i profile.hmm -d database.fasta -o results.txt`
**Explanation:** `-i` input HMM; `-d` database; `-o` results.

### Align sequences
**Args:** `sam align -i sequences.fasta -o alignment.txt`
**Explanation:** Aligns multiple sequences using profile HMM.

### Profile comparison
**Args:** `sam compare -i1 profile1.hmm -i2 profile2.hmm -o comparison.txt`
**Explanation:** Compares two profile HMMs.

### Convert format
**Args:** `sam convert -i alignment.txt -o alignment.sto --format stockholm`
**Explanation:** Converts alignment to Stockholm format.

### Extract domain
**Args:** `sam extract -i sequence.fasta -o domain.fasta -r 100-200`
**Explanation:** Extracts subsequence from position 100-200.

### Merge profiles
**Args:** `sam merge -i profiles.txt -o merged.hmm`
**Explanation:** Merges multiple profiles into one.