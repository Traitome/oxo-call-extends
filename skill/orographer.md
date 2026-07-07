---
name: orographer
category: alignment
description: Orographer visualizes alignments from BAM files with interactive HTML plots.
tags: [orographer, alignment, visualization, bam]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/Orographer"
---

## Concepts

- **Tool Overview**: Orographer generates interactive alignment visualizations from BAM files.
- **Core Function**: Creates Bokeh-based HTML plots for reviewing alignments.
- **Algorithm**: Uses Bokeh library for interactive visualization.
- **Input Format**: Accepts BAM files, GTF/GFF3 gene tracks, and VCF variants.
- **Output**: Produces interactive HTML plots.
- **Use Case**: Alignment review, variant visualization, and data exploration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large BAM files require memory.
- **Computational Cost**: Visualization can be computationally intensive.
- **Browser Compatibility**: HTML plots may require modern browsers.
- **File Size**: HTML output can be large.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orographer --help`
**Explanation:** Shows available options and usage instructions.

### Visualize BAM
**Args:** `orographer -i alignments.bam -o alignment_view.html`
**Explanation:** Creates visualization of alignments.

### With gene track
**Args:** `orographer -i alignments.bam -g genes.gtf -o alignment_view.html`
**Explanation:** Adds gene annotation track.

### With variants
**Args:** `orographer -i alignments.bam -v variants.vcf -o alignment_view.html`
**Explanation:** Overlays variants on alignment.

### Region selection
**Args:** `orographer -i alignments.bam -r chr1:1000-2000 -o region_view.html`
**Explanation:** Visualizes specific genomic region.

### Verbose mode
**Args:** `orographer -i alignments.bam -v -o alignment_view.html`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `orographer batch -d bams/ -o views/`
**Explanation:** Processes multiple BAM files.