---
name: rmats2sashimiplot
category: utility
description: rmats2sashimiplot visualizes rMATS alternative splicing events as sashimi plots.
tags: [rmats2sashimiplot, utility, visualization, sashimi-plot, splicing]
author: oxo-call-community
source_url: "https://github.com/Xinglab/rmats2sashimiplot"
---

## Concepts

- **Tool Overview**: rmats2sashimiplot generates sashimi plots from rMATS output.
- **Core Function**: Visualizes alternative splicing events with read counts.
- **Algorithm**: Uses MISO-style sashimi plot rendering on rMATS AS event coordinates.
- **Input Format**: Accepts rMATS output (MATS_JC.txt, MATS_JCEC.txt) and BAM files.
- **Output**: Produces PDF/PNG sashimi plots.
- **Use Case**: Visualizing differential alternative splicing events.

## Pitfalls

- **BAM Coordinates**: BAM files must use the same chromosome/contig naming convention as rMATS input GTF.
- **rMATS Output Required**: Tool reads rMATS-formatted event files; not a general-purpose sashimi plotter.
- **Coordinate Compatibility**: Ensure BAM is coordinate-sorted and indexed for IGV/visualization compatibility.
- **Color Choices**: Default event-type colors may need adjustment for publication-quality figures.
- **Read Group**: Specify `-t` read group tag matching BAM read group identifier (e.g., '1', '2').
- **Version Mismatch**: rMATS v3 vs v4 output formats differ; use matching rmats2sashimiplot version.

## Examples

### Display help
**Args:** `rmats2sashimiplot --help`
**Explanation:** Shows all available flags and required input arguments.

### Plot SE events from rMATS
**Args:** `rmats2sashimiplot --b1 s1.bam --b2 s2.bam -o plots/ --event-type SE -e MATS_output/SE.MATS.JC.txt`
**Explanation:** `--b1`/`--b2` are sample BAMs; `-o` output dir; `--event-type SE` for skipped exon; `-e` is the rMATS event file.

### With GTF annotation
**Args:** `rmats2sashimiplot --b1 s1.bam --b2 s2.bam -o plots/ --event-type A3SS -e events.A3SS.txt --gtf genes.gtf`
**Explanation:** `--gtf` provides gene models to draw exon/intron structures correctly.

### With read groups
**Args:** `rmats2sashimiplot --b1 s1.bam --b2 s2.bam -o plots/ --event-type A5SS -e events.txt --rg1 1 --rg2 2`
**Explanation:** `--rg1`/`--rg2` specify BAM read group tags for proper sample labeling.

### Single sample plot
**Args:** `rmats2sashimiplot --b1 single.bam -o plots/ --event-type RI -e events.RI.txt --no-stats`
**Explanation:** `--no-stats` skips statistical summary; plots read coverage for one sample only.

### Custom output format
**Args:** `rmats2sashimiplot --b1 s1.bam --b2 s2.bam -o plots/ --event-type MXE -e events.txt --format pdf`
**Explanation:** `--format pdf` outputs PDF instead of default PNG for publication-quality figures.

### With LRU cache
**Args:** `rmats2sashimiplot --b1 s1.bam --b2 s2.bam -o plots/ --event-type SE -e events.txt --lru 200`
**Explanation:** `--lru 200` increases BAM caching for faster repeated access during plot generation.