---
name: jellyfish
category: utility
description: Jellyfish is a tool for fast, memory-efficient counting of k-mers in DNA sequences.
tags: [jellyfish, utility, k-mer, counting, genomics]
author: oxo-call-community
source_url: "http://www.genome.umd.edu/jellyfish.html"
---

## Concepts

- **Tool Overview**: jellyfish (v2.2.10) - A fast, memory-efficient tool for counting k-mers in DNA sequences.
- **k-mer Counting**: Counts occurrences of all k-length substrings in DNA sequences.
- **Memory Efficiency**: Uses hash-based counting with memory-mapped files for efficiency.
- **Multi-threading**: Supports parallel processing for faster counting.
- **k-mer Size**: Configurable k-mer size for different applications.
- **Output Formats**: Generates output in various formats for downstream analysis.

## Pitfalls

- **Memory Requirements**: Large k-mer sizes require significant memory.
- **Disk Space**: Output files can be very large for large genomes.
- **k-mer Size Selection**: Choosing appropriate k-mer size is critical.
- **Sequence Quality**: Low-quality sequences can affect k-mer counting.
- **Duplicate Reads**: PCR duplicates can inflate k-mer counts.
- **File Format**: Requires FASTA or FASTQ input format.

## Examples

### Count k-mers
**Args:** `jellyfish count -m 21 -s 100M -o kmers.jf reads.fastq`
**Explanation:** Counts 21-mers using 100MB hash size.

### Generate k-mer histogram
**Args:** `jellyfish histo kmers.jf > histogram.txt`
**Explanation:** Generates histogram of k-mer frequencies.

### Query k-mer counts
**Args:** `jellyfish query kmers.jf -s query.fasta`
**Explanation:** Queries k-mer counts for sequences in query file.

### Merge multiple k-mer files
**Args:** `jellyfish merge kmers1.jf kmers2.jf -o merged.jf`
**Explanation:** Merges k-mer counts from multiple files.

### Multi-threaded counting
**Args:** `jellyfish count -m 31 -s 500M -t 8 -o kmers.jf reads.fastq`
**Explanation:** Uses 8 threads for parallel k-mer counting.

### Dump k-mer counts
**Args:** `jellyfish dump kmers.jf > kmers.txt`
**Explanation:** Dumps all k-mer counts to text file.