---
name: crisper_recognition_tool
category: genome-editing
description: CRISPR Recognition Tool (CRT) for automatic detection of CRISPR arrays in genomic sequences
tags: [crisper_recognition_tool, CRT, CRISPR, array-detection, repeats, spacers, prokaryote, bacterial-immunity]
author: oxo-call-community
source_url: "http://www.room220.com/crt/"
---

## Concepts

- **Tool Overview**: crisper_recognition_tool (CRT) v1.2 - A Java-based tool for automatic detection of CRISPR arrays in genomic sequences.
- **Core Function**: Searches genomic sequences to identify Clustered Regularly Interspersed Short Palindromic Repeats (CRISPR) arrays consisting of direct repeats separated by spacer sequences. Available as both GUI and command-line interface.
- **Algorithm**: Uses pattern recognition to identify repeated sequences separated by non-repeated regions at consistent length intervals. Searches for palindromic repeat sequences with characteristic spacing patterns.
- **Input**: Genomic sequence file in FASTA format.
- **Output**: CRISPR array locations, repeat sequences, spacer sequences, array orientation.
- **Application**: Prokaryotic genome annotation, CRISPRCas system identification, phage resistance analysis, horizontal gene transfer studies.
- **Installation**: Download CRT1.2-CLI.jar.zip from room220.com, unzip and run with Java.

## Pitfalls

- **Java Required**: Requires Java runtime environment (JRE) to be installed.
- **Old Software**: Last updated in 2008 - may not detect newer CRISPR types or unconventional array structures.
- **Parameter Sensitivity**: Results can vary with search window size and repeat/spacer length parameters.
- **Minimum Repeat Requirement**: Requires at least 3 repeats by default - may miss smaller arrays.
- **Sequence Quality**: Ns in sequences and edge effects can cause truncated repeat detection issues.
- **Limited Output Options**: Basic output format may need post-processing for downstream analysis.

## Examples

### Basic CRISPR detection
**Args:** `java -cp CRT1.2-CLI.jar crt input.fasta output.txt`
**Explanation:** Run CRT on input FASTA file and write results to output file.

### Adjust minimum number of repeats
**Args:** `java -cp CRT1.2-CLI.jar crt -minNR 2 input.fasta output.txt`
**Explanation:** Set minimum number of repeats to 2 instead of default 3 for detecting smaller arrays.

### Set repeat length range
**Args:** `java -cp CRT1.2-CLI.jar crt -minRL 20 -maxRL 50 input.fasta output.txt`
**Explanation:** Define the allowed repeat length range (20-50 bp).

### Set spacer length range
**Args:** `java -cp CRT1.2-CLI.jar crt -minSL 15 -maxSL 60 input.fasta output.txt`
**Explanation:** Define the allowed spacer length range (15-60 bp).

### Adjust search window size
**Args:** `java -cp CRT1.2-CLI.jar crt -searchW 7 input.fasta output.txt`
**Explanation:** Set search window size to 7 (valid range 6-9). Smaller windows increase sensitivity but may find more false positives.

### Display help
**Args:** `java -cp CRT1.2-CLI.jar crt -h`
**Explanation:** Display all available command-line options and their default values.

### Process multiple sequences
**Args:** `java -cp CRT1.2-CLI.jar crt multi_genomes.fasta results.txt`
**Explanation:** Process a multi-sequence FASTA file containing multiple genomic sequences.

### Use with piped input
**Args:** `cat input.fasta | java -cp CRT1.2-CLI.jar crt /dev/stdin output.txt`
**Explanation:** Read input from stdin instead of file path (Unix-like systems).

### Combined parameter usage
**Args:** `java -cp CRT1.2-CLI.jar crt -minNR 2 -minRL 19 -maxRL 50 -minSL 19 -maxSL 60 genome.fasta crispr_results.txt`
**Explanation:** Use multiple parameters together for customized detection with typical CRISPR repeat/spacer sizes.

### GUI mode (requires display)
**Args:** `java -jar CRT1.2-CLI.jar`
**Explanation:** Launch the graphical user interface instead of command-line mode if X11/display is available.
