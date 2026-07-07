---
name: cassiopee
category: sequence-analysis
description: Scan genomic sequences for subsequence patterns with Hamming distance and indel support
tags: [cassiopee, sequence-search, pattern-matching, hamming-distance, motif-search]
author: oxo-call-community
source_url: "https://github.com/osallou/cassiopee-c"
---

## Concepts

- **Tool Overview**: Cassiopee searches genomic sequences for subsequence patterns with support for substitutions and indels.
- **Core Function**: Scans DNA/RNA/protein sequences for specific patterns using Hamming distance and gap penalties.
- **Algorithm**: Implements fast pattern matching with configurable mismatch and indel tolerance.
- **Input**: FASTA sequence file and pattern file.
- **Output**: Matching positions with scores and annotations.
- **Application**: Motif discovery, primer/probe design, and sequence pattern analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cassiopee`

## Pitfalls

- **Pattern File**: Requires properly formatted pattern file.
- **Sequence Type**: Supports DNA, RNA, and protein sequences.
- **Performance**: Complex patterns may slow down search.
- **Memory Usage**: Large sequences require significant memory.

## Examples

### Search for exact matches
**Args:** `cassiopee -i sequence.fa -p patterns.txt -o matches.tsv`
**Explanation:** Searches sequence for patterns with exact matching.

### Allow mismatches
**Args:** `cassiopee -i sequence.fa -p patterns.txt -m 2 -o matches.tsv`
**Explanation:** Allows up to 2 mismatches (Hamming distance).

### Allow indels
**Args:** `cassiopee -i sequence.fa -p patterns.txt -g 1 -o matches.tsv`
**Explanation:** Allows gaps/indels in pattern matching.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.