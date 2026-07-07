---
name: hr2
category: mass_spectrometry
description: HR2 is a program to calculate elemental compositions for a given mass
tags: [hr2, mass_spectrometry, elemental_composition, mass_analysis]
author: oxo-call-community
source_url: "http://fiehnlab.ucdavis.edu"
---

## Concepts

- **Elemental Composition Calculation**: Computes possible elemental compositions from a given mass
- **High-Resolution Mass Spectrometry**: Designed for accurate mass measurements from HRMS instruments
- **Isotope Pattern Matching**: Considers isotope distributions for verification
- **Constraints-Based Search**: Allows specifying element limits and valence rules
- **Formula Generation**: Generates all possible molecular formulas within specified constraints
- **Mass Accuracy**: Handles high precision mass measurements (ppm level)

## Pitfalls

- **Element Constraints**: Incorrect element limits can exclude valid compositions
- **Mass Accuracy**: Poor mass accuracy leads to incorrect formula assignments
- **Charge State**: Must correctly specify charge state for accurate results
- **Isotope Interference**: Overlapping isotope patterns can complicate interpretation
- **Complex Molecules**: Very large molecules may exceed computational limits
- **Time Constraints**: Exhaustive searches can be computationally intensive

## Examples

### Basic composition calculation
**Args:** `hr2 342.12345`
**Explanation:** Calculates possible elemental compositions for mass 342.12345.

### With element constraints
**Args:** `hr2 180.06339 -C 6-12 -H 8-20 -O 4-10`
**Explanation:** Searches for compositions with specified C, H, O ranges.

### Monoisotopic mass search
**Args:** `hr2 180.06339 --mono`
**Explanation:** Searches using monoisotopic mass only.

### With isotope pattern verification
**Args:** `hr2 342.12345 --isotope-match observed_pattern.txt`
**Explanation:** Matches calculated compositions against observed isotope pattern.

### Output to file
**Args:** `hr2 284.0946 -o compositions.txt`
**Explanation:** Writes results to output file for further analysis.