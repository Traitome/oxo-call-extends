---
name: mobster
category: formatting
description: NGS tool for detecting MEI and gene retrotransposition events in WGS and WES data.
tags: [mobster, formatting, mobile-elements]
author: oxo-call-community
source_url: "https://github.com/jyhehir/mobster"
---

## Concepts

- **Tool Overview**: MOBSTER v0.2.4.1 detects mobile element insertions and retrotransposition events.
- **Core Function**: Identifies MEI (Mobile Element Insertions) in sequencing data.
- **Retrotransposition Detection**: Finds gene retrotransposition events.
- **WGS/WES Support**: Works with whole-genome and whole-exome sequencing data.
- **Input/Output**: Accepts BAM files; outputs MEI calls.
- **Structural Variation**: Supports detection of insertion-type structural variants.

## Pitfalls

- **Detection Specific**: Focused on mobile element insertions only.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for optimal detection.
- **Data Quality**: Results depend on sequencing coverage and quality.
- **Reference Genome**: Requires appropriate reference genome.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Detect MEI events
**Args:** `mobster -i alignments.bam -g genome.fasta -o mei_calls.vcf`
**Explanation:** Detects mobile element insertions from aligned reads.

### With quality filtering
**Args:** `mobster -i alignments.bam -g genome.fasta -q -o mei_calls.vcf`
**Explanation:** Applies quality filtering before calling.

### Verbose output
**Args:** `mobster -i alignments.bam -g genome.fasta -v -o mei_calls.vcf`
**Explanation:** Shows detailed detection process.

### Output in BED format
**Args:** `mobster -i alignments.bam -g genome.fasta -f bed -o mei_calls.bed`
**Explanation:** Outputs MEI calls in BED format.

### Batch processing
**Args:** `mobster -i bam/ -g genome.fasta -o results/`
**Explanation:** Processes multiple BAM files.