---
name: bx-python
category: programming
description: Python tools for manipulating biological data, particularly multiple sequence alignments
tags: [bx-python, python, alignment, bioinformatics, library]
author: oxo-call-community
source_url: "https://github.com/bxlab/bx-python"
---

## Concepts

- **Tool Overview**: bx-python is a Python library for biological data manipulation.
- **Core Function**: Provides tools for working with alignments, intervals, and genomic data.
- **Features**: MAF format handling, interval operations, and sequence utilities.
- **Modules**: bx.align, bx.intervals, bx.seq, and bx.misc.
- **Installation**: Install via bioconda: `conda install -c bioconda bx-python`

## Pitfalls

- **Python Only**: Python library, not a command-line tool.
- **Python Version**: Requires Python 3.x for current versions.
- **Dependencies**: Some modules require additional packages.

## Examples

### Parse MAF alignment
**Args:** `python -c "from bx.align import maf; reader = maf.Reader(open('align.maf')); print(next(reader))"`
**Explanation:** Reads and parses MAF alignment file.

### Interval operations
**Args:** `python -c "from bx.intervals import IntervalTree; tree = IntervalTree(); tree.insert(0, 100, 'gene1'); print(tree.find(50, 60))"`
**Explanation:** Creates interval tree and finds overlapping intervals.

### Read FASTA
**Args:** `python -c "from bx.seq import fasta; for seq in fasta.fasta_reader('seqs.fa'): print(seq.name)"`
**Explanation:** Iterates over sequences in a FASTA file.
