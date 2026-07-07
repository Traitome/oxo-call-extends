---
name: hitea
category: structural-variation
description: HiTea identifies transposable element insertions using Hi-C data by capitalizing on clipped reads and discordant read pairs.
tags: [hitea, Hi-C, transposable-elements, structural-variation, TE-insertions]
author: oxo-call-community
source_url: "https://github.com/parklab/HiTea"
---

## Concepts

- **TE Insertion Detection**: HiTea detects non-reference transposable element insertions from Hi-C data.

- **Clipped Reads**: Capitalizes on clipped Hi-C reads to identify insertion breakpoints.

- **Discordant Read Pairs**: Uses discordant read pairs in Hi-C data for detection.

- **Filtering Steps**: Series of filtering steps to remove false positive insertions.

- **TE Families**: Detects three major families of active human transposable elements.

- **Hi-C Data**: Designed to work with Hi-C chromatin conformation capture data.

## Pitfalls

- **Uneven Coverage**: Hi-C data has uneven genome coverage which affects detection sensitivity.

- **False Positives**: Requires careful filtering to remove potential false positive instances.

- **Restriction Site**: Filtering considers presence of restriction endonuclease site at breakpoint.

- **Amplification Artifacts**: Clusters with same start, clip, and read-orientation are omitted.

- **Reference Bias**: May miss insertions in regions with poor reference coverage.

## Examples

### Run HiTea on Hi-C data
**Args:** `hitea --bam hic.bam --output te_insertions.vcf`
**Explanation:** Detects transposable element insertions from Hi-C BAM file.

### With custom TE reference
**Args:** `hitea --bam hic.bam --te-reference te_consensus.fasta --output te_insertions.vcf`
**Explanation:** Uses custom transposable element consensus sequences.

### With quality filtering
**Args:** `hitea --bam hic.bam --min-quality 30 --output te_insertions.vcf`
**Explanation:** Filters reads by mapping quality score.

### Batch processing
**Args:** `for f in *.bam; do hitea --bam $f --output ${f%.bam}_te.vcf; done`
**Explanation:** Processes multiple Hi-C BAM files.

### Generate report
**Args:** `hitea --bam hic.bam --output te_insertions.vcf --report report.html`
**Explanation:** Generates comprehensive analysis report.

### With breakpoint validation
**Args:** `hitea --bam hic.bam --validate-breakpoints --output te_insertions.vcf`
**Explanation:** Validates detected breakpoints using additional criteria.

### Help command
**Args:** `hitea --help`
**Explanation:** Shows available options and usage information.