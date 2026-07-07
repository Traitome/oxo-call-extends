---
name: smof
category: sequence-analysis
description: smof - UNIX-style utilities for FASTA file exploration and manipulation
tags: [smof, sequence-analysis, fasta, utilities, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/incertae-sedis/smof"
---

## Concepts

- **Tool Overview**: smof (v2.22.4) - A collection of UNIX-style utilities for FASTA file processing
- **Core Function**: Provides various utilities for exploring and manipulating FASTA sequences
- **Input/Output**: Accepts FASTA files; outputs processed sequences or statistics
- **Algorithm**: Various sequence processing algorithms
- **Installation**: `conda install -c bioconda smof`
- **Key Features**: Modular utilities, UNIX pipeline compatible, fast performance

## Pitfalls

- **FASTA Format**: Requires properly formatted FASTA files
- **Sequence Length**: May struggle with extremely long sequences
- **Memory Usage**: Some operations require significant memory
- **Output Format**: May need post-processing for specific use cases
- **Command Syntax**: Each utility has its own syntax
- **Compression**: Input files must be uncompressed or properly handled

## Examples

### Display help
**Args:** `smof --help`
**Explanation:** Shows available utilities and usage information.

### Count sequences
**Args:** `smof count -i input.fasta`
**Explanation:** Count number of sequences in FASTA file.

### Calculate statistics
**Args:** `smof stats -i input.fasta`
**Explanation:** Generate sequence statistics (length, GC content, etc.).

### Extract sequence by ID
**Args:** `smof extract -i input.fasta -n "seq1" -o seq1.fasta`
**Explanation:** Extract specific sequence by name.

### Filter by length
**Args:** `smof filter -i input.fasta -m 100 -M 1000 -o filtered.fasta`
**Explanation:** Filter sequences between 100-1000bp.

### Reverse complement
**Args:** `smof revcomp -i input.fasta -o revcomp.fasta`
**Explanation:** Generate reverse complement of sequences.

### Shuffle sequences
**Args:** `smof shuffle -i input.fasta -o shuffled.fasta`
**Explanation:** Randomly shuffle sequences in FASTA file.

### Convert to lowercase
**Args:** `smof lower -i input.fasta -o lowercase.fasta`
**Explanation:** Convert all sequences to lowercase.