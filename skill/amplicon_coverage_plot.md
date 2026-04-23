---
name: amplicon_coverage_plot
category: qc
description: Generate interactive coverage barplots for amplicon sequencing from BED/BAM files
tags: [amplicon, coverage, visualization, plotly, bam, bed]
author: oxo-call-community
source_url: "https://github.com/chienchi/amplicon_coverage_plot"
---

## Concepts

- **Tool Overview**: amplicon_coverage_plot (amplicov) generates interactive barplots visualizing amplicon coverage depth from sequencing data. Version 0.3.4.
- **Input Formats**: Accepts amplicon coordinates in BED6 or BEDPE format, and coverage data from sorted BAM files or pre-computed coverage files.
- **Interactive Output**: Produces HTML files with Plotly-based interactive visualizations allowing zoom, hover, and data exploration.
- **Coverage Metrics**: Calculates and displays per-amplicon coverage statistics, highlighting regions below coverage thresholds (default: <5x black, <20x blue).
- **Primer Handling**: Optional `--count_primer` flag to include overlapping primer regions in unique coverage calculations.
- **Ambiguous Site Detection**: Identifies positions with coverage below threshold (default 10x) as ambiguous N sites.
- **Reference Lines**: Displays depth reference lines at configurable levels (default: 5, 10, 20, 50x) for quick quality assessment.

## Pitfalls

- **BAM File Sorting**: Input BAM files must be coordinate-sorted. Use `samtools sort` if needed.
- **Properly Paired Reads**: Use `--pp` flag only for Illumina paired-end data to filter for properly paired reads.
- **Coverage Thresholds**: Default mincov=10 for ambiguous site detection may be too low for some applications. Adjust based on required confidence.
- **Reference ID Matching**: BED file chromosome names must match BAM file reference names exactly (e.g., "chr1" vs "1").
- **Memory Usage**: Large BAM files may require significant memory. Consider downsampling or using pre-computed coverage files.

## Examples

### Generate coverage plot from BAM and BED
**Args:** `amplicov --bed amplicons.bed --bam aligned.bam -o output_dir -p sample1`
**Explanation:** Basic usage: creates interactive barplot from amplicon coordinates (BED6) and aligned reads (BAM). Outputs sample1_amplicon_coverage.html and sample1_amplicon_coverage.txt.

### Use BEDPE format for paired amplicons
**Args:** `amplicov --bedpe amplicons.bedpe --bam aligned.bam -o results/ -p experiment1`
**Explanation:** Uses BEDPE format for paired-end amplicon definitions. Suitable for amplicon panels with primer pair information.

### Filter for properly paired reads
**Args:** `amplicov --bed amplicons.bed --bam aligned.bam --pp -o output/ -p sample_pp`
**Explanation:** Filters BAM to include only properly paired reads (Illumina-specific). Useful for removing chimeric or improperly aligned reads.

### Include primer regions in coverage
**Args:** `amplicov --bed amplicons.bed --bam aligned.bam --count_primer -o output/ -p sample_with_primers`
**Explanation:** Counts overlapping primer regions toward unique coverage. Appropriate when primer sequences are part of the target region.

### Adjust coverage thresholds
**Args:** `amplicov --bed amplicons.bed --bam aligned.bam --mincov 20 --depth_lines 10 30 50 100 -o output/ -p high_coverage`
**Explanation:** Sets minimum coverage for ambiguous site detection to 20x (default 10). Custom depth reference lines at 10, 30, 50, 100x. Use for high-depth amplicon panels.

### Use pre-computed coverage file
**Args:** `amplicov --bed amplicons.bed --cov coverage.txt -o output/ -p from_cov`
**Explanation:** Uses pre-computed coverage file (format: position<tab>coverage) instead of BAM. Faster for repeated analyses with same coverage data.

### Add GFF annotation for hover info
**Args:** `amplicov --bed amplicons.bed --bam aligned.bam --gff annotations.gff -o output/ -p annotated`
**Explanation:** Includes GFF annotation data in hover information on the plot. Useful for identifying which genes/features are covered by each amplicon.
