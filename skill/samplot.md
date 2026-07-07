---
name: samplot
category: visualization
description: Plot structural variant signals from BAMs and CRAMs
tags: ["samplot", "structural variants", "visualization", "BAM", "CRAM"]
author: oxo-call-community
source_url: "https://github.com/ryanlayer/samplot"
---

## Concepts

- **Tool Overview**: Samplot (v1.3.0) is a visualization tool for plotting structural variant signals from BAM and CRAM alignment files, enabling visual validation of variant calls.
- **Core Function**: Generates publication-quality plots of read alignments around structural variants, showing split reads, discordant pairs, and coverage patterns.
- **Algorithm**: Extracts alignment information from BAM/CRAM files, identifies variant-supporting reads, and generates visual representations.
- **Input Format**: BAM/CRAM alignment files, VCF variant files, reference genome.
- **Output Format**: SVG/PNG plots, PDF reports, interactive HTML visualizations.
- **Use Case**: Variant validation, publication figure generation, quality control, structural variant analysis.

## Pitfalls

- **Memory requirements**: Large BAM files require significant memory.
- **Reference genome**: Requires indexed reference genome for CRAM support.
- **Variant format**: VCF must contain proper structural variant annotations.
- **Plot quality**: Depends on sequencing coverage and read quality.
- **Computational time**: Generating plots for large regions can be slow.
- **File indexing**: BAM/CRAM files must be indexed for efficient access.

## Examples

### Plot single variant
**Args:** `samplot plot -b sample.bam -v variants.vcf -o sv_plot.png -c chr1:1000000-1005000`
**Explanation:** `-b` BAM file; `-v` VCF file; `-o` output plot; `-c` region.

### Multiple BAMs
**Args:** `samplot plot -b sample1.bam sample2.bam -v variants.vcf -o comparison.png`
**Explanation:** Plots multiple samples for comparison.

### Output SVG
**Args:** `samplot plot -b sample.bam -v variants.vcf -o sv_plot.svg`
**Explanation:** Outputs in SVG format for vector graphics.

### Include coverage
**Args:** `samplot plot -b sample.bam -v variants.vcf -o sv_plot.png --coverage`
**Explanation:** `--coverage` shows read coverage track.

### Highlight variants
**Args:** `samplot plot -b sample.bam -v variants.vcf -o sv_plot.png --highlight`
**Explanation:** `--highlight` emphasizes variant-supporting reads.

### Interactive HTML
**Args:** `samplot plot -b sample.bam -v variants.vcf -o sv_plot.html --format html`
**Explanation:** Generates interactive HTML visualization.

### Batch processing
**Args:** `samplot batch -i variants.txt -o plots_dir`
**Explanation:** Processes multiple variants in batch mode.