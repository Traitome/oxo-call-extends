---
name: htseq-clip
category: expression
description: htseq-clip is a toolset for the analysis of eCLIP/iCLIP datasets, extracting crosslink site counts from RNA-binding protein experiments.
tags: [htseq-clip, expression, CLIP, eCLIP, iCLIP, RNA-binding]
author: oxo-call-community
source_url: "https://github.com/EMBL-Hentze-group/htseq-clip"
---

## Concepts

- **Tool Overview**: htseq-clip is a Python package for preprocessing eCLIP and iCLIP sequencing data to identify RNA-binding protein binding sites.
- **Crosslink Site Extraction**: Extracts truncation sites, mutations, and deletions from CLIP sequencing reads at nucleotide resolution.
- **Count Matrix Generation**: Generates crosslink site count matrices for downstream differential binding analysis.
- **Sliding Window Analysis**: Supports aggregation of crosslink sites into sliding windows across gene annotations.
- **Quality Metrics**: Provides metrics including crosslink site density and maximum crosslink sites per nucleotide.
- **Installation**: `conda install -c bioconda htseq-clip`

## Pitfalls

- **Input Requirements**: Requires coordinate-sorted and indexed BAM files as input.
- **Annotation Format**: Gene annotations must be in GFF3 format with proper feature types.
- **Strand Specificity**: Strand information must be correctly specified for strand-specific protocols.
- **Mate Selection**: For paired-end data, correct mate (first or second) must be specified for crosslink extraction.
- **Read Quality**: Low-quality reads can introduce false crosslink sites; pre-filtering recommended.
- **Protocol Specificity**: Parameters may need adjustment for different CLIP protocols (eCLIP vs iCLIP).

## Examples

### Basic crosslink site extraction
**Args:** `htseq-clip count -a annotation.gff3 -b alignments.bam -o crosslink_counts.tsv`
**Explanation:** Extracts crosslink sites from aligned CLIP reads and generates a count matrix using gene annotations.

### Sliding window analysis
**Args:** `htseq-clip count -a annotation.gff3 -b alignments.bam -o window_counts.tsv --window-size 50 --step-size 25`
**Explanation:** Aggregates crosslink sites into 50bp sliding windows with 25bp step size for differential binding analysis.

### Extract from specific mate
**Args:** `htseq-clip count -a annotation.gff3 -b alignments.bam -o counts.tsv --mate 1`
**Explanation:** Extracts crosslink sites specifically from the first mate in paired-end sequencing data.

### Strand-specific analysis
**Args:** `htseq-clip count -a annotation.gff3 -b alignments.bam -o counts.tsv --strand reverse`
**Explanation:** Processes data from reverse-stranded library preparation protocols.

### Generate quality metrics
**Args:** `htseq-clip stats -b alignments.bam -o clip_stats.tsv`
**Explanation:** Computes quality metrics including crosslink site density and distribution statistics.