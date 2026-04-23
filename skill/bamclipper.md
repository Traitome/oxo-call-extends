---
name: bamclipper
category: qc
description: Bamclipper - Remove primer sequences from BAM alignments by soft-clipping
tags: [primer-removal, amplicon-sequencing, soft-clipping, bam-processing]
author: oxo-call-community
source_url: "https://github.com/tommyau/bamclipper"
---

## Concepts

- **Tool Overview**: Bamclipper removes primer sequences from amplicon sequencing BAM alignments by soft-clipping, preserving read quality and alignment information.

- **Soft-Clipping**: Uses soft-clipping to remove primer sequences without discarding reads, maintaining alignment coordinates.

- **Amplicon Focus**: Designed for amplicon sequencing data where primers are present in reads.

- **BED Input**: Accepts primer positions in BED format for flexible primer specification.

## Pitfalls

- **Primer BED Required**: Requires accurate primer position BED file. Incorrect positions lead to poor clipping.

- **Primer Variants**: Primer sequence variants may not be clipped correctly. Use degenerate primer definitions if needed.

- **Alignment Coordinates**: Soft-clipping preserves coordinates but read length changes. Downstream tools must handle this.

## Examples

### Basic primer clipping
**Args:** `bamclipper.sh -b alignments.bam -p primers.bed -o clipped.bam`
**Explanation:** Removes primer sequences defined in BED file by soft-clipping.

### Multiple BAM files
**Args:** `bamclipper.sh -b sample1.bam sample2.bam -p primers.bed -o output_dir/`
**Explanation:** Processes multiple BAM files with same primer definitions.

### Specify threads
**Args:** `bamclipper.sh -b alignments.bam -p primers.bed -t 8 -o clipped.bam`
**Explanation:** Uses 8 threads for parallel processing of large BAM files.
