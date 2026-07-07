---
name: shorttracks
category: alignment
description: ShortTracks - Generate length- and strand-based coverage files from small RNA-seq alignments
tags: ["shorttracks", "alignment", "bam", "bigwig"]
author: oxo-call-community
source_url: "https://github.com/MikeAxtell/ShortTracks"
---

## Concepts

- **Tool Overview**: ShortTracks (v1.3) generates coverage tracks from small RNA-seq alignments.
- **Core Function**: Creates strand-specific bigwig files for visualization.
- **Algorithm**: Uses BAM alignments to calculate coverage by read length and strand.
- **Input/Output**: Accepts BAM files and produces bigwig coverage tracks.
- **Coverage Analysis**: Focuses on length-specific and strand-specific coverage.
- **Applications**: Small RNA-seq visualization, genome browser tracks.

## Pitfalls

- **BAM Requirements**: Requires sorted and indexed BAM files.
- **Memory Usage**: High memory requirements for large datasets.
- **Chromosome Names**: Requires consistent chromosome naming.
- **Input Quality**: Results depend on alignment quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Generate coverage tracks
**Args:** `shorttracks -i alignments.bam -o coverage/`
**Explanation:** `-i` input BAM; `-o` output directory.

### With genome size
**Args:** `shorttracks -i alignments.bam -g genome.fasta -o coverage/`
**Explanation:** `-g` genome FASTA for chromosome sizes.

### Strand-specific
**Args:** `shorttracks -i alignments.bam -s -o coverage/`
**Explanation:** `-s` strand-specific output.

### Help command
**Args:** `shorttracks --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shorttracks --version`
**Explanation:** Shows current version.

### Length filtering
**Args:** `shorttracks -i alignments.bam -m 18 -M 30 -o coverage/`
**Explanation:** `-m/-M` minimum/maximum read length.

### Verbose mode
**Args:** `shorttracks -v -i alignments.bam -o coverage/`
**Explanation:** `-v` verbose output.
