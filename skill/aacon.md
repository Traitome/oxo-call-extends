---
name: aacon
category: utility
description: AACon: A Fast Amino Acid Conservation Calculation Service
tags: [aacon, utility, protein, conservation, alignment]
author: oxo-call-community
source_url: "https://github.com/bartongroup/aacon"
---

## Concepts

- **Tool Overview**: AACon implements 17 different conservation scores reviewed by Valdar plus the SMERFS algorithm for predicting protein functional sites. Version 1.1.
- **Core Function**: Calculates amino acid conservation scores from multiple sequence alignments to identify functionally important residues.
- **Input/Output**: Input is a multiple sequence alignment; output is conservation scores for each column/position.
- **Installation**: Install via bioconda: `conda install -c bioconda aacon`
- **Platform Support**: Platform-independent (noarch, Java-based)
- **Parallel Processing**: Exploits parallelism for demanding methods and allows multiple methods to run simultaneously with near-linear speedup.
- **Performance**: Calculates conservation by all 18 methods for an alignment of 500 sequences × 350 residues in less than a second on a single CPU.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Format**: Requires properly formatted multiple sequence alignment. Ensure alignment quality affects conservation calculation.
- **Java Dependency**: Requires Java runtime environment (JRE) to execute.
- **Memory Usage**: Large alignments may require increased Java heap space via `-Xmx` flag.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available conservation methods, options, and usage information.

### Run basic conservation calculation
**Args:** `-i alignment.fasta -o conservation_scores.txt`
**Explanation:** Calculates conservation scores from the input alignment file and writes results to the output file.

### Run with specific conservation method
**Args:** `-i alignment.fasta -m shannon_entropy -o scores.txt`
**Explanation:** Uses the Shannon entropy method for conservation calculation. Different methods may give different results for the same alignment.

### Run all conservation methods
**Args:** `-i alignment.fasta --all-methods -o all_scores.txt`
**Explanation:** Calculates conservation using all 18 available methods (17 Valdar-reviewed + SMERFS). Comprehensive analysis for identifying conserved residues.

### Run SMERFS for functional site prediction
**Args:** `-i alignment.fasta --smerfs -o functional_sites.txt`
**Explanation:** Uses the SMERFS algorithm specifically designed for predicting protein functional sites based on conservation patterns.
