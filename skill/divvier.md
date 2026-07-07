---
name: divvier
category: alignment
description: Divvier - Tool for removing multiple sequence alignment uncertainty.
tags: [divvier, alignment, uncertainty, trimming, msa]
author: oxo-call-community
source_url: "https://github.com/simonwhelan/Divvier"
---

## Concepts

- **Tool Overview**: Divvier (v1.01+) is a tool for removing uncertain regions from multiple sequence alignments.
- **Core Function**: Identifies and removes alignment columns with high uncertainty or ambiguity.
- **Input/Output**: Input: Multiple sequence alignments (FASTA/PHYLIP). Output: Cleaned alignments with reduced uncertainty.
- **Algorithm**: Uses various metrics to assess alignment confidence and remove uncertain positions.
- **Key Features**: Alignment cleaning, uncertainty assessment, gap handling, column filtering, quality improvement.
- **Installation**: `conda install -c bioconda divvier`

## Pitfalls

- **Input Requirements**: Requires multiple sequence alignment in FASTA format.
- **Over-trimming**: May remove biologically meaningful regions if thresholds are too strict.
- **Alignment Quality**: Poor input alignment affects uncertainty assessment.
- **Parameter Selection**: Choosing appropriate uncertainty thresholds is critical.
- **Format Compatibility**: Not all alignment formats may be supported.

## Examples

### Remove uncertain regions
**Args:** `divvier --input alignment.fa --output cleaned.fa`
**Explanation:** Removes uncertain regions from multiple sequence alignment.

### With custom threshold
**Args:** `divvier --input alignment.fa --output cleaned.fa --threshold 0.9`
**Explanation:** Use custom uncertainty threshold for filtering.

### Keep gap-only columns
**Args:** `divvier --input alignment.fa --output cleaned.fa --keep-gaps`
**Explanation:** Retain columns with only gaps.

### Generate uncertainty report
**Args:** `divvier --input alignment.fa --output cleaned.fa --report uncertainty.tsv`
**Explanation:** Generate report of alignment uncertainty per column.

### Multiple output formats
**Args:** `divvier --input alignment.fa --output cleaned.fa --format phylip`
**Explanation:** Output alignment in PHYLIP format.