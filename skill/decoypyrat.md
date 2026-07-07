---
name: decoypyrat
category: annotation
description: Fast Hybrid Decoy Sequence Database Creation for Proteomic Mass Spectrometry Analyses.
tags: [decoypyrat, annotation, proteomics, mass-spectrometry, decoy-database]
author: oxo-call-community
source_url: "https://github.com/tdido/DecoyPYrat"
---

## Concepts

- **Tool Overview**: decoypyrat (v1.0.1+) is a tool for creating hybrid decoy sequence databases for proteomic mass spectrometry analyses. It generates decoy sequences for false discovery rate estimation.
- **Core Function**: Creates decoy protein sequences by reversing, shuffling, or combining protein sequences to generate a target-decoy database for FDR calculation in proteomics.
- **Input/Output**: Input: Target protein FASTA database. Output: Combined target-decoy FASTA database, decoy-only database.
- **Algorithm**: Implements multiple decoy generation strategies including reverse, shuffle, and hybrid approaches for creating decoy sequences.
- **Key Features**: Fast decoy generation, multiple strategies, hybrid approaches, target-decoy database creation, FDR estimation support.
- **Installation**: `conda install -c bioconda decoypyrat`

## Pitfalls

- **Decoy Strategy**: Different strategies affect FDR estimation.
- **Database Size**: Large databases may require significant memory.
- **Contamination**: Ensure target database is clean.
- **Decoy Proportion**: Typically 1:1 target to decoy ratio.
- **Search Engine Compatibility**: Ensure compatibility with search engines.

## Examples

### Create decoy database
**Args:** `decoypyrat -i target.fasta -o target_decoy.fasta`
**Explanation:** Create combined target-decoy database using default settings.

### Use reverse strategy
**Args:** `decoypyrat -i target.fasta -o target_decoy.fasta -s reverse`
**Explanation:** Use reverse decoy generation strategy.

### Create separate decoy database
**Args:** `decoypyrat -i target.fasta -o decoy.fasta --decoy-only`
**Explanation:** Generate only decoy sequences without targets.