---
name: fasta3
category: alignment
description: "The FASTA package - protein and DNA sequence similarity searching and alignment programs"
tags: [fasta3, alignment, sequence-search, bioinformatics, phylogenetics]
author: oxo-call-community
source_url: "http://faculty.virginia.edu/wrpearson/fasta"
---

## Concepts

- **Tool Overview**: FASTA3 is a comprehensive package for sequence similarity searching and alignment, including programs like fasta, tfastx, and ssearch.
- **Core Function**: Performs rapid sequence similarity searches and produces alignments between query and database sequences.
- **Input/Output**: Input: Query sequence (FASTA), database (FASTA). Output: Alignment results, similarity scores.
- **Algorithm**: Uses heuristic methods for fast sequence comparison, including the FASTA algorithm for rapid database searches.
- **Key Features**: Protein and DNA alignment, rapid database searching, multiple alignment programs, statistical significance evaluation, batch processing.
- **Installation**: `conda install -c bioconda fasta3`

## Pitfalls

- **Database Format**: Requires properly formatted FASTA database.
- **Computation Time**: Large databases may require significant processing time.
- **Memory Usage**: Large databases may require significant memory.
- **Statistical Significance**: Requires careful interpretation of scores.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic sequence search
**Args:** `fasta36 query.fasta database.fasta -o results.txt`
**Explanation:** Searches query sequence against database.

### Protein search
**Args:** `tfastx36 protein_query.fasta dna_database.fasta -o results.txt`
**Explanation:** Searches protein query against translated DNA database.

### Smith-Waterman alignment
**Args:** `ssearch36 query.fasta database.fasta -o results.txt`
**Explanation:** Performs rigorous Smith-Waterman alignment.

### Batch queries
**Args:** `fasta36 -f queries.list database.fasta -o results.txt`
**Explanation:** Processes multiple query sequences.

### Output alignment format
**Args:** `fasta36 query.fasta database.fasta -o results.txt -m 8`
**Explanation:** Outputs alignments in tabular format.