---
name: aacon
category: utility
description: "AACon: A Fast Amino Acid Conservation Calculation Service implementing 17 conservation scores and SMERFS algorithm for predicting protein functional sites."
tags: [aacon, utility, protein, conservation, alignment, amino-acid, bioinformatics]
author: oxo-call-community
source_url: "https://www.compbio.dundee.ac.uk/aacon/"
---
## Concepts

- **Tool Overview**: AACon implements 17 different conservation scores reviewed by Valdar plus the SMERFS algorithm for predicting protein functional sites. Version 1.1.
- **Core Function**: Calculates amino acid conservation scores from multiple sequence alignments to identify functionally important residues.
- **Input/Output**: Input is a multiple sequence alignment (FASTA or Clustal format); output is conservation scores for each column/position.
- **Installation**: Install via bioconda: `conda install -c bioconda aacon`
- **Platform Support**: Platform-independent (noarch, Java-based with shell wrapper)
- **Parallel Processing**: Exploits parallelism for demanding methods and allows multiple methods to run simultaneously with near-linear speedup.
- **Performance**: Calculates conservation by all 18 methods for an alignment of 500 sequences × 350 residues in less than a second on a single CPU.
- **Methods**: Supports 17 Valdar methods (KABAT, SHENKIN, JONES, etc.) plus SMERFS algorithm for functional site prediction.

## Pitfalls

- **Java Dependency**: Requires Java runtime environment (JRE) to execute. The shell wrapper automatically uses JAVA_HOME or system java.
- **Memory Usage**: Large alignments may require increased Java heap space. Set JAVA_OPTS environment variable if needed.
- **Input Format**: Requires properly formatted multiple sequence alignment. Accepts FASTA or Clustal formats.
- **Gap Characters**: Default gap characters are -, _, x, *, ., and space. Custom gaps can be specified with `-g` flag.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available conservation methods, options, and usage information.

### Run basic conservation calculation
**Args:** `-i=alignment.fasta -o=conservation_scores.txt`
**Explanation:** Calculates conservation scores using default method (Shenkin) from the input alignment and writes results to the output file.

### Run with specific conservation method
**Args:** `-i=alignment.fasta -m=KABAT -o=scores.txt`
**Explanation:** Uses the KABAT method for conservation calculation. Other available methods include SHENKIN, JONES, GERSTEIN, etc.

### Run all conservation methods
**Args:** `-i=alignment.fasta --all-methods -o=all_scores.txt`
**Explanation:** Calculates conservation using all 18 available methods (17 Valdar-reviewed + SMERFS). Provides comprehensive analysis for identifying conserved residues.

### Run SMERFS for functional site prediction
**Args:** `-i=alignment.fasta --smerfs -o=functional_sites.txt`
**Explanation:** Uses the SMERFS algorithm specifically designed for predicting protein functional sites based on conservation patterns.

### Run SMERFS with custom window parameters
**Args:** `-i=alignment.fasta --smerfs --smerfs-window=11 --smerfs-cutoff=0.2 -o=smerfs_output.txt`
**Explanation:** Runs SMERFS with a custom window width of 11 and gap percentage cutoff of 0.2. The window width must be an odd integer.

### Specify custom gap character
**Args:** `-i=alignment.fasta -g=-,_,x -o=scores.txt`
**Explanation:** Sets custom gap characters to -, _, and x. By default, AACon recognizes -, _, x, *, ., and space as gap characters.

### Run with Clustal format input
**Args:** `-i=alignment.clustal -o=scores.txt`
**Explanation:** Reads a Clustal formatted alignment file and calculates conservation scores. AACon automatically detects the input format.