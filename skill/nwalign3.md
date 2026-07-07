---
name: nwalign3
category: alignment
description: nwalign3 is a Python 3 compatible implementation of the Needleman-Wunsch global sequence alignment algorithm.
tags: [nwalign3, alignment, needleman-wunsch, python]
author: oxo-call-community
source_url: "https://github.com/briney/nwalign3"
---

## Concepts

- **Tool Overview**: nwalign3 performs global sequence alignment using Needleman-Wunsch algorithm.
- **Core Function**: Aligns two sequences globally with gap penalties.
- **Algorithm**: Implements Needleman-Wunsch dynamic programming algorithm.
- **Input Format**: Accepts sequence strings or FASTA files.
- **Output**: Produces aligned sequences with score.
- **Use Case**: Sequence alignment, comparative genomics, and bioinformatics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Time Complexity**: O(n*m) complexity for sequence alignment.
- **Memory Usage**: Large sequences require memory.
- **Parameter Selection**: Requires appropriate gap penalties.
- **Performance**: Not optimized for very large sequences.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `python -c "import nwalign3; help(nwalign3)"`
**Explanation:** Shows available functions and usage.

### Basic alignment
**Args:** `python -c "import nwalign3; print(nwalign3.global_align('ACGT', 'AGCT'))"`
**Explanation:** Aligns two sequences globally.

### With custom scoring
**Args:** `python -c "import nwalign3; print(nwalign3.global_align('ACGT', 'AGCT', gap_open=-10, gap_extend=-1))"`
**Explanation:** Uses custom gap penalties.

### From FASTA
**Args:** `python -c "import nwalign3; seqs = nwalign3.read_fasta('sequences.fasta'); print(nwalign3.global_align(seqs[0], seqs[1]))"`
**Explanation:** Reads and aligns sequences from FASTA file.

### Output format
**Args:** `python -c "import nwalign3; result = nwalign3.global_align('ACGT', 'AGCT', output='fasta'); print(result)"`
**Explanation:** Outputs alignment in FASTA format.

### Local alignment
**Args:** `python -c "import nwalign3; print(nwalign3.local_align('ACGTGGAT', 'GGAT'))"`
**Explanation:** Performs local alignment.

### Multiple sequences
**Args:** `python -c "import nwalign3; print(nwalign3.multi_align(['ACGT', 'AGCT', 'ACAT']))"`
**Explanation:** Aligns multiple sequences.