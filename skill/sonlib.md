---
name: sonlib
category: programming
description: sonLib - General purpose library for C and Python bioinformatics
tags: [sonlib, programming, library, c, python, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ComparativeGenomicsToolkit/sonLib"
---

## Concepts

- **Tool Overview**: sonlib (v2.0.dev88) - A bioinformatics library
- **Core Function**: Provides general purpose utilities for bioinformatics
- **Input/Output**: Library functions for C and Python
- **Algorithm**: Utility functions for sequence and genome analysis
- **Installation**: `conda install -c bioconda sonlib`
- **Key Features**: C/Python library, bioinformatics utilities, genome analysis

## Pitfalls

- **Language Support**: Requires proper C and Python environment
- **Dependencies**: May require additional dependencies
- **Memory Usage**: Large genomes require significant memory
- **API Changes**: API may change between versions
- **Compilation**: C library requires proper compilation
- **Python Version**: Requires compatible Python version

## Examples

### Display help
**Args:** `python -c "import sonLib; help(sonLib)"`
**Explanation:** Shows module documentation.

### Basic sequence operations
**Args:** `python -c "import sonLib.bioio; sonLib.bioio.readFasta('sequences.fasta')"`
**Explanation:** Read FASTA sequences.

### Write FASTA
**Args:** `python -c "import sonLib.bioio; sonLib.bioio.writeFasta(sequences, 'output.fasta')"`
**Explanation:** Write FASTA sequences.

### Get sequence length
**Args:** `python -c "import sonLib.bioio; length = sonLib.bioio.getSequenceLength('sequences.fasta')"`
**Explanation:** Get sequence length.

### Parse BED file
**Args:** `python -c "import sonLib.bioio; bed = sonLib.bioio.readBed('regions.bed')"`
**Explanation:** Parse BED file.

### Write BED file
**Args:** `python -c "import sonLib.bioio; sonLib.bioio.writeBed(regions, 'output.bed')"`
**Explanation:** Write BED file.

### Get random sequence
**Args:** `python -c "import sonLib.bioio; seq = sonLib.bioio.getRandomSequence(1000)"`
**Explanation:** Generate random sequence.

### Calculate GC content
**Args:** `python -c "import sonLib.bioio; gc = sonLib.bioio.getGCContent(sequence)"`
**Explanation:** Calculate GC content.