---
name: intervaltree_bio
category: utility
description: Interval tree convenience classes for genomic data
tags: [intervaltree_bio, utility, genomics, interval-tree]
author: oxo-call-community
source_url: "https://github.com/konstantint/intervaltree-bio"
---

## Concepts

- **Tool Overview**: intervaltree_bio (v1.0.1) provides GenomeIntervalTree data structure for genomic intervals
- **Core Function**: Efficiently stores and queries genomic intervals for overlap detection
- **BED File Support**: Directly reads BED files and UCSC table formats
- **Algorithm**: Uses interval tree data structure for O(log n + k) overlap queries
- **Installation**: `conda install -c bioconda intervaltree_bio`

## Pitfalls

- **Memory Usage**: Large datasets require significant memory
- **Coordinate System**: Uses 0-based or 1-based coordinates depending on input
- **Chromosome Names**: Ensure consistent chromosome naming conventions
- **Overlap Definition**: Understand how overlaps are defined (inclusive vs exclusive)
- **Performance**: Building the tree can be time-consuming for very large datasets

## Examples

### Load intervals from BED file
**Args:** `python -c "from intervaltree_bio import GenomeIntervalTree; tree = GenomeIntervalTree.from_bed('regions.bed')"`
**Explanation:** Loads genomic intervals from a BED file into an interval tree.

### Query overlapping intervals
**Args:** `python -c "from intervaltree_bio import GenomeIntervalTree; tree = GenomeIntervalTree.from_bed('genes.bed'); overlaps = tree['chr1'].search(100000, 200000)"`
**Explanation:** Finds all intervals on chr1 overlapping the range 100000-200000.

### Load from UCSC table
**Args:** `python -c "from intervaltree_bio import GenomeIntervalTree; knownGene = GenomeIntervalTree.from_table('knownGene')"`
**Explanation:** Loads knownGene table from UCSC into an interval tree.

### Add intervals programmatically
**Args:** `python -c "from intervaltree_bio import GenomeIntervalTree; tree = GenomeIntervalTree(); tree.add('chr1', 100, 200, 'gene1')"`
**Explanation:** Adds a single interval to the genome interval tree.

### Check interval count
**Args:** `python -c "from intervaltree_bio import GenomeIntervalTree; tree = GenomeIntervalTree.from_bed('regions.bed'); print(len(tree))"`
**Explanation:** Prints the total number of intervals in the tree.

### Iterate over all intervals
**Args:** `python -c "from intervaltree_bio import GenomeIntervalTree; tree = GenomeIntervalTree.from_bed('genes.bed'); [print(iv) for iv in tree['chr1']]"`
**Explanation:** Iterates over all intervals on chromosome 1.