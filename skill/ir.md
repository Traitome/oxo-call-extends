---
name: ir
category: sequence-analysis
description: Program for Calculating the Repetitiveness of DNA Sequences
tags: [ir, sequence-analysis, repeats, DNA]
author: oxo-call-community
source_url: "http://guanine.evolbio.mpg.de/cgi-bin/ir/ir.cgi.pl"
---

## Concepts

- **Tool Overview**: ir (v2.8.0) - A bioinformatics tool for analyzing DNA sequence repetitiveness and detecting repetitive elements
- **Core Function**: Identifies and quantifies repetitive DNA sequences including tandem repeats, inverted repeats, and other repetitive patterns
- **Algorithm**: Uses dynamic programming and alignment scoring to detect repeats with configurable match/mismatch/indel parameters
- **Input/Output**: Accepts FASTA format sequences; generates structured output with repeat locations and characteristics
- **Scoring Parameters**: Configurable alignment weights for match (+2), mismatch (-3 to -7), and indel penalties
- **Statistical Analysis**: Provides probabilistic scoring based on match probability (PM) and indel probability (PI)

## Pitfalls

- **Parameter Sensitivity**: Results depend heavily on match/mismatch/delta parameters; defaults may not work for all sequences
- **Memory Requirements**: Analyzing large sequences with high MaxLength settings can consume significant memory
- **Output Complexity**: Multiple output files generated (HTML, data files); requires careful interpretation
- **Lowercase Handling**: By default, lowercase letters are ignored during detection; use `-l` flag to include them
- **Performance**: Higher sensitivity settings (lower mismatch penalties) significantly increase runtime
- **Redundancy Filtering**: Default redundancy filtering may remove biologically relevant repeats

## Examples

### Basic repeat detection
**Args:** `ir input.fasta 2 3 5 80 10 40 100000 500000`
**Explanation:** Detects repeats using match=2, mismatch=3, indel=5, PM=80, PI=10, min score=40, max stem=100K, max loop=500K.

### Generate data file output
**Args:** `ir genome.fasta 2 7 7 80 10 50 200000 1000000 -d`
**Explanation:** Runs analysis with standard parameters and generates a machine-readable data file for further processing.

### Include flanking sequences
**Args:** `ir contigs.fasta 2 5 7 80 10 40 50000 200000 -f`
**Explanation:** Extracts and reports sequences flanking detected repeats for downstream analysis.

### Suppress HTML output
**Args:** `ir sequence.fasta 2 3 5 80 10 30 100000 500000 -h`
**Explanation:** Disables HTML report generation, useful for batch processing pipelines.

### Enable lookahead optimization
**Args:** `ir large_genome.fasta 2 5 7 80 10 50 500000 1000000 -la`
**Explanation:** Uses lookahead test for faster analysis on large sequences with acceptable accuracy trade-off.

### Mirror repeats detection
**Args:** `ir palindrome_test.fasta 2 5 7 80 10 40 100000 500000 -mr`
**Explanation:** Specifically targets mirror repeat structures with inverted orientation patterns.