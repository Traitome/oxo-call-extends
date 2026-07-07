---
name: foldseek
category: utility
description: "Foldseek: fast and accurate protein structure search."
tags: [foldseek, protein structure, structure search, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/steineggerlab/foldseek"
---
## Concepts
- **Structure Similarity Search**: Searches for structurally similar proteins in databases.
- **TM-score Calculation**: Uses TM-score for measuring structural similarity.
- **Database Indexing**: Builds compressed indexes for fast searching.
- **Sensitive Search**: Detects remote homologs with low sequence identity but similar structures.
- **GPU Acceleration**: Supports GPU acceleration for faster search performance.

## Pitfalls
- **Database Size**: Large structure databases require significant storage space.
- **Search Speed vs Sensitivity**: Faster modes trade sensitivity for speed.
- **Structure Quality**: Poor quality structures affect search accuracy.
- **Memory Requirements**: Indexing large databases requires substantial RAM.
- **Output Interpretation**: Requires careful interpretation of similarity scores.

## Examples
### Basic structure search
**Args:** `foldseek search query.pdb database results.tsv`
**Explanation:** Searches for structures similar to the query in the specified database.

### Build custom database
**Args:** `foldseek createdb structures/ custom_db`
**Explanation:** Creates a searchable database from a directory of structure files.

### Search with GPU acceleration
**Args:** `foldseek search query.pdb database results.tsv --gpu`
**Explanation:** Performs structure search using GPU acceleration for faster results.

### Calculate TM-score between two structures
**Args:** `foldseek tmscore struct1.pdb struct2.pdb`
**Explanation:** Computes the TM-score between two protein structures.

### Align structures
**Args:** `foldseek align struct1.pdb struct2.pdb alignment.txt`
**Explanation:** Aligns two protein structures and outputs the alignment.