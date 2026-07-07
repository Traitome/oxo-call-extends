---
name: defense-finder
category: annotation
description: Defense Finder - systematic search of all known anti-phage systems in bacterial genomes.
tags: [defense-finder, annotation, phage, defense-systems, bacteria]
author: oxo-call-community
source_url: "https://github.com/mdmparis/defense-finder"
---

## Concepts

- **Tool Overview**: defense-finder (v2.0.1+) is a tool for systematic detection of anti-phage defense systems in bacterial and archaeal genomes. It identifies known defense mechanisms like CRISPR-Cas, restriction-modification, and abortive infection systems.
- **Core Function**: Identifies and annotates anti-phage defense systems in prokaryotic genomes, enabling comparative analysis of bacterial immunity.
- **Input/Output**: Input: Protein FASTA files, genome sequences (FASTA/GenBank). Output: List of detected defense systems, annotations, genomic coordinates.
- **Algorithm**: Uses HMM profiles and pattern matching to identify characteristic protein domains associated with defense systems.
- **Key Features**: Comprehensive database, supports multiple defense system types, annotates genomic context, visualization support, batch processing.
- **Installation**: `conda install -c bioconda defense-finder`

## Pitfalls

- **Input Requirements**: Works best with complete genomes or high-quality protein predictions.
- **Database Coverage**: May miss novel or uncharacterized defense systems.
- **False Positives**: May produce false positive predictions requiring manual verification.
- **Computational Time**: May be slow for very large genomes.
- **Memory Usage**: May require significant memory for large inputs.

## Examples

### Search for defense systems
**Args:** `defense-finder run --input proteins.fa --output results/`
**Explanation:** Searches for anti-phage defense systems in protein sequences.

### From genome sequence
**Args:** `defense-finder run --input genome.fa --output results/ --genome`
**Explanation:** Analyze genome sequence directly for defense systems.

### With visualization
**Args:** `defense-finder run --input genome.fa --output results/ --visualize`
**Explanation:** Generate visualization of detected defense systems.