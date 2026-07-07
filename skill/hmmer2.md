---
name: hmmer2
category: alignment
description: Biosequence analysis using profile hidden Markov models (legacy HMMER2 version).
tags: [hmmer2, profile-hmm, sequence-analysis, homology, legacy]
author: oxo-call-community
source_url: "http://hmmer.org"
---

## Concepts

- **Tool Overview**: HMMER2 (v2.3.2) is the legacy version of the HMMER software package for sequence analysis using profile hidden Markov models. While HMMER3 has superseded it, HMMER2 is still used in some legacy applications and pipelines.

- **Profile HMM Construction**: The `hmmbuild` program builds profile HMMs from multiple sequence alignments in various formats (Stockholm, FASTA, Clustal). Profiles capture position-specific substitution, insertion, and deletion probabilities.

- **Search Functionality**: HMMER2 provides `hmmsearch` for searching profile HMMs against sequence databases and `hmmscan` for searching sequences against profile HMM databases like Pfam.

- **Scoring System**: Uses log-odds scores based on position-specific scoring matrices derived from the input alignment. E-values are computed using a null model for statistical significance assessment.

- **Sequence Alignment**: The `hmmalign` program aligns sequences to a profile HMM, producing a multiple sequence alignment consistent with the profile's expectations.

- **Legacy Compatibility**: HMMER2 format profiles are not directly compatible with HMMER3. Use `hmmconvert` from HMMER3 to convert between formats when needed.

## Pitfalls

- **Performance Limitations**: HMMER2 is significantly slower than HMMER3 for large database searches due to lack of multi-stage filtering and SIMD optimizations.

- **Format Incompatibility**: HMMER2 profile format differs from HMMER3. Legacy profiles must be converted before use with HMMER3 tools.

- **Reduced Sensitivity**: HMMER2 lacks some of the advanced algorithms in HMMER3 that improve remote homology detection.

- **No Single-Sequence Tools**: HMMER2 does not include `phmmer` or `jackhmmer` - these were introduced in HMMER3.

- **Memory Efficiency**: HMMER2 is less memory-efficient than HMMER3 for large alignments and databases.

- **Limited Support**: Official support for HMMER2 is limited; users are encouraged to upgrade to HMMER3 for most applications.

## Examples

### Build a profile HMM from alignment
**Args:** `hmmbuild globins.hmm globins.aln`
**Explanation:** Constructs a profile HMM from a multiple sequence alignment. Supports various alignment formats including Stockholm, Clustal, and MSF.

### Search sequence database with profile HMM
**Args:** `hmmsearch globins.hmm swissprot.fasta`
**Explanation:** Searches a sequence database using the profile HMM. Outputs ranked hits with scores and alignment information.

### Search profile database with sequence
**Args:** `hmmscan Pfam.hmm query.fasta`
**Explanation:** Scans a query sequence against a profile HMM database like Pfam to identify domain matches.

### Align sequences to profile HMM
**Args:** `hmmalign globins.hmm new_sequences.fasta`
**Explanation:** Aligns new sequences to an existing profile HMM, producing a multiple sequence alignment.

### Show profile statistics
**Args:** `hmmstat globins.hmm`
**Explanation:** Displays summary statistics for the profile HMM including length, number of states, and consensus sequence.

### Convert profile format
**Args:** `hmmconvert -2to3 old_profile.hmm new_profile.hmm`
**Explanation:** Converts HMMER2 profile format to HMMER3 format for use with newer tools.

### Filter low-scoring hits
**Args:** `hmmsearch -E 0.001 globins.hmm database.fasta > filtered_results.out`
**Explanation:** Searches with an E-value cutoff of 0.001, filtering out less significant matches.