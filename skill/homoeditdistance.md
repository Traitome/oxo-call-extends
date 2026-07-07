---
name: homoeditdistance
category: formatting
description: HomoEditDistance implements the homo-edit distance algorithm for sequence comparison using homo-insertions and homo-deletions.
tags: [homoeditdistance, sequence-alignment, edit-distance]
author: oxo-call-community
source_url: "https://github.com/AlBi-HHU/homo-edit-distance"
---

## Concepts

- **Homo-Edit Distance**: Measures the minimum number of homo-insertions (inserting a block of identical characters) or homo-deletions (deleting such a block) needed to convert one string to another.
- **Block Operations**: Operates on blocks of identical characters rather than individual characters, making it particularly suitable for sequences with repeated elements.
- **Efficient Algorithm**: Implements an optimized dynamic programming approach for computing homo-edit distance.
- **Backtrace Support**: Provides backtrace functionality to reconstruct the optimal sequence of operations.
- **Multiple Optimal Solutions**: Can enumerate all optimal transformation sequences when multiple solutions exist.
- **Bioinformatics Applications**: Particularly useful for analyzing sequences with homopolymer runs, such as DNA sequences with repeat expansions.

## Pitfalls

- **String Length Limitations**: Performance decreases with very long strings; consider sequence segmentation for large inputs.
- **Memory Usage**: Dynamic programming matrix requires O(n²) memory for strings of length n.
- **Alphabet Assumption**: Designed for discrete character sets; continuous or real-valued sequences require preprocessing.
- **Backtrace Complexity**: Enumerating all optimal solutions can be computationally expensive for complex transformations.
- **Edge Cases**: Empty strings and single-character strings require special handling.
- **Algorithm Specificity**: Homo-edit distance has different semantics than traditional edit distances; ensure appropriate use case.

## Examples

### Compute homo-edit distance between two strings
**Args:** `hed -s "TCAGACT" -t "TAGGCTT"`
**Explanation:** Calculates the homo-edit distance between two DNA sequences, showing the minimum number of block operations needed.

### Show all optimal transformations
**Args:** `hed -s "AAAA" -t "AA" -a -b`
**Explanation:** Displays all optimal transformation sequences with detailed backtrace information.

### Python API usage
**Args:** `python -c "from homoeditdistance import homoEditDistance; result = homoEditDistance('ATTTG', 'ATG', 0); print(result['hed'])"`
**Explanation:** Integrates homo-edit distance calculation into Python scripts for custom sequence analysis.

### Analyze homopolymer variations
**Args:** `hed -s "CAGGGGCT" -t "CAGGGCT"`
**Explanation:** Compares sequences with varying homopolymer lengths, showing how single block operations handle repeat length variations.

### Empty string handling
**Args:** `hed -s "" -t "AAAA"`
**Explanation:** Computes distance from empty string to a string of repeated characters, demonstrating homo-insertion operations.

### Complex sequence transformation
**Args:** `hed -s "GTTCCAA" -t "GTCCAAA" -a -b`
**Explanation:** Analyzes complex sequence transformation with multiple optimal paths, showing all equivalent solutions.