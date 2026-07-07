---
name: bamsnap
category: formatting
description: BamSnap - Visualize BAM alignments as PNG images for specific genomic regions
tags: [bamsnap, formatting, BAM, visualization, png]
author: oxo-call-community
source_url: "https://github.com/parklab/bamsnap"
---

## Concepts

- **Tool Overview**: BamSnap converts BAM alignments to PNG images for specific genomic regions, providing visual representation of read alignments. Version 0.2.19.
- **Core Function**: Generates visual snapshots of BAM alignments for specific genomic regions.
- **Visualization**: Creates PNG images showing read alignments in specified genomic regions.
- **Region Focus**: Visualizes specific genomic regions of interest.
- **Multiple Samples**: Supports comparison of multiple BAM files in same region.
- **Input/Output**: Accepts BAM files, outputs PNG images of alignments.
- **Installation**: `conda install -c bioconda bamsnap`.

## Pitfalls

- **BAM Index Required**: Requires indexed BAM file for region queries.
- **Region Specification**: Requires correct region format (chr:start-end).
- **Image Size**: Output image size depends on region size and read density.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Basic snapshot
**Args:** `bamsnap -b alignments.bam -r chr1:1000-2000 -o snapshot.png`
**Explanation:** Creates PNG snapshot of alignments in specified region.

### Multiple BAM comparison
**Args:** `bamsnap -b sample1.bam sample2.bam -r chr1:1000-2000 -o comparison.png`
**Explanation:** Compares alignments from multiple BAM files.

### Custom image size
**Args:** `bamsnap -b alignments.bam -r chr1:1000-2000 -o snapshot.png --width 1000`
**Explanation:** Creates image with custom width.

### Include reference
**Args:** `bamsnap -b alignments.bam -r chr1:1000-2000 -o snapshot.png -f reference.fasta`
**Explanation:** Includes reference sequence in visualization.

### Highlight variants
**Args:** `bamsnap -b alignments.bam -r chr1:1000-2000 -o snapshot.png -v variants.vcf`
**Explanation:** Highlights variant positions in visualization.

### Vertical mode
**Args:** `bamsnap -b alignments.bam -r chr1:1000-2000 -o snapshot.png --vertical`
**Explanation:** Outputs vertical orientation image.

### Display help
**Args:** `bamsnap --help`
**Explanation:** Shows all available command-line options and usage information.