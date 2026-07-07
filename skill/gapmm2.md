---
name: gapmm2
category: alignment
description: "Gapmm2: gapped alignment using minimap2."
tags: [gapmm2, alignment, minimap2, gapped alignment]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/gapmm2"
---
## Concepts
- **Gapped Alignment**: Performs gapped alignments using minimap2.
- **Long-read Alignment**: Handles long-read sequencing data.
- **Gap Detection**: Identifies gaps in alignments.
- **Reference Mapping**: Maps reads to reference sequences.
- **SAM Output**: Outputs alignments in SAM format.

## Pitfalls
- **Minimap2 Dependency**: Requires minimap2 installation.
- **Memory Usage**: High memory usage for large references.
- **Gap Sensitivity**: Gap detection sensitivity may vary.
- **Read Length**: Performance varies with read length.
- **Parameter Tuning**: Requires careful parameter selection.

## Examples
### Align with gaps
**Args:** `gapmm2 -d reference.fasta -i reads.fastq -o alignments.sam`
**Explanation:** Performs gapped alignment of reads.

### Specify gap penalty
**Args:** `gapmm2 -d reference.fasta -i reads.fastq -g 5 -o alignments.sam`
**Explanation:** Sets gap opening penalty to 5.

### Long reads mode
**Args:** `gapmm2 -d reference.fasta -i reads.fastq --lr -o alignments.sam`
**Explanation:** Runs in long-read mode.

### Set minimum alignment length
**Args:** `gapmm2 -d reference.fasta -i reads.fastq -m 100 -o alignments.sam`
**Explanation:** Sets minimum alignment length to 100bp.

### Multiple threads
**Args:** `gapmm2 -d reference.fasta -i reads.fastq -t 8 -o alignments.sam`
**Explanation:** Uses 8 threads for alignment.