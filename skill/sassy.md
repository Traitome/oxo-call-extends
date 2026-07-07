---
name: sassy
category: utility
description: Fast approximate string searching for bioinformatics applications
tags: ["sassy", "utility", "string-search", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/ragnargrootkoerkamp/sassy"
---

## Concepts

- **Tool Overview**: sassy (v0.2.2) is a fast approximate string searching tool optimized for bioinformatics applications, enabling efficient pattern matching with mismatches.
- **Core Function**: Performs rapid approximate string matching with configurable edit distance thresholds.
- **Algorithm**: Implements bit-parallel string matching algorithms for fast pattern searching with mismatches.
- **Input/Output**: Accepts text files or stdin and produces matched positions with edit distances.
- **Performance**: Designed for high-throughput applications with large sequence datasets.
- **Applications**: Sequence searching, pattern matching, and motif finding in genomic data.

## Pitfalls

- **Memory Usage**: High memory consumption for large pattern sets.
- **Pattern Length**: Performance degrades with very long patterns.
- **Edit Distance**: Search time increases exponentially with allowed mismatches.
- **Indexing Overhead**: Preprocessing time for large reference sequences.
- **Output Volume**: May produce large output files for highly repetitive sequences.
- **Parameter Tuning**: Requires careful adjustment of sensitivity parameters.

## Examples

### Basic pattern search
**Args:** `sassy -p pattern.txt -i sequences.fasta -o matches.tsv`
**Explanation:** `-p` pattern file; `-i` input sequences; `-o` output matches with positions.

### Allow mismatches
**Args:** `sassy -p pattern.txt -i sequences.fasta -m 2 -o matches.tsv`
**Explanation:** `-m 2` allows up to 2 mismatches in the pattern match.

### Case insensitive
**Args:** `sassy -p pattern.txt -i sequences.fasta -c -o matches.tsv`
**Explanation:** `-c` enables case-insensitive matching.

### Output all matches
**Args:** `sassy -p pattern.txt -i sequences.fasta -a -o all_matches.tsv`
**Explanation:** `-a` outputs all matches instead of best match only.

### Progress tracking
**Args:** `sassy -p pattern.txt -i sequences.fasta -v -o matches.tsv`
**Explanation:** `-v` enables verbose progress tracking.

### From stdin
**Args:** `cat sequences.fasta | sassy -p pattern.txt -o matches.tsv`
**Explanation:** Reads input from standard input pipe.

### Multiple patterns
**Args:** `sassy -p patterns.txt -i sequences.fasta -o matches.tsv`
**Explanation:** Processes multiple patterns from a single file.