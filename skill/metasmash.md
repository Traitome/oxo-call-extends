---
name: metasmash
category: metagenomics
description: metaSMASH - scalable metagenome-scale BGC mining, a fork of antiSMASH.
tags: [metasmash, metagenomics, BGC-mining]
author: oxo-call-community
source_url: "https://github.com/canerbagci/metasmash"
---

## Concepts

- **Tool Overview**: metaSMASH v0.1.0 is a fork of antiSMASH designed for scalable biosynthetic gene cluster (BGC) mining at metagenome scale.
- **Core Function**: Identifies and annotates biosynthetic gene clusters from metagenomic sequences.
- **BGC Detection**: Detects various types of biosynthetic gene clusters including antibiotics, toxins, and secondary metabolites.
- **Scalable Mining**: Optimized for large-scale metagenomic datasets with bounded memory usage.
- **Input/Output**: Accepts FASTA-formatted sequences; outputs annotated BGCs with functional predictions.
- **AntiSMASH Fork**: Based on antiSMASH with modifications for metagenomic analysis.

## Pitfalls

- **Memory Management**: Processing large metagenomic datasets may require careful memory management.
- **False Positives**: May detect false positive BGCs.
- **Database Completeness**: Detection accuracy depends on reference database completeness.
- **Runtime**: Analyzing large datasets can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Complexity**: BGC detection can be complex and may produce ambiguous results.

## Examples

### Mine BGCs from sequences
**Args:** `metasmash -i sequences.fasta -o results/`
**Explanation:** Identifies biosynthetic gene clusters from input sequences.

### With custom database
**Args:** `metasmash -i sequences.fasta -d custom_db/ -o results/`
**Explanation:** Uses a custom database for BGC detection.

### Detailed annotation
**Args:** `metasmash -i sequences.fasta -o results/ -v`
**Explanation:** Generates detailed annotations with verbose output.

### Batch processing
**Args:** `metasmash -i fasta/ -o results/`
**Explanation:** Processes multiple FASTA files in batch mode.

### Focus on specific BGC types
**Args:** `metasmash -i sequences.fasta -o results/ --types PKS NRPS`
**Explanation:** Focuses detection on specific types of biosynthetic gene clusters.