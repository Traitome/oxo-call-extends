---
name: kbo-cli
category: alignment
description: Command-line interface for the kbo local sequence aligner.
tags: [kbo-cli, alignment, local alignment, sequence comparison]
author: oxo-call-community
source_url: "https://docs.rs/kbo"
---

## Concepts

- **Tool Overview**: kbo-cli (v0.2.1) - CLI for kbo local sequence aligner.
- **Local Alignment**: Performs local sequence alignment.
- **k-mer Based**: Uses k-mer matching for fast alignment.
- **Speed**: Optimized for fast local alignment.
- **Multiple Sequences**: Can align multiple sequence pairs.
- **Score Calculation**: Computes alignment scores.

## Pitfalls

- **k-mer Size**: Choosing appropriate k-mer size is important.
- **Memory Usage**: Large sequences require memory.
- **Alignment Length**: Limited by k-mer size.
- **Gap Handling**: May not handle large gaps well.
- **Sensitivity**: May miss distant homologs.
- **Format Support**: Limited input format support.

## Examples

### Local alignment
**Args:** `kbo align -q query.fasta -t target.fasta -o alignment.txt`
**Explanation:** Performs local alignment between query and target.

### Set k-mer size
**Args:** `kbo align -q query.fasta -t target.fasta -k 15 -o alignment.txt`
**Explanation:** Uses k-mer size of 15 for alignment.

### Multiple targets
**Args:** `kbo align -q query.fasta -t targets.fasta -o alignments.txt`
**Explanation:** Aligns query against multiple targets.

### Output SAM format
**Args:** `kbo align -q query.fasta -t target.fasta -o alignment.sam --sam`
**Explanation:** Outputs alignment in SAM format.

### Verbose mode
**Args:** `kbo align -q query.fasta -t target.fasta -o alignment.txt -v`
**Explanation:** Shows verbose output with alignment details.

### Score only
**Args:** `kbo score -q query.fasta -t target.fasta`
**Explanation:** Outputs only alignment score.