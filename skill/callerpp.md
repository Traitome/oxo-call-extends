---
name: callerpp
category: variant-calling
description: Consensus caller based on partial order alignment with SPOA
tags: [callerpp, consensus, poa, spoa, variant-calling]
author: oxo-call-community
source_url: "https://github.com/nh13/callerpp"
---

## Concepts

- **Tool Overview**: callerpp generates consensus sequences using partial order alignment.
- **Core Function**: Calls consensus from multiple aligned sequences using SPOA.
- **Algorithm**: Uses partial order alignment for accurate consensus calling.
- **Input**: Multiple aligned sequences in FASTA format.
- **Output**: Consensus sequence and variant calls.
- **Installation**: Install via bioconda: `conda install -c bioconda callerpp`

## Pitfalls

- **Alignment Required**: Requires pre-aligned sequences.
- **Sequence Count**: More sequences improve consensus accuracy.
- **Memory Usage**: Large alignments require significant memory.

## Examples

### Call consensus from alignments
**Args:** `callerpp -i aligned.fa -o consensus.fa`
**Explanation:** Generates consensus sequence from aligned sequences.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
