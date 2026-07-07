---
name: jali
category: alignment
description: Alignment method for comparing a protein sequence to a protein family using a generalized Smith-Waterman algorithm.
tags: [jali, alignment, protein, Smith-Waterman, family]
author: oxo-call-community
source_url: "http://bibiserv.cebitec.uni-bielefeld.de/jali"
---

## Concepts

- **Tool Overview**: jali (v1.3) - A sensitive protein alignment tool that compares a query sequence against a protein family represented by a multiple sequence alignment.
- **Generalized Smith-Waterman**: Extends the classic Smith-Waterman algorithm for profile-profile alignment.
- **Profile Alignment**: Aligns query sequences to position-specific scoring matrices derived from multiple sequence alignments.
- **Gap Penalty Optimization**: Implements position-specific gap penalties for improved alignment accuracy.
- **Sensitive Search**: Designed for detecting remote homologs with low sequence similarity.
- **Database Search**: Can perform sensitive searches against protein databases using profile-based scoring.

## Pitfalls

- **Computational Complexity**: Profile-profile alignment is computationally intensive.
- **Memory Usage**: Large multiple sequence alignments require significant memory.
- **Alignment Quality**: Results depend on the quality of the input multiple sequence alignment.
- **Parameter Sensitivity**: Gap penalties and scoring parameters significantly affect results.
- **False Positives**: High sensitivity can lead to increased false positive matches.
- **Database Size**: Search time increases linearly with database size.

## Examples

### Align query to profile
**Args:** `jali -q query.fasta -p profile.ali -o alignment.txt`
**Explanation:** Aligns query sequence to a profile from multiple sequence alignment.

### Database search
**Args:** `jali -q query.fasta -d database.fasta -o results.txt`
**Explanation:** Searches query against protein database using profile-based scoring.

### Set gap penalties
**Args:** `jali -q query.fasta -p profile.ali -o out.txt --gap-open 10 --gap-extend 2`
**Explanation:** Sets custom gap opening (10) and extension (2) penalties.

### Output alignment format
**Args:** `jali -q query.fasta -p profile.ali -o out.txt --format clustal`
**Explanation:** Outputs alignment in Clustal format.

### Include secondary structure
**Args:** `jali -q query.fasta -p profile.ali -o out.txt --ss query.ss`
**Explanation:** Incorporates secondary structure information into alignment scoring.

### Threshold filtering
**Args:** `jali -q query.fasta -d database.fasta -o results.txt -e 1e-10`
**Explanation:** Filters results by E-value threshold of 1e-10.