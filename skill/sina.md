---
name: sina
category: sequence-analysis
description: SINA - Reference-based multiple sequence alignment
tags: ["sina", "sequence-analysis", "alignment", "16s"]
author: oxo-call-community
source_url: "https://sina.readthedocs.io"
---

## Concepts

- **Tool Overview**: SINA (v1.7.2) performs reference-based multiple sequence alignment.
- **Core Function**: Aligns sequences to a reference database.
- **Algorithm**: Uses profile alignment with reference sequences.
- **Input/Output**: Accepts FASTA sequences and produces aligned sequences.
- **16S rRNA Analysis**: Specialized for 16S rRNA gene alignment.
- **Applications**: Microbiome analysis, phylogenetic studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Reference Database**: Requires reference database preparation.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Align sequences
**Args:** `sina -i sequences.fasta -r reference.fasta -o aligned.fasta`
**Explanation:** `-i` input sequences; `-r` reference; `-o` output.

### Build profile
**Args:** `sina --build-profile -i sequences.fasta -o profile.fasta`
**Explanation:** Builds alignment profile from sequences.

### With identity filter
**Args:** `sina -i sequences.fasta -r reference.fasta -i 0.9 -o aligned.fasta`
**Explanation:** `-i 0.9` minimum identity threshold.

### Help command
**Args:** `sina --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sina --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sina -v -i sequences.fasta -r reference.fasta -o aligned.fasta`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sina -t 8 -i sequences.fasta -r reference.fasta -o aligned.fasta`
**Explanation:** `-t 8` uses 8 threads.
