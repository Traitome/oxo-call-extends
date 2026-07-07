---
name: linkedsv
category: variant-calling
description: LinkedSV - Structural variant caller for 10X Genomics linked-read sequencing data
tags: [linkedsv, variant-calling, structural-variants, 10X-Genomics, linked-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/WGLab/LinkedSV"
---

## Concepts

- **Structural Variant Calling**: Detection of structural variants from sequencing data
- **Linked-read Sequencing**: 10X Genomics linked-read sequencing technology
- **Long-range Information**: Utilizes long-range molecular barcodes
- **SV Detection**: Identification of deletions, duplications, inversions, translocations
- **Barcode Analysis**: Analysis of molecular barcodes for variant detection
- **Genome Assembly**: Integration with genome assembly for variant validation

## Pitfalls

- **Barcode Quality**: Poor barcode quality affects SV detection
- **Coverage Depth**: Requires sufficient sequencing coverage
- **Complex Regions**: Repeat regions may cause false positives
- **Parameter Tuning**: Requires careful parameter optimization
- **Computational Time**: May be slow for large datasets
- **Memory Usage**: Memory-intensive for large genomes

## Examples

### Call structural variants
**Args:** `linkedsv -i aligned.bam -o sv_calls.vcf -r reference.fasta`
**Explanation:** Calls structural variants from aligned linked-reads.

### Deletion detection
**Args:** `linkedsv -i aligned.bam -o deletions.vcf -r reference.fasta -t DEL`
**Explanation:** Detects deletion variants only.

### Threads
**Args:** `linkedsv -i aligned.bam -o sv_calls.vcf -r reference.fasta -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum size
**Args:** `linkedsv -i aligned.bam -o sv_calls.vcf -r reference.fasta -m 50`
**Explanation:** Sets minimum SV size to 50bp.

### Quality filtering
**Args:** `linkedsv -i aligned.bam -o sv_calls.vcf -r reference.fasta -q 30`
**Explanation:** Filters variants by quality score.

### BED region
**Args:** `linkedsv -i aligned.bam -o sv_calls.vcf -r reference.fasta -b regions.bed`
**Explanation:** Analyzes specific genomic regions.