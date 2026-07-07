---
name: swipe
category: alignment
description: Rapid local alignment search tool using SIMD-optimized Smith-Waterman algorithm.
tags: [swipe, sequence-alignment, smith-waterman, simd]
author: oxo-call-community
source_url: "http://dna.uio.no/swipe"
---

## Concepts

- **Tool Overview**: swipe (v2.1.1) is a fast Smith-Waterman local aligner using SIMD.
- **Core Function**: Performs rapid local sequence alignment searches.
- **Algorithm**: Uses SIMD parallel computing for accelerated Smith-Waterman.
- **Input/Output**: Input: Query sequence, database; Output: Alignments.
- **Applications**: Sequence similarity search, database search, homology detection.
- **Installation**: `conda install -c bioconda swipe` or download from website.

## Pitfalls

- **Memory Requirements**: Large databases require significant memory.
- **Performance**: Depends on SIMD support in CPU.
- **Parameter Tuning**: Incorrect parameters affect alignment.
- **Sequence Quality**: Poor quality sequences affect results.
- **Database Format**: Requires specific database format.
- **Scalability**: Very large databases may be challenging.

## Examples

### Display help
**Args:** `swipe --help`
**Explanation:** Shows available options and usage information.

### Basic database search
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt`
**Explanation:** Search query against database.

### With E-value threshold
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt -e 1e-5`
**Explanation:** Use E-value threshold of 1e-5.

### Verbose mode
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt --stats`
**Explanation:** Generate statistics about search.

### Batch processing
**Args:** `for q in queries/*.fasta; do swipe -i $q -d db.fasta -o results/${q%.fasta}.txt; done`
**Explanation:** Search multiple queries against database.

### Filter by score
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt -s 100`
**Explanation:** Filter by minimum alignment score.

### Include all hits
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt --all`
**Explanation:** Output all alignments.

### Generate report
**Args:** `swipe -i query.fasta -d database.fasta -o alignments.txt --report`
**Explanation:** Generate comprehensive search report.
