---
name: hmmer
category: alignment
description: Biosequence analysis using profile hidden Markov models. HMMER3 provides tools for searching sequence databases, building profile HMMs, and performing sensitive homology detection.
tags: [hmmer, profile-hmm, sequence-analysis, homology, Pfam, jackhmmer, hmmsearch, hmmscan]
author: oxo-call-community
source_url: "http://hmmer.org/documentation.html"
---

## Concepts

- **Tool Overview**: HMMER (v3.4) is a powerful bioinformatics software package for sequence analysis using profile hidden Markov models (profile HMMs). It is the core utility behind protein family databases like Pfam and InterPro, enabling sensitive detection of remote homologs.

- **Profile HMM Construction**: The `hmmbuild` program constructs probabilistic profile HMMs from multiple sequence alignments. These models capture position-specific information about residue conservation, insertion, and deletion probabilities across a sequence family.

- **Search Algorithms**: HMMER3 introduced significant performance improvements through multi-stage filtering (MSV, Viterbi, Forward) and SIMD vectorization, making profile HMM searches nearly as fast as BLAST while maintaining superior sensitivity for remote homology detection.

- **Key Programs**: 
  - `phmmer`: Single-sequence searches against protein databases (BLASTP-like)
  - `jackhmmer`: Iterative homology refinement (PSIBLAST-like)
  - `hmmsearch`: Profile HMM against sequence database
  - `hmmscan`: Sequence against profile HMM database (e.g., Pfam)
  - `hmmalign`: Align sequences to a profile HMM
  - `hmmpress`: Prepare HMM database for efficient scanning

- **Statistical Significance**: HMMER computes E-values based on profile-specific null models, providing rigorous statistical assessment of homology matches. Bit scores are normalized for comparison across different profiles.

- **Database Integration**: HMMER is integrated with major protein family databases. Pfam uses HMMER profiles to annotate protein domains, and tools like InterPro incorporate HMMER searches for comprehensive functional annotation.

## Pitfalls

- **Multiple Sequence Alignment Quality**: Poor alignments produce poor profiles. Ensure input alignments are high-quality, properly trimmed, and free of misaligned regions before building profiles.

- **E-value Threshold Selection**: Default E-value thresholds may miss true homologs or produce false positives depending on the database size and profile specificity. Adjust thresholds based on your analysis goals.

- **Memory Usage**: Building profiles from large alignments or searching massive databases can be memory-intensive. Monitor memory usage and consider splitting large datasets.

- **Version Compatibility**: HMMER3 format is not directly compatible with HMMER2. Use `hmmconvert` to convert between formats when working with legacy profiles.

- **Database Indexing**: For efficient `hmmscan` searches, databases must be indexed with `hmmpress`. Failure to do so results in extremely slow searches.

- **Domain Boundary Prediction**: While HMMER identifies domain hits, precise boundary prediction may require additional refinement using tools like `hmmalign` or structural information.

## Examples

### Build a profile HMM from alignment
**Args:** `hmmbuild globins.hmm globins.sto`
**Explanation:** Constructs a profile HMM from a multiple sequence alignment in Stockholm format. The resulting HMM captures the characteristic patterns of the globin family.

### Search sequence database with profile HMM
**Args:** `hmmsearch globins.hmm uniprot_sprot.fasta > globins_results.out`
**Explanation:** Searches the UniProt Swiss-Prot database using the globins profile HMM. Outputs BLAST-like results with E-values and alignment information.

### Search profile database with sequence
**Args:** `hmmscan Pfam-A.hmm query_sequence.fasta`
**Explanation:** Scans a query sequence against the Pfam-A profile database to identify potential domain matches. Requires Pfam database to be pre-processed with `hmmpress`.

### Iterative homology search
**Args:** `jackhmmer HBB_HUMAN.fasta uniprot_sprot.fasta -o jackhmmer_results.out`
**Explanation:** Performs iterative PSIBLAST-like search starting with human beta-globin. Each iteration builds a profile from hits and searches again, progressively finding more distant homologs.

### Press an HMM database for efficient scanning
**Args:** `hmmpress Pfam-A.hmm`
**Explanation:** Creates binary index files for the Pfam-A database, enabling fast `hmmscan` searches. Produces .h3f, .h3i, .h3m, and .h3p index files.

### Align sequences to a profile HMM
**Args:** `hmmalign globins.hmm unknown_sequences.fasta > aligned_results.sto`
**Explanation:** Aligns a set of sequences to the globins profile HMM, producing a multiple sequence alignment in Stockholm format with consistent positioning.

### Single sequence search (phmmer)
**Args:** `phmmer query.fasta target_database.fasta -o phmmer_results.out`
**Explanation:** Performs BLASTP-like search using profile HMM technology. More sensitive than BLAST for detecting remote homologs while maintaining comparable speed.