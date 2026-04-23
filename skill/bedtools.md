---
name: bedtools
category: annotation
description: BEDtools - A powerful toolset for genome arithmetic
tags: [bed, genomic-intervals, intersection, merge, coverage, subtract, shuffle, closest, window]
author: oxo-call-community
source_url: "https://github.com/arq5x/bedtools2"
---

## Concepts
- **Tool Overview**: BEDtools is the most widely used suite of utilities for comparing genomic features. It provides over 40 subcommands for performing arithmetic on genomic intervals (intersection, merge, subtract, complement, etc.) and is essential for virtually any bioinformatics workflow involving interval data.
- **Core Operations**: `intersect` (find overlaps), `merge` (combine overlapping intervals), `subtract` (remove intervals), `complement` (find gaps), `closest` (find nearest feature), `window` (find nearby features), `coverage` (compute coverage), `shuffle` (randomize positions), `sort` (sort intervals), `bamtobed` (BAM to BED conversion), `getfasta` (extract sequences).
- **Input Formats**: Supports BED, GFF, VCF, BAM, and custom interval formats.
- **Chaining Operations**: Multiple bedtools commands can be piped together for complex analyses.
- **Genome File**: Some operations require a genome file listing chromosome sizes for proper coordinate handling.

## Pitfalls
- **Sorted Input Required**: `merge`, `coverage`, `complement`, and other operations require pre-sorted input. Use `sort -k1,1 -k2,2n` or `bedtools sort`.
- **Coordinate System**: BED is 0-based half-open; GFF/VCF are 1-based. bedtools handles conversion internally but be aware when mixing formats.
- **Memory Usage**: Some operations (e.g., `intersect` with large files) can consume significant memory. Use `-sorted` flag with sorted input for streaming mode.
- **Strand Awareness**: Use `-s` flag for strand-specific operations; otherwise, strand is ignored.

## Examples
### Find overlaps between reads and genes
**Args:** `bedtools intersect -a reads.bed -b genes.bed > overlaps.bed`
**Explanation:** Reports all overlaps between reads and gene annotations.

### Report only reads with at least one overlap
**Args:** `bedtools intersect -a reads.bed -b genes.bed -u > reads_with_genes.bed`
**Explanation:** Reports reads that overlap at least one gene, showing each read once.

### Report reads with no overlap
**Args:** `bedtools intersect -a reads.bed -b genes.bed -v > reads_no_genes.bed`
**Explanation:** Reports reads that do NOT overlap any genes.

### Count overlaps per feature
**Args:** `bedtools intersect -a genes.bed -b reads.bed -c > genes_with_counts.bed`
**Explanation:** Appends a count column showing how many reads overlap each gene.

### Require reciprocal overlap
**Args:** `bedtools intersect -a sv.bed -b segdups.bed -f 0.50 -r > reciprocal_overlaps.bed`
**Explanation:** Reports overlaps where at least 50% of BOTH features overlap (reciprocal).

### Merge overlapping intervals
**Args:** `bedtools merge -i sorted.bed > merged.bed`
**Explanation:** Merges overlapping or adjacent intervals into single records.

### Merge and count merged features
**Args:** `bedtools merge -i sorted.bed -c 4 -o count > merged_with_counts.bed`
**Explanation:** Merges intervals and reports how many original features were merged.

### Find closest feature
**Args:** `bedtools closest -a genes.bed -b enhancers.bed > nearest_enhancers.bed`
**Explanation:** For each gene, finds the closest enhancer.

### Subtract introns from genes to get exons
**Args:** `bedtools subtract -a genes.bed -b introns.bed > exons.bed`
**Explanation:** Removes intron regions from gene regions, leaving exon regions.

### Compute coverage over windows
**Args:** `bedtools coverage -a windows.bed -b reads.bed > coverage.bed`
**Explanation:** Computes the depth and breadth of read coverage over each window.

### Find features within a window
**Args:** `bedtools window -a snps.bed -b genes.bed -w 10000 > nearby_genes.bed`
**Explanation:** Finds genes within 10kb of each SNP.

### Shuffle features randomly
**Args:** `bedtools shuffle -i peaks.bed -g hg38.genome -excl blacklist.bed > shuffled.bed`
**Explanation:** Randomly repositions peaks, excluding blacklisted regions.

### Extract sequences from BED
**Args:** `bedtools getfasta -fi genome.fa -bed regions.bed -fo regions.fa`
**Explanation:** Extracts FASTA sequences corresponding to BED regions.

### Convert BAM to BED
**Args:** `bedtools bamtobed -i reads.bam > reads.bed`
**Explanation:** Converts BAM alignments to BED format.
