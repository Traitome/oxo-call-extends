---
name: cgelib
category: genomics
description: Future replacement for cgecore - Shared library for CGE bioinformatics tools
tags: [cgelib, genomic-epidemiology, cge, bioinformatics, library]
author: oxo-call-community
source_url: "https://genomicepidemiology.org/"
---

## Concepts

- **Tool Overview**: CGELib is the next-generation core library for Center for Genomic Epidemiology tools, intended to replace cgecore.
- **Core Function**: Provides shared classes and functions for sequence analysis, database management, and typing across CGE tools.
- **Features**: Modern API design, improved performance, sequence processing utilities, and database integration.
- **Input**: Bacterial genome sequences and typing data.
- **Output**: Analysis results, typing predictions, and annotation data.
- **Application**: Bacterial genomic epidemiology and antimicrobial resistance analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cgelib`

## Pitfalls

- **Migration Transition**: During transition from cgecore, API may change.
- **Version Compatibility**: Ensure compatibility with other CGE tools.
- **Documentation**: New API may have limited documentation initially.
- **Dependency Management**: Requires specific Python version and dependencies.

## Examples

### Import library in Python
**Args:** `python -c "import cgelib; print(cgelib.__version__)"`
**Explanation:** Imports CGELib and checks version.

### Load sequence data
**Args:** `python -c "from cgelib import Sequence; seq = Sequence('genome.fasta')"`
**Explanation:** Loads sequence data using CGELib.

### Run typing analysis
**Args:** `python -c "from cgelib import MLST; result = MLST.analyze('genome.fasta')"`
**Explanation:** Performs MLST typing using CGELib.

### Display help
**Args:** `python -c "help(cgelib)"`
**Explanation:** Shows CGELib documentation.