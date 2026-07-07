---
name: hs-blastn
category: alignment
description: High-speed BLASTN - a fast and accurate nucleotide-nucleotide sequences aligner
tags: [hs-blastn, alignment, blast, nucleotide, sequence_search]
author: oxo-call-community
source_url: "https://github.com/chenying2016/queries"
---

## Concepts

- **FMD-index**: Uses a Ferragina-Manzini index for fast seed lookup
- **Parallel Processing**: Implements parallel algorithms for accelerated search
- **MegaBLAST Acceleration**: Specifically optimized for MegaBLAST-like searches
- **Memory Efficiency**: More memory-efficient than traditional BLAST for large databases
- **Exact Match**: Produces results identical to NCBI BLAST
- **Scalability**: Designed for large-scale sequence database searches

## Pitfalls

- **Index Construction**: Building the FMD-index requires time and memory
- **Database Format**: Requires preprocessing of database into FMD-index format
- **Short Reads**: May not be optimal for very short read sequences
- **Parameter Tuning**: Default parameters may need adjustment for specific use cases
- **Compatibility**: Output format may differ slightly from NCBI BLAST
- **Resource Requirements**: Index construction is computationally intensive

## Examples

### Basic alignment search
**Args:** `hs-blastn -query query.fasta -db ref_db -out results.txt`
**Explanation:** Runs HS-BLASTN search against a reference database.

### Build FMD-index
**Args:** `hs-blastn -build_index ref_db.fasta -out ref_db.index`
**Explanation:** Builds FMD-index for the reference database.

### With E-value threshold
**Args:** `hs-blastn -query query.fasta -db ref_db -out results.txt -evalue 1e-10`
**Explanation:** Sets E-value threshold to 1e-10 for more stringent filtering.

### Parallel mode
**Args:** `hs-blastn -query query.fasta -db ref_db -out results.txt -threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output in BLAST format
**Args:** `hs-blastn -query query.fasta -db ref_db -out results.txt -outfmt 6`
**Explanation:** Outputs results in tabular format (format 6).