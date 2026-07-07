---
name: shustring
category: utility
description: shustring - Compute Shortest Unique Substrings
tags: ["shustring", "utility", "sequence", "substring"]
author: oxo-call-community
source_url: "http://guanine.evolbio.mpg.de/cgi-bin/shustring/shustring.cgi.pl"
---

## Concepts

- **Tool Overview**: shustring (v2.6) computes shortest unique substrings in sequences.
- **Core Function**: Finds minimal unique substrings for sequence identification.
- **Algorithm**: Uses suffix tree or suffix array for efficient substring search.
- **Input/Output**: Accepts FASTA sequences and produces unique substrings.
- **Sequence Analysis**: Focuses on identifying unique sequence markers.
- **Applications**: Sequence barcoding, primer design, and sequence identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large sequences.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Size**: Performance degrades with very long sequences.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Find unique substrings
**Args:** `shustring -i sequence.fasta -o results.txt`
**Explanation:** `-i` input FASTA; `-o` output results.

### With minimum length
**Args:** `shustring -i sequence.fasta -m 10 -o results.txt`
**Explanation:** `-m 10` minimum substring length.

### With maximum length
**Args:** `shustring -i sequence.fasta -M 50 -o results.txt`
**Explanation:** `-M 50` maximum substring length.

### Help command
**Args:** `shustring --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shustring --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `shustring -v -i sequence.fasta -o results.txt`
**Explanation:** `-v` verbose output.

### Multiple sequences
**Args:** `shustring -i sequences.fasta -o results.txt`
**Explanation:** Processes multiple sequences in FASTA file.
