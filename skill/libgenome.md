---
name: libgenome
category: bioinformatics
description: C++ library for DNA and protein sequence manipulation
tags: [libgenome, bioinformatics, C++, sequence-analysis, genome]
author: oxo-call-community
source_url: "https://darlinglab.org/mauve/mauve.html"
---

## Concepts

- **Sequence Operations**: Manipulation of DNA and protein sequences
- **Annotation Handling**: Processing sequence annotations
- **Multiple Formats**: Support for various sequence formats
- **FASTA/FASTQ**: Reading and writing FASTA/FASTQ files
- **Genomic Analysis**: Tools for genomic sequence analysis
- **Sequence Comparison**: Basic sequence comparison operations

## Pitfalls

- **Memory Usage**: Large sequences require memory management
- **Format Compatibility**: Strict format requirements
- **Error Handling**: Requires careful error checking
- **Thread Safety**: Not thread-safe by default
- **Version Compatibility**: API may change between versions
- **Performance**: May require optimization for large genomes

## Examples

### Read sequence
**Args:** `genome read -i genome.fasta -o genome.dat`
**Explanation:** Reads genomic sequence file.

### Write sequence
**Args:** `genome write -i genome.dat -o output.fasta`
**Explanation:** Writes sequence to FASTA format.

### Extract region
**Args:** `genome extract -i genome.dat -c chr1 -s 1 -e 1000 -o region.fasta`
**Explanation:** Extracts specific genomic region.

### Sequence length
**Args:** `genome length -i genome.dat`
**Explanation:** Shows sequence length.

### GC content
**Args:** `genome gc -i genome.fasta`
**Explanation:** Calculates GC content.

### Sequence comparison
**Args:** `genome compare -i1 seq1.fasta -i2 seq2.fasta -o diff.txt`
**Explanation:** Compares two sequences.