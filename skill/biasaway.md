---
name: biasaway
category: annotation
description: BiasAway - Generate composition-matched background sequences
tags: [background-sequences, gc-content, motif-analysis, enrichment]
author: oxo-call-community
source_url: "https://bitbucket.org/CBGR/biasaway"
---

## Concepts
- **Tool Overview**: BiasAway generates composition-matched background sequences for enrichment analyses. It provides multiple models for creating control sequences that match the nucleotide composition of target sequences.
- **Background Models**: Four models available: mononucleotide shuffle, dinucleotide shuffle, genomic GC-matched, and genomic di-matched.
- **Use Case**: Essential for motif discovery and enrichment analysis where background sequences must be compositionally matched to avoid false positives from sequence composition bias.
- **Integration**: Commonly used with tools like MEME, HOMER, and AME for motif analysis.

## Pitfalls
- **Model Selection**: Different background models are appropriate for different analyses. Mononucleotide shuffling is simplest but may not control for dinucleotide biases.
- **Genomic Background**: When using genomic background models, ensure the reference genome matches your target organism.
- **Sequence Length**: Background sequences should match target sequences in length distribution.

## Examples
### Generate mononucleotide-shuffled background
**Args:** `biasaway shuffle -f target.fa -o background.fa`
**Explanation:** Generates background sequences by mononucleotide shuffling of target sequences.

### Generate dinucleotide-shuffled background
**Args:** `biasaway shuffle -f target.fa -m dinucleotide -o background.fa`
**Explanation:** Generates background sequences preserving dinucleotide frequencies.

### Generate GC-matched genomic background
**Args:** `biasaway genomic -f target.fa -g genome.fa -o background.fa`
**Explanation:** Extracts genomic regions matching the GC content distribution of target sequences.

### Generate background with specific count
**Args:** `biasaway shuffle -f target.fa -n 10 -o background.fa`
**Explanation:** Generates 10 shuffled background sequences per input sequence.
