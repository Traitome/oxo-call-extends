---
name: bamdash
category: formatting
description: BAMdash - Aggregate pathogen NGS results into interactive visualization
tags: [bamdash, formatting, BAM, visualization, pathogen-analysis]
author: oxo-call-community
source_url: "https://github.com/jonas-fuchs/BAMdash/blob/v.0.4.5/README.md"
---

## Concepts

- **Tool Overview**: BAMdash aggregates pathogen NGS results into interactive visualization plots for comprehensive analysis. Version 0.4.5.
- **Core Function**: Creates interactive visualizations from BAM files to explore pathogen sequencing results.
- **Interactive Plots**: Generates interactive HTML plots for exploring coverage, variants, and mapping statistics.
- **Pathogen Focus**: Designed specifically for pathogen sequencing data analysis.
- **Coverage Visualization**: Visualizes sequencing coverage across pathogen genomes.
- **Variant Display**: Shows identified variants in context with coverage data.
- **Input/Output**: Accepts BAM alignment files, outputs interactive HTML visualization.
- **Installation**: `conda install -c bioconda bamdash`.

## Pitfalls

- **Pathogen Specific**: Optimized for pathogen analysis. May not work well with human/mammalian genomes.
- **BAM Requirements**: Requires properly aligned and indexed BAM files.
- **Memory Usage**: Large BAM files may require significant memory.
- **Output Size**: Interactive HTML files can be large with extensive data.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Basic visualization
**Args:** `bamdash -i alignments.bam -o report.html`
**Explanation:** Creates interactive visualization from BAM file.

### Multiple samples
**Args:** `bamdash -i sample1.bam sample2.bam -o comparison.html`
**Explanation:** Compares multiple samples in single interactive plot.

### Specify reference
**Args:** `bamdash -i alignments.bam -r reference.fasta -o report.html`
**Explanation:** Uses reference genome for annotation in visualization.

### Include variants
**Args:** `bamdash -i alignments.bam -v variants.vcf -o report.html`
**Explanation:** Integrates variant calls into visualization.

### Custom title
**Args:** `bamdash -i alignments.bam -o report.html --title "Pathogen Analysis Report"`
**Explanation:** Sets custom title for the visualization report.

### Output statistics
**Args:** `bamdash -i alignments.bam -o report.html -s stats.txt`
**Explanation:** Outputs statistics alongside visualization.

### Display help
**Args:** `bamdash --help`
**Explanation:** Shows all available command-line options and usage information.