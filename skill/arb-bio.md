---
name: arb-bio
category: alignment
description: ARB Sequence Analysis Suite core package for molecular sequence analysis
tags: [arb-bio, alignment, phylogeny, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://www.arb-home.de/documentation.html"
---

## Concepts

- **Tool Overview**: ARB (ARBor, Latin for tree) is a comprehensive software suite for molecular sequence analysis, database management, and phylogeny reconstruction. Version 6.0.6.
- **Core Function**: Provides essential tools for sequence alignment, phylogenetic tree building, and sequence database management with a focus on microbial and environmental sequence analysis.
- **Sequence Database System**: Maintains structured databases for storing sequences, taxonomic information, and metadata, enabling efficient querying and comparative analysis.
- **Phylogeny Methods**: Supports neighbor-joining, maximum likelihood, and parsimony-based tree reconstruction algorithms.
- **Alignment Tools**: Includes multiple sequence alignment algorithms with support for manual editing and refinement.
- **Input/Output**: Supports FASTA, GenBank, EMBL, BAM/SAM, and other standard bioinformatics formats.
- **Installation**: `conda install -c bioconda arb-bio` or download from official ARB website.

## Pitfalls

- **Version Compatibility**: Database formats and command-line options may differ between versions. Check documentation for your specific version.
- **Memory Requirements**: Large sequence databases require significant RAM. Monitor system resources during analysis.
- **Input Format**: Ensure sequences are in supported formats. ARB has specific requirements for database initialization.
- **Phylogeny Computation**: Tree building for large datasets can be computationally intensive.
- **Graphical Interface**: Some features require the GUI, which may not be available in headless environments.
- **Database Locking**: Concurrent access to ARB databases can cause conflicts. Use proper file permissions.

## Examples

### Display help
**Args:** `arb --help`
**Explanation:** Shows all available command-line options and usage information for the ARB suite.

### Initialize new sequence database
**Args:** `arb -create my_database.arb`
**Explanation:** Creates a new ARB database file with default schema and settings.

### Import sequences
**Args:** `arb -import sequences.fasta -db my_database.arb`
**Explanation:** Imports sequences from FASTA file into the specified ARB database.

### Build phylogenetic tree
**Args:** `arb -db my_database.arb -tree neighbor-joining -out tree.newick`
**Explanation:** Constructs a neighbor-joining tree from aligned sequences in the database.

### Export aligned sequences
**Args:** `arb -db my_database.arb -export aligned.fasta -format fasta`
**Explanation:** Exports aligned sequences from database to FASTA format for downstream analysis.

### Run sequence alignment
**Args:** `arb -align unaligned.fasta -output aligned.arb -method muscle`
**Explanation:** Performs multiple sequence alignment using MUSCLE algorithm.

### Batch processing
**Args:** `for f in *.fasta; do arb -import "$f" -db combined.arb; done`
**Explanation:** Imports multiple FASTA files into a single combined database.