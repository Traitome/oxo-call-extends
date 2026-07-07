---
name: nextalign
category: alignment
description: Nextalign is a tool for rapid and accurate viral genome sequence alignment.
tags: [nextalign, alignment, viral-genomics, nextstrain, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/nextstrain/nextclade"
---

## Concepts

- **Tool Overview**: Nextalign is a fast and accurate aligner specifically designed for viral genomes.
- **Core Function**: Aligns viral sequences to a reference genome with gap-aware alignment.
- **Algorithm**: Uses seeded alignment with affine gap penalties optimized for viral evolution.
- **Input Format**: Accepts FASTA files with viral sequences.
- **Output**: Produces aligned sequences and gap information.
- **Use Case**: Viral genome analysis, outbreak monitoring, and sequence comparison.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Quality**: Results depend on reference genome quality.
- **Sequence Quality**: Low-quality sequences may produce poor alignments.
- **Memory Usage**: Large datasets require memory.
- **Gap Handling**: Complex gap patterns may affect alignment quality.
- **Ambiguity Codes**: May struggle with ambiguous nucleotide codes.

## Examples

### Display help
**Args:** `nextalign --help`
**Explanation:** Shows available options and usage instructions.

### Basic alignment
**Args:** `nextalign --sequences sequences.fasta --reference reference.fasta --output-all output/`
**Explanation:** Aligns sequences to reference genome.

### Output aligned sequences
**Args:** `nextalign --sequences input.fasta --reference ref.fasta --output-sequences aligned.fasta`
**Explanation:** Outputs aligned sequences only.

### Output insertions
**Args:** `nextalign --sequences input.fasta --reference ref.fasta --output-insertions insertions.csv`
**Explanation:** Outputs detected insertions.

### Output deletions
**Args:** `nextalign --sequences input.fasta --reference ref.fasta --output-deletions deletions.csv`
**Explanation:** Outputs detected deletions.

### Report mutations
**Args:** `nextalign --sequences input.fasta --reference ref.fasta --output-mutations mutations.csv`
**Explanation:** Reports mutations relative to reference.

### Threads
**Args:** `nextalign --sequences input.fasta --reference ref.fasta -t 8 --output-all output/`
**Explanation:** Uses 8 threads for parallel processing.