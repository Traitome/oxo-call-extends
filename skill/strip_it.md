---
name: strip_it
category: chemistry
description: Strip-it extracts predefined scaffolds from organic small molecules.
tags: [strip_it, chemoinformatics, scaffold-extraction, molecules]
author: oxo-call-community
source_url: "http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/strip-it/1.0.2/strip-it.html"
---

## Concepts

- **Tool Overview**: strip_it (v1.0.2) is a program for extracting predefined scaffolds from organic small molecules.
- **Core Function**: Identifies and extracts molecular scaffolds from chemical structures.
- **Algorithm**: Uses pattern matching to identify and extract scaffold patterns.
- **Input/Output**: Input: Molecular structure file (SMILES/SDF); Output: Extracted scaffolds.
- **Applications**: Chemoinformatics, drug discovery, molecular analysis.
- **Installation**: `conda install -c bioconda strip_it` or download from website.

## Pitfalls

- **Input Format**: Requires specific molecular structure format.
- **Scaffold Library**: Depends on predefined scaffold library.
- **Structure Quality**: Poor quality structures affect extraction.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Ambiguity**: Ambiguous structures may produce multiple scaffolds.

## Examples

### Display help
**Args:** `strip_it --help`
**Explanation:** Shows available options and usage information.

### Basic scaffold extraction
**Args:** `strip_it -i molecules.sdf -o scaffolds.txt`
**Explanation:** Extract scaffolds from molecular structures.

### With SMILES input
**Args:** `strip_it -i molecules.smi -o scaffolds.txt -f smiles`
**Explanation:** Process SMILES format input.

### Verbose mode
**Args:** `strip_it -i molecules.sdf -o scaffolds.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Custom scaffold library
**Args:** `strip_it -i molecules.sdf -o scaffolds.txt -l custom_scaffolds.txt`
**Explanation:** Use custom scaffold library.

### Batch processing
**Args:** `strip_it -i structures/ -o results/`
**Explanation:** Process multiple structure files together.

### Filter by size
**Args:** `strip_it -i molecules.sdf -o scaffolds.txt -m 5`
**Explanation:** Minimum scaffold size of 5 atoms.

### Include statistics
**Args:** `strip_it -i molecules.sdf -o scaffolds.txt --stats`
**Explanation:** Generate statistics about extracted scaffolds.

### Generate report
**Args:** `strip_it -i molecules.sdf -o scaffolds.txt --report`
**Explanation:** Generate comprehensive HTML report.
