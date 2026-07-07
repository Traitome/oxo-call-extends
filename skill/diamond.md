---
name: diamond
category: alignment
description: DIAMOND - Accelerated BLAST-compatible sequence aligner.
tags: [diamond, alignment, blast, sequence-search, protein]
author: oxo-call-community
source_url: "https://github.com/bbuchfink/diamond"
---

## Concepts

- **Tool Overview**: diamond (v2.1.24+) is a high-performance BLAST-compatible sequence aligner optimized for protein and translated DNA searches.
- **Core Function**: Performs fast sequence alignment similar to BLAST but achieves up to 20,000x speed improvement for protein searches.
- **Input/Output**: Input: FASTA query sequences, DIAMOND database. Output: Alignments in BLAST-compatible formats (m8, SAM, etc.).
- **Algorithm**: Uses double-indexing and SIMD vectorization for accelerated sequence comparison.
- **Key Features**: BLAST compatibility, 20,000x faster than BLASTP, supports protein and translated searches, multiple output formats, low memory usage.
- **Installation**: `conda install -c bioconda diamond`

## Pitfalls

- **Database Requirement**: Must create database with `diamond makedb` before running searches.
- **Memory Usage**: Large databases may require significant memory.
- **Sensitivity/ Speed Tradeoff**: Higher sensitivity modes are slower.
- **Output Format**: Default format may require adjustment for specific downstream tools.
- **Version Compatibility**: Database format may change between major versions.

## Examples

### Create protein database
**Args:** `makedb --in proteins.fa -d mydb`
**Explanation:** Creates DIAMOND database from protein sequences.

### Run protein search
**Args:** `blastp -d mydb -q queries.fa -o matches.m8`
**Explanation:** Runs BLASTP-like protein search against database.

### Translated nucleotide search
**Args:** `blastx -d mydb -q dna_queries.fa -o matches.m8`
**Explanation:** Translates DNA queries and searches against protein database.

### With sensitivity settings
**Args:** `blastp -d mydb -q queries.fa -o matches.m8 --sensitive`
**Explanation:** Use sensitive mode for better detection of distant homologs.

### Output in SAM format
**Args:** `blastp -d mydb -q queries.fa -o matches.sam --outfmt 100`
**Explanation:** Output alignments in SAM format for variant calling pipelines.